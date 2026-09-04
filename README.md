# rpmbuild

COPR `biyuan/apps` 的 spec 与资源仓库，通过 SCM + webhook 自动构建。

**COPR：** `https://copr.fedorainfracloud.org/coprs/biyuan/apps/`

## 安装

```bash
sudo dnf copr enable biyuan/apps
sudo dnf install <package>
```

## 仓库结构

```text
specs/                  # 各包 .spec
assets/<pkg>/           # 图标、LICENSE 等（spec 通过 raw.githubusercontent 引用）
  bilibili/
  hmcl/
  kazumi/
  splayer/
  splayer-next/
  hellwal/
  ...
```

## 已打包程序

| 包名 | 版本 | 说明 |
| --- | --- | --- |
| kazumi | 2.3.0 | 二次元追番 |
| hmcl | 3.16.3 | Minecraft 启动器 |
| bilibili | 1.18.0 | Bilibili 客户端 |
| miyu | 0.4.6 | 终端 AI 助手 |
| splayer | 3.1.1 | 音乐播放器 |
| splayer-next | 1.1.0 | 音乐播放器 |
| rime-ice | 2026.06.30 | 雾凇拼音 |
| grub-btrfs | 4.14 | GRUB Btrfs 快照 |
| waypaper | 2.9 | 壁纸管理器 |
| hellwal | 1.0.7 | 终端取色 |
| kde-material-you-colors | 2.2.0 | KDE Material You |

## 构建

**SCM 自动构建：** `specs/` 推送到 GitHub 后，COPR webhook 自动对 11 个包排队构建。

## 特殊包

- `splayer-next` / `waypaper` 等含二进制/新服务，需同步 `%files`

## 许可

各包遵循上游许可，spec 采用 MIT。
