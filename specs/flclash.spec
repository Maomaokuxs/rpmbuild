%global debug_package %{nil}
%global __os_install_post %{nil}
%global __arch_install_post %{nil}
%global __provides_exclude ^(%{_datadir}/%{name}/.*\\.so)

Name:           flclash
Version:        0.8.98
Release:        1%{?dist}
Summary:        Cross-platform proxy client built with Flutter

License:        GPL-3.0-only
URL:            https://github.com/chen08209/FlClash
Source0:        https://github.com/chen08209/FlClash/releases/download/v%{version}/FlClash-%{version}-linux-amd64.rpm

BuildRequires:  desktop-file-utils

%description
FlClash is a cross-platform proxy client (Clash/Mihomo front-end)
built with Flutter, supporting rule-based routing, TUN mode,
system tray integration and subscription management.
Repackaged from the official upstream RPM without modification.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
rpm2cpio %{SOURCE0} | cpio -idm

%build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}
# 只取 bin/share：官方包 usr/lib 下仅有无用的 .build-id 链接
cp -a %{name}-%{version}/usr/bin/* %{buildroot}%{_bindir}/
cp -a %{name}-%{version}/usr/share/. %{buildroot}%{_datadir}/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/FlClash.desktop

%files
%{_bindir}/FlClash
%{_datadir}/FlClash/
%{_datadir}/applications/FlClash.desktop
%{_datadir}/pixmaps/FlClash.png
%{_datadir}/metainfo/

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 0.8.98-1
- Initial package (repack official upstream RPM)
