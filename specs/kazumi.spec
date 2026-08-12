%global debug_package %{nil}
%global __provides_exclude ^(%{_libdir}/%{name}/.*\.so)
%global __requires_exclude ^(libmpv|libflutter|libdart|libapp).*

Name:           kazumi
Version:        2.2.7
Release:        1%{?dist}
Summary:        Kazumi 应用

License:        Unknown
URL:            https://github.com/Predidit/Kazumi
Source0:        https://github.com/Predidit/Kazumi/releases/download/2.2.7/Kazumi_linux_2.2.7_amd64.tar.gz
Source1:        https://raw.githubusercontent.com/Maomaokuxs/rpmbuild/main/assets/kazumi-icon.png

BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
BuildRequires:  rpm-build

%description
Kazumi 第三方应用。

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications
tar xzf %{SOURCE0} -C %{buildroot}%{_libdir}/%{name} --strip-components=1
for f in %{buildroot}%{_libdir}/%{name}/kazumi %{buildroot}%{_libdir}/%{name}/lib/*.so; do
    chrpath -r '$ORIGIN/lib' "$f" 2>/dev/null || true
done
chmod +x %{buildroot}%{_libdir}/%{name}/kazumi
ln -s %{_libdir}/%{name}/kazumi %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<DESKEOF
[Desktop Entry]
Name=Kazumi
Comment=Kazumi 应用
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
StartupWMClass=Kazumi
DESKEOF
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Wed Aug 12 2026 Maomaokuxs <biyuanh@qq.com> - 2.2.7-1
- Test webhook auto-rebuild

* Sun Jul 26 2026 Maomaokuxs <biyuanh@qq.com> - 2.2.7-1
- Update to 2.2.7
