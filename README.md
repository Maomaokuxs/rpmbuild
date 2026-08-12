# rpmbuild

COPR 打包规范文件仓库（spec + assets）。

仓库结构：
```
rpmbuild/
├── specs/     # 各包的 .spec 文件
├── assets/    # 图标、LICENSE 等小文件（spec 通过 raw.githubusercontent URL 引用）
└── .gitignore
```

## 构建流程

普通包（Source0 为远程 URL）可直接提交 COPR：
```bash
copr-cli build biyuan/apps specs/<pkg>.spec
```

## 特殊包

以下包的 Source0 是本地构建产物，需要先把 tar.gz 放入 `~/rpmbuild/SOURCES/`，
再本地生成 SRPM 后提交：

| 包 | 说明 |
|----|------|
| splayer-next | Electron 应用，需本地 `pnpm build:unpack` 后打 tar.gz |
| clipflux | Flutter 应用，本地打包的 clipflux-1.0.0.tar.gz |

本地生成 SRPM 并提交：
```bash
cp <artifact>.tar.gz ~/rpmbuild/SOURCES/
rpmbuild -bs specs/<pkg>.spec
copr-cli build biyuan/apps ~/rpmbuild/SRPMS/<pkg>-*.src.rpm
```

## 更新版本

1. 修改 `specs/<pkg>.spec` 的 `Version:`（及写死的 Source0 版本号）
2. 提交推送 GitHub
3. COPR 通过 webhook 自动构建

## 已知包

- kazumi / hmcl / bilibili / miyu / splayer / splayer-next
- rime-ice / grub-btrfs / waypaper / clipflux / clipshare
