%global debug_package %{nil}
%global __provides_exclude ^(%{_libdir}/%{name}/.*\.so)
%global __requires_exclude ^(libmpv|libflutter|libdart|libapp).*

Name:           bilibili
Version:        1.18.0
Release:        1%{?dist}
Summary:        Bilibili 应用

License:        Unknown
URL:            https://github.com/msojocs/bilibili-linux
Source0:        https://github.com/msojocs/bilibili-linux/releases/download/v1.18.0-1/bilibili-v1.18.0-1-x64.tar.gz
Source1:        https://raw.githubusercontent.com/Maomaokuxs/rpmbuild/main/assets/bilibili-icon.png

BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
BuildRequires:  rpm-build

%description
Bilibili 第三方应用。

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications
tar xzf %{SOURCE0} -C %{buildroot}%{_libdir}/%{name} 
for f in %{buildroot}%{_libdir}/%{name}/bin/bilibili %{buildroot}%{_libdir}/%{name}/lib/*.so; do
    chrpath -r '$ORIGIN/lib' "$f" 2>/dev/null || true
done
chmod +x %{buildroot}%{_libdir}/%{name}/bin/bilibili
ln -s %{_libdir}/%{name}/bin/bilibili %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<DESKEOF
[Desktop Entry]
Name=Bilibili
Comment=Bilibili 应用
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
StartupWMClass=Bilibili
DESKEOF
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Sun Jul 26 2026 Maomaokuxs <biyuanh@qq.com> - 1.18.0-1
- Update to 1.18.0-1
