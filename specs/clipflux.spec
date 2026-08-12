%global debug_package %{nil}

Name: clipflux
Version: 1.0.0
Release: 1%{?dist}
Summary: Cross-platform clipboard sync tool
License: GPLv3+
URL: https://github.com/clipflux/clipflux
Source0: clipflux-1.0.0.tar.gz

Requires: gtk3
Requires: wl-clipboard

%description
ClipFlux is a cross-platform clipboard synchronization tool.
Sync your clipboard between Linux, Android, and Windows devices over LAN.

%prep
%setup -q -n clipflux-bundle

%install
mkdir -p %{buildroot}%{_libdir}/clipflux/lib
mkdir -p %{buildroot}%{_libdir}/clipflux/data
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
cp -p clipflux %{buildroot}%{_libdir}/clipflux/
cp -rp data/* %{buildroot}%{_libdir}/clipflux/data/
cp -rp lib/* %{buildroot}%{_libdir}/clipflux/lib/
cat > %{buildroot}%{_bindir}/clipflux << 'WRAPPER'
#!/bin/sh
export LD_LIBRARY_PATH=%{_libdir}/clipflux${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
exec %{_libdir}/clipflux/clipflux "$@"
WRAPPER
chmod +x %{buildroot}%{_bindir}/clipflux

cat > %{buildroot}%{_datadir}/applications/clipflux.desktop << DESKTOP
[Desktop Entry]
Version=1.0
Type=Application
Name=ClipFlux
Comment=Cross-platform clipboard sync
Exec=%{_libdir}/clipflux/clipflux
Icon=clipflux
Terminal=false
Categories=Utility;
DESKTOP

cp %{_builddir}/clipflux-bundle/clipflux.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/clipflux.png

%post
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache -q -t -f %{_datadir}/icons/hicolor 2>/dev/null || :
fi
if [ -x /usr/bin/update-desktop-database ]; then
  /usr/bin/update-desktop-database 2>/dev/null || :
fi

%postun
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  /usr/bin/gtk-update-icon-cache -q -t -f %{_datadir}/icons/hicolor 2>/dev/null || :
fi

%files
%{_bindir}/clipflux
%{_libdir}/clipflux/
%{_datadir}/applications/clipflux.desktop
%{_datadir}/icons/hicolor/256x256/apps/clipflux.png

%changelog
* Thu Jul 23 2026 ClipFlux Team <support@clipflux.example.com> - 1.0.0-1
- Initial release
