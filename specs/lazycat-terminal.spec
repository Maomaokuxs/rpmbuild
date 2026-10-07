%global debug_package %{nil}

Name:           lazycat-terminal
Version:        1.1.11
Release:        1%{?dist}
Summary:        Hackable terminal emulator with tabs, splits and transparent background

License:        GPL-3.0-or-later
URL:            https://github.com/manateelazycat/lazycat-terminal
Source0:        https://github.com/manateelazycat/lazycat-terminal/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(vte-2.91-gtk4)

%description
Lazycat Terminal is a high-performance terminal emulator written in Vala,
featuring tabs, split panes, transparent background and theme support.

%prep
%setup -q -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

# Icons, themes and default config are not installed by meson
install -Dm644 icons/lazycat-terminal.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/lazycat-terminal.svg
for size in 32 48 96 128; do
    install -Dm644 icons/${size}x${size}/lazycat-terminal.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/lazycat-terminal.png
done
install -dm755 %{buildroot}%{_datadir}/lazycat-terminal/theme
install -m644 theme/* %{buildroot}%{_datadir}/lazycat-terminal/theme/
install -Dm644 config.conf %{buildroot}%{_datadir}/lazycat-terminal/config.conf

%files
%license LICENSE
%doc README.md
%{_bindir}/lazycat-terminal
%{_datadir}/applications/lazycat-terminal.desktop
%{_datadir}/icons/hicolor/*/apps/lazycat-terminal.*
%{_datadir}/lazycat-terminal/

%changelog
* Sat Oct 03 2026 Maomaokuxs <biyuanh@qq.com> - 1.1.11-1
- Initial package
