%global debug_package %{nil}

Name:           rime-ice
Version:        2025.05.21
Release:        1%{?dist}
Summary:        雾凇拼音 - Rime 简体中文输入方案

License:        GPL-3.0
URL:            https://github.com/iDvel/rime-ice
Source0:        https://github.com/iDvel/rime-ice/releases/download/nightly/full.zip

BuildArch:      noarch
Requires:       librime

%description
雾凇拼音是长期维护的 Rime 简体中文词库和输入方案，
提供拼音、双拼、辅助码等多种输入模式。

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}
unzip -q %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir}/rime-data/rime-ice
mkdir -p %{buildroot}%{_bindir}
cd %{name}-%{version}
for d in */; do [ "$d" != "BUILDROOT/" ] && [ "$d" != "SPECPARTS/" ] && cp -a "$d" %{buildroot}%{_datadir}/rime-data/rime-ice/; done
cp -a ./*.yaml ./*.txt ./*.lua 2>/dev/null %{buildroot}%{_datadir}/rime-data/rime-ice/ || true

# 激活脚本
cat > %{buildroot}%{_bindir}/rime-ice-enable <<'EOF'
#!/bin/bash
DST="$HOME/.local/share/fcitx5/rime"
SRC="/usr/share/rime-data/rime-ice"
mkdir -p "$DST"
for f in "$SRC"/*; do
    ln -sf "$f" "$DST/$(basename "$f")"
done
echo "rime-ice 已启用，请执行 fcitx5-remote -r"
EOF
chmod +x %{buildroot}%{_bindir}/rime-ice-enable

%post
if [ -n "$SUDO_USER" ]; then
    DST=$(eval echo ~$SUDO_USER)/.local/share/fcitx5/rime
    mkdir -p "$DST"
    for f in %{_datadir}/rime-data/rime-ice/*; do
        ln -sf "$f" "$DST/$(basename "$f")" 2>/dev/null
    done
    echo "rime-ice 已自动部署到 $DST"
fi

%files
%dir %{_datadir}/rime-data/rime-ice
%{_datadir}/rime-data/rime-ice/
%{_bindir}/rime-ice-enable

%changelog
* Wed Jul 09 2025 Maomaokuxs <biyuanh@qq.com> - 2025.05.21-1
- Initial packaging
