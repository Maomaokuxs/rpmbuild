%global debug_package %{nil}
%global __os_install_post %{nil}
%global __arch_install_post %{nil}

Name:           com.cmic.mcloud
Version:        1.1.1
Release:        3%{?dist}
Summary:        China Mobile Cloud Drive desktop client

License:        Proprietary
URL:            https://yun.139.com/
Source0:        https://yun.mcloud.139.com/mCloudPc/kylinV111/com.cmic.mcloud_1.1.1_amd64.deb

BuildRequires:  binutils
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
Requires:       gtk3, nss, alsa-lib, libXScrnSaver, libdrm, mesa-libgbm
Requires:       hicolor-icon-theme
AutoReqProv:    no

%description
中国移动云盘官方 Linux 客户端。内容来自官网提供的银河麒麟版
deb 包，仅重新打包为 rpm，不修改任何程序文件。
相对本地 -1 版：图标改走 hicolor 主题并修正分类。

安装位置：/usr/lib/com.cmic.mcloud

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
ar x %{SOURCE0}
tar --no-same-owner -xf data.tar.*

%build

%install
cd %{name}-%{version}
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/com.cmic.mcloud
# 应用本体统一进 /usr/lib（官方 deb 放在 /opt/apps，无他因）
cp -a opt/apps/com.cmic.mcloud/. %{buildroot}%{_libdir}/com.cmic.mcloud/
mkdir -p %{buildroot}%{_datadir}
cp -a usr/share/. %{buildroot}%{_datadir}/

# 修复官方包里指向厂商构建机的绝对符号链接
while IFS= read -r link; do
    [ -n "$link" ] || continue
    target=$(readlink "$link")
    case "$target" in /*) ;; *) continue ;; esac
    [ -e "$link" ] && continue
    base=$(basename "$target")
    if [ -e "$(dirname "$link")/$base" ]; then
        ln -sfn "$base" "$link"
    fi
done <<EOF
$(find %{buildroot}%{_libdir}/com.cmic.mcloud -type l 2>/dev/null)
EOF

# deb 自带全套 hicolor 图标，直接沿用；删掉厂商机器残留的点文件
find %{buildroot}%{_datadir}/icons -name ".*" -delete 2>/dev/null || true

# desktop 改走主题名、修正分类、Exec 跟随新路径
sed -i 's|^Icon=.*|Icon=com.cmic.mcloud|' %{buildroot}%{_datadir}/applications/com.cmic.mcloud.desktop
sed -i 's|^Categories=.*|Categories=Network;FileTransfer;|' %{buildroot}%{_datadir}/applications/com.cmic.mcloud.desktop
sed -i 's|^Exec=/opt/apps/com.cmic.mcloud|Exec=%{_libdir}/com.cmic.mcloud|' %{buildroot}%{_datadir}/applications/com.cmic.mcloud.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.cmic.mcloud.desktop || true

%post
update-desktop-database -q %{_datadir}/applications || :

%postun
update-desktop-database -q %{_datadir}/applications || :

%files
%{_libdir}/com.cmic.mcloud
%{_datadir}/applications/com.cmic.mcloud.desktop
%{_datadir}/icons/hicolor/*/apps/com.cmic.mcloud.png

%changelog
* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 1.1.1-3
- Move app dir to /usr/lib (repo path standard)
- Icon via hicolor theme + Network;FileTransfer categories (fixes missing launcher icon)
