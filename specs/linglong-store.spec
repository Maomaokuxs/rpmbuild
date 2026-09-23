%global debug_package %{nil}

Name:           linglong-store
Version:        3.6.0
Release:        2%{?dist}
Summary:        Linglong application store (community edition)

License:        MIT
URL:            https://github.com/HanHan666666/flutter-linglong-store
Source0:        https://github.com/HanHan666666/flutter-linglong-store/releases/download/v%{version}/linglong-store-%{version}-1.x86_64.rpm

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

%description
Linyaps Store Community Edition is a Flutter-based graphical
front-end for browsing and installing Linglong applications.
Repackaged from the official upstream RPM without modification.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
rpm2cpio %{SOURCE0} | cpio -idm

%build

%install
mkdir -p %{buildroot}
cp -a %{name}-%{version}/opt %{buildroot}/
cp -a %{name}-%{version}/usr %{buildroot}/
# 上游构建机残留的 /tmp runpath 在本机必然失效，直接删掉
for f in %{buildroot}/opt/linglong-store/lib/*.so; do
    chrpath -d "$f" 2>/dev/null || true
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/linglong-store.desktop

%files
%license /opt/linglong-store/LICENSE
/opt/linglong-store/
%{_bindir}/linglong-store
%{_datadir}/applications/linglong-store.desktop
%{_datadir}/applications/com.dongpl.linglong-store.v2.desktop
%{_datadir}/icons/hicolor/256x256/apps/linglong-store.png
%{_datadir}/metainfo/linglong-store.appdata.xml

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 3.6.0-2
- Repack official upstream RPM for biyuan/software (supersedes manual install)
