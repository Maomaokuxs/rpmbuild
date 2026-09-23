# rpmbuild

**COPR：** `https://copr.fedorainfracloud.org/coprs/biyuan/software/`

## 安装

```bash
sudo dnf copr enable biyuan/software
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
| kazumi | 2.3.4 | 二次元追番 |
| hmcl | 3.16.3 | Minecraft 启动器 |
| bilibili | 1.19.0 | Bilibili 客户端 |
| miyu | 0.6.2 | 终端 AI 助手 |
| splayer | 3.1.1 | 音乐播放器 |
| splayer-next | 1.1.0 | 音乐播放器 |
| rime-ice | 2026.06.30 | 雾凇拼音 |
| grub-btrfs | 4.14 | GRUB Btrfs 快照 |
| waypaper | 2.9 | 壁纸管理器 |
| hellwal | 1.0.8 | 终端取色 |
| kde-material-you-colors | 2.2.0 | KDE Material You |
| fcitx5-mellow-themes | 1.10.1 | fcitx5 圆角主题 10 款 |
| fcitx5-hud-paper | 1.0 | 自制 Hud Paper 主题（浅/深） |
| biyuan-niri-config | 20260922 | niri 桌面配置模板+部署脚本 |
| biyuan-niri-desktop | 20260922 | niri 桌面元包（拉齐应用依赖） |
| hyprwayland-scanner | 0.4.6 | wayland-scanner C++ 版（构建工具） |
| hyprutils | 0.14.2 | Hyprland C++ 基础库 |
| hyprlang | 0.6.8 | Hyprland 配置语言库 |
| hyprgraphics | 0.5.1 | Hyprland 图像加载库 |
| hypridle | 0.1.8 | Hyprland 闲置守护进程 |
| hyprlock | 0.9.6 | Hyprland 锁屏 |
| hyprland-protocols | 0.7.1 | Hyprland Wayland 协议扩展 |
| jetbrainsmono-nerd-fonts | 3.5.1 | JetBrainsMono 图标字体 |
| python3-materialyoucolor | 3.0.4 | Material You 纯 Python 算法库 |
| python3-screeninfo | 0.8.1 | 屏幕信息查询库 |
| sarasa-gothic-fonts | 1.0.41 | 更纱黑体 CJK 编程字体 |
| awww | 0.12.1 | Wayland 动态壁纸守护进程 |
| starship | 1.26.0 | 极简快速的 shell 提示符 |
| lxgw-wenkai | 1.522 | 霞鹜文楷 CJK 字体（常规+等宽） |

## 许可

各包遵循上游许可，spec 采用 MIT。
