Name:           hyprwayland-scanner
Version:        0.4.6
Release:        1%{?dist}
Summary:        Hyprland version of wayland-scanner for C++

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwayland-scanner
Source0:        https://github.com/hyprwm/hyprwayland-scanner/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(pugixml)

%description
hyprwayland-scanner is Hyprland's version of wayland-scanner,
generating C++ bindings from Wayland protocol XML files.
It is a build-time tool required by hypridle, hyprlock and
other Hyprland ecosystem projects.

%prep
%autosetup -n hyprwayland-scanner-%{version}

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/hyprwayland-scanner

%changelog
* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.4.6-1
- Initial package (clone for biyuan/software)
