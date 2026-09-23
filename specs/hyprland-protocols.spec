Name:           hyprland-protocols
Version:        0.7.1
Release:        1%{?dist}
Summary:        Wayland protocol extensions for Hyprland

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols
Source0:        https://github.com/hyprwm/hyprland-protocols/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  cmake

%description
Wayland protocol extension XMLs for Hyprland (toplevel export,
global shortcuts, focus grab, input capture, lock notify, ...),
with pkg-config file. Newer than the Fedora package, required
by hypridle/hyprlock builds.

%prep
%autosetup -n hyprland-protocols-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_datadir}/hyprland-protocols/
%{_datadir}/pkgconfig/hyprland-protocols.pc

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 0.7.1-1
- Initial package (clone for biyuan/software)
