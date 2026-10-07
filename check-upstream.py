#!/usr/bin/env python3
"""
check-upstream.py —— 扫描 specs/ 下所有包，对比上游最新版本。

不走 GitHub API（避免限额），原理：
  - 有 release 的仓库: https://github.com/<o>/<r>/releases/latest 会 302 跳到 tag
  - 没 release 的仓库: git ls-remote --tags 取最大 tag
  - rime-ice: nightly 的 full.zip 看 HTTP Last-Modified
  - PyPI 包: pypi.org/json

用法:
    ./check-upstream.py                    # 检查全部
    ./check-upstream.py rime-ice waypaper   # 只检查指定包
"""

import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime

SPECS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "specs")
GH = "https://github.com"
UA = {"User-Agent": "copr-upstream-checker"}

_cache = {}


def norm(v):
    return re.sub(r"^[vV]", "", v.strip())


def ver_key(v):
    key = []
    for p in re.split(r"[.\-+_~]", norm(v)):
        key.append((0, int(p)) if p.isdigit() else (1, p))
    return key


def cmp_ver(a, b):
    ka, kb = ver_key(a), ver_key(b)
    return (ka > kb) - (ka < kb)


def latest_release_tag(owner, repo):
    """有 release 的仓库，/releases/latest 会跳转到具体 tag。"""
    url = f"{GH}/{owner}/{repo}/releases/latest"
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        # 不跟跳转，自己读 Location
        opener = urllib.request.build_opener(NoRedirect())
        with opener.open(req, timeout=20) as r:
            pass
    except urllib.error.HTTPError as e:
        loc = e.headers.get("Location", "")
        m = re.search(r"/releases/tag/([^/]+)/?$", loc)
        if m:
            return m.group(1)
    except Exception as e:
        print(f"  ! {owner}/{repo} release 检查失败: {e}", file=sys.stderr)
    return None


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def latest_git_tag(owner, repo):
    """没 release 的仓库，用 git ls-remote 取最大 tag。"""
    try:
        out = subprocess.run(
            ["git", "ls-remote", "--tags", "--refs", f"{GH}/{owner}/{repo}.git"],
            capture_output=True, text=True, timeout=30,
        ).stdout
    except Exception as e:
        print(f"  ! {owner}/{repo} ls-remote 失败: {e}", file=sys.stderr)
        return None
    tags = set()
    for line in out.splitlines():
        m = re.search(r"refs/tags/(.+)$", line)
        if m:
            t = m.group(1)
            if re.match(r"^[vV]?\d", t):  # 只认像版本号的 tag
                tags.add(t)
    if not tags:
        return None
    return max(tags, key=ver_key)


def upstream_version(owner, repo):
    key = (owner, repo)
    if key not in _cache:
        _cache[key] = latest_release_tag(owner, repo) or latest_git_tag(owner, repo)
    return _cache[key]


