Name:           waypaper
Version:        2.9
Release:        1%{?dist}
Summary:        GUI wallpaper manager for Wayland and Xorg

License:        GPL-3.0
URL:            https://github.com/anufrievroman/waypaper
Source0:        https://github.com/anufrievroman/waypaper/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros
Requires:       python3
Requires:       python3-pillow
Requires:       python3-gobject
Requires:       gtk3

%description
Waypaper is a GUI wallpaper manager for Wayland and Xorg,
supporting swaybg, swww, feh, hyprpaper, and other backends.

%prep
%setup -q

%build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --optimize=1

%files
%{_bindir}/waypaper
%{_bindir}/waypaperd
%{python3_sitelib}/waypaper/
%{python3_sitelib}/waypaper-%{version}-py*.egg-info/
%{_datadir}/applications/waypaper.desktop
%{_datadir}/icons/hicolor/*/apps/waypaper.*
%{_datadir}/systemd/user/waypaperd.service
%{_mandir}/man1/waypaper.1*

%changelog
* Thu Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 2.9-1
- Update to 2.9

* Thu Jul 10 2025 Maomaokuxs <biyuanh@qq.com> - 2.8-1
- Initial packaging
