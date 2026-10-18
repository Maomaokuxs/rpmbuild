%global debug_package %{nil}
%global __os_install_post %{nil}
%global __arch_install_post %{nil}

Name:           wps-office
Version:        12.1.2.29183
Release:        1%{?dist}
Summary:        WPS Office - Word, Presentation, Spreadsheet and PDF

License:        Proprietary
URL:            https://www.wps.cn
Source0:        https://github.com/Maomaokuxs/rpmbuild/releases/download/wps-office-12.1.2.29183/wps-office-12.1.2.29183.AK.preread.sw.Personal-1-806792.x86_64.rpm

ExclusiveArch:  x86_64

BuildRequires:  desktop-file-utils
BuildRequires:  rpm
Requires:       libXScrnSaver
Requires:       hicolor-icon-theme
AutoReqProv:    no

%description
WPS Office 官方 Linux 客户端，包含 WPS 文字、WPS 演示、
WPS 表格和 PDF 组件。内容来自官网发布的 RPM 安装包，
仅重新打包，不修改任何程序文件。

安装位置：/opt/kingsoft/wps-office

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
mkdir -p %{buildroot}%{_bindir}
cp -a usr/bin/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}
cp -a usr/share/applications %{buildroot}%{_datadir}/
cp -a usr/share/icons %{buildroot}%{_datadir}/
cp -a usr/share/mime %{buildroot}%{_datadir}/ 2>/dev/null || :

%check
for d in %{buildroot}%{_datadir}/applications/wps-office-*.desktop; do
  desktop-file-validate "$d"
done

%post
update-desktop-database -q %{_datadir}/applications || :
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :

%postun
update-desktop-database -q %{_datadir}/applications || :
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :

%files
/opt/kingsoft/wps-office/
%{_bindir}/et
%{_bindir}/wpp
%{_bindir}/wps
%{_bindir}/wpspdf
%{_datadir}/applications/wps-office-*.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/mime/

%changelog
* Sun Oct 18 2026 Maomaokuxs <biyuanh@qq.com> - 12.1.2.29183-1
- Update to 12.1.2.29183
* Sun Oct 18 2026 Maomaokuxs <biyuanh@qq.com> - 11.1.0.11723-1
- Initial package: repackage official Linux RPM, no program changes