def _rime_ice(owner, repo, spec_ver):
    """rime-ice 打的是 nightly 的 full.zip，看下载链接的 Last-Modified。"""
    url = f"{GH}/iDvel/rime-ice/releases/download/nightly/full.zip"
    req = urllib.request.Request(url, headers=UA, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            lm = r.headers.get("Last-Modified")
    except Exception as e:
        print(f"  ! rime-ice 检查失败: {e}", file=sys.stderr)
        return None
    if not lm:
        return None
    dt = datetime.strptime(lm, "%a, %d %b %Y %H:%M:%S %Z")
    return dt.strftime("%Y.%m.%d")


def _pypi(pkg):
    def f(owner, repo, spec_ver):
        try:
            req = urllib.request.Request(
                f"https://pypi.org/pypi/{pkg}/json", headers=UA)
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.load(r)["info"]["version"]
        except Exception:
            return None
    return f


def _codeberg(owner, repo):
    """Codeberg (Forgejo) 上游：releases API 取最新正式版，无 release 则取最大 tag。"""
    key = ("codeberg", owner, repo)
    if key in _cache:
        return _cache[key]
    v = None
    try:
        req = urllib.request.Request(
            "https://codeberg.org/api/v1/repos/%s/%s/releases?limit=10" % (owner, repo),
            headers=UA)
        with urllib.request.urlopen(req, timeout=20) as r:
            releases = json.load(r)
        for rel in releases:
            if not rel.get("draft") and not rel.get("prerelease"):
                v = rel.get("tag_name")
                break
        if not v:
            req = urllib.request.Request(
                "https://codeberg.org/api/v1/repos/%s/%s/tags?limit=20" % (owner, repo),
                headers=UA)
            with urllib.request.urlopen(req, timeout=20) as r:
                tags = json.load(r)
            names = [t["name"] for t in tags
                     if re.match(r"^[vV]?\d", t.get("name", ""))]
            v = max(names, key=ver_key) if names else None
    except Exception as e:
        print("  ! codeberg %s/%s 检查失败: %s" % (owner, repo, e), file=sys.stderr)
    _cache[key] = v
    return v


def _mcloud(owner, repo, spec_ver):
    """移动云盘：按官方下载 URL 规律探测新版本。

    https://yun.mcloud.139.com/mCloudPc/kylinV{MmP}/com.cmic.mcloud_{M.m.p}_amd64.deb
    探测 patch+1/+2、minor+1、major+1，返回存在的最大版本。
    """
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)$", spec_ver)
    if not m:
        return None
    M, mi, pa = map(int, m.groups())
    found = []
    for cand in [(M, mi, pa + 1), (M, mi, pa + 2), (M, mi + 1, 0), (M + 1, 0, 0)]:
        v = "%d.%d.%d" % cand
        seg = "kylinV%d%d%d" % cand
        url = ("https://yun.mcloud.139.com/mCloudPc/%s/"
               "com.cmic.mcloud_%s_amd64.deb" % (seg, v))
        req = urllib.request.Request(url, headers=UA, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                if r.status == 200:
                    found.append(v)
        except Exception:
            pass
    if not found:
        return spec_ver  # 没探测到更新的，视为与当前一致
    return max(found, key=ver_key)


SPECIAL = {
    "rime-ice": _rime_ice,
    "python3-materialyoucolor": _pypi("materialyoucolor"),
    "com.cmic.mcloud": _mcloud,
}

SKIP_RE = re.compile(r"yun\.139\.com|dec05eba\.com|pypi\.org")


def parse_spec(path):
    name = ver = url = rel = None
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            if name is None and line.startswith("Name:"):
                name = line.split(":", 1)[1].strip()
            elif ver is None and line.startswith("Version:") \
                    and not line.startswith("VersionControl"):
                ver = line.split(":", 1)[1].split()[0]
            elif rel is None and line.startswith("Release:"):
                rel = line.split(":", 1)[1].split()[0]
            elif url is None and line.startswith("URL:"):
                url = line.split(":", 1)[1].strip()
            if name and ver and url and rel:
                break
    # Release 去掉 %{?dist} 这类宏后缀，只留数字部分
    if rel:
        rel = re.sub(r"%\{.*", "", rel).strip()
        rel = re.sub(r"\.fc\d+$", "", rel)
    return name, ver, url, rel


def effective_version(ver, rel):
    """把 Release 并入版本号参与比较（如 bilibili 的 1.19.0-3）。"""
    if rel and re.match(r"^\d+$", rel):
        return "%s-%s" % (ver, rel)
    return ver


def main():
    only = set(sys.argv[1:])
    specs = sorted(p for p in os.listdir(SPECS_DIR) if p.endswith(".spec"))
    behind, unknown, skipped = [], [], []
    for spec in specs:
        name, ver, url, rel = parse_spec(os.path.join(SPECS_DIR, spec))
        ever = effective_version(ver, rel)
        if not name or not ver:
            continue
        if only and name not in only:
            continue
        if name in SPECIAL:
            up = SPECIAL[name](None, None, ver)
        elif not url or SKIP_RE.search(url or ""):
            skipped.append((name, "非 GitHub 上游"))
            continue
        else:
            m = re.match(r"https?://codeberg\.org/([^/]+)/([^/]+?)(?:\.git)?/?$", url)
            if m:
                up = _codeberg(m.group(1), m.group(2))
            else:
                m = re.match(r"https?://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", url)
                if not m:
                    skipped.append((name, "URL 无法解析: %s" % url))
                    continue
                up = upstream_version(m.group(1), m.group(2))
        if not up:
            unknown.append(name)
            print(f"UNKNOWN {name:28s} {ver} (上游无 release/tag)")
        elif cmp_ver(ever, up) < 0:
            behind.append(name)
            print(f"BEHIND  {name:28s} {ever} -> {norm(up)}")
        else:
            print(f"OK      {name:28s} {ver}")

    print(f"\n{len(behind)} 个落后, {len(unknown)} 个未知, {len(skipped)} 个跳过")
    for n, why in skipped:
        print(f"  跳过 {n}: {why}")


if __name__ == "__main__":
    main()
