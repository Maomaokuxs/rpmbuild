%global debug_package %{nil}

Name:           linglong-store
Version:        3.6.0
Release:        3%{?dist}
Summary:        Linglong application store (community edition)

License:        MIT
URL:            https://github.com/HanHan666666/flutter-linglong-store
Source0:        https://github.com/HanHan666666/flutter-linglong-store/releases/download/v%{version}/linglong-store-%{version}-1.x86_64.rpm

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

%description
Linyaps Store Community Edition is a Flutter-based graphical
front-end for browsing and installing Linglong applications.
Repackaged from the official upstream RPM, relocated from /opt
to /usr/lib per repo path standard.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
rpm2cpio %{SOURCE0} | cpio -idm

%build

%install
mkdir -p %{buildroot}%{_libdir}/linglong-store %{buildroot}%{_bindir} %{buildroot}%{_datadir}
# 应用本体统一进 /usr/lib；官方 wrapper 写死 /opt，改由我们生成
cp -a %{name}-%{version}/opt/linglong-store/. %{buildroot}%{_libdir}/linglong-store/
cat > %{buildroot}%{_bindir}/linglong-store <<WRAPEOF
#!/bin/sh
exec %{_libdir}/linglong-store/linglong_store "\$@"
WRAPEOF
chmod +x %{buildroot}%{_bindir}/linglong-store
cp -a %{name}-%{version}/usr/share/. %{buildroot}%{_datadir}/
# 上游构建机残留的 /tmp runpath 在本机必然失效，直接删掉
for f in %{buildroot}%{_libdir}/linglong-store/lib/*.so; do
    chrpath -d "$f" 2>/dev/null || true
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/linglong-store.desktop

%files
%license /usr/lib/linglong-store/LICENSE
%{_libdir}/linglong-store/
%{_bindir}/linglong-store
%{_datadir}/applications/linglong-store.desktop
%{_datadir}/applications/com.dongpl.linglong-store.v2.desktop
%{_datadir}/icons/hicolor/256x256/apps/linglong-store.png
%{_datadir}/metainfo/linglong-store.appdata.xml

%changelog
* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 3.6.0-3
- Move app dir to /usr/lib (repo path standard)

* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 3.6.0-2
- Repack official upstream RPM for biyuan/software (supersedes manual install)
