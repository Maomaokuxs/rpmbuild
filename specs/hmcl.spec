%global debug_package %{nil}

Name:           hmcl
Version:        3.16.3
Release:        1%{?dist}
Summary:        Hmcl 应用

License:        Unknown
URL:            https://github.com/HMCL-dev/HMCL
Source0:        https://github.com/HMCL-dev/HMCL/releases/download/v3.16.3/HMCL-3.16.3.jar
Source1:        https://raw.githubusercontent.com/Maomaokuxs/rpmbuild/main/assets/hmcl/hmcl-icon.png
Requires:       java
BuildRequires:  desktop-file-utils
BuildRequires:  chrpath

%description
Hmcl 第三方应用。

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE0} %{buildroot}%{_libdir}/%{name}/HMCL-%{version}.jar
cat > %{buildroot}%{_bindir}/%{name} <<WRAPEOF
#!/bin/sh
exec java -Dglass.gtk.uiScale=1.5 -jar %{_libdir}/%{name}/HMCL-%{version}.jar "$@"
WRAPEOF
chmod +x %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<DESKEOF
[Desktop Entry]
Name=Hmcl
Comment=Hmcl 应用
Exec=java -Dglass.gtk.uiScale=1.5 -jar %{_libdir}/%{name}/HMCL-%{version}.jar
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
StartupWMClass=Hmcl
DESKEOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Sun Jul 26 2026 Maomaokuxs <biyuanh@qq.com> - 3.16.3-1
- Update to 3.16.3
