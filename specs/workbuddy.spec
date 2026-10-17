%global debug_package %{nil}
%global __os_install_post %{nil}
%global __arch_install_post %{nil}

Name:           workbuddy
Version:        5.6.2
Release:        1%{?dist}
Summary:        WorkBuddy Desktop - AI Agent Desktop Application

License:        Proprietary
URL:            https://www.workbuddy.cn
Source0:        https://download.codebuddy.cn/workbuddy/saas/linux-x64-rpm/WorkBuddy-linux-x64-rpm-5.6.2.40046327-c7b525f3.rpm

ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  rpm
Requires:       alsa-lib, at-spi2-core, gtk3, libXScrnSaver, libnotify, mesa-libgbm, nss, xdg-utils
Requires:       libXtst, libuuid
Requires:       hicolor-icon-theme
AutoReqProv:    no

%description
WorkBuddy Desktop 官方 Linux 客户端。内容来自官网发布的 RPM 安装包，
仅重新打包，不修改任何程序文件。

安装位置：/opt/WorkBuddy

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
rpm2cpio %{SOURCE0} | cpio -idm

%build

%install
cd %{name}-%{version}
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -a opt %{buildroot}/
mkdir -p %{buildroot}%{_datadir}
cp -a usr/share/applications %{buildroot}%{_datadir}/
cp -a usr/share/icons %{buildroot}%{_datadir}/
# 终端里也能直接敲 workbuddy 启动
mkdir -p %{buildroot}%{_bindir}
ln -s /opt/WorkBuddy/workbuddy %{buildroot}%{_bindir}/workbuddy

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/workbuddy.desktop

%post
update-desktop-database -q %{_datadir}/applications || :
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :

%postun
update-desktop-database -q %{_datadir}/applications || :
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :

%files
/opt/WorkBuddy/
/usr/bin/workbuddy
%{_datadir}/applications/workbuddy.desktop
%{_datadir}/icons/hicolor/*/apps/workbuddy.png

%changelog
* Sat Oct 17 2026 Maomaokuxs <biyuanh@qq.com> - 5.6.2-1
- Initial package: repackage official Linux RPM (5.6.2.40046327), no program changes
