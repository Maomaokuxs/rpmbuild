Name:           hyprlock
Version:        0.9.6
Release:        1%{?dist}
Summary:        Hyprland screen locker

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprlock
Source0:        https://github.com/hyprwm/hyprlock/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hyprwayland-scanner
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(hyprgraphics) >= 0.1.6
BuildRequires:  pkgconfig(hyprland-protocols) >= 0.6.0
BuildRequires:  pkgconfig(hyprlang) >= 0.6.0
BuildRequires:  pkgconfig(hyprutils) >= 0.11.0
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
hyprlock is Hyprland's GPU-accelerated screen locker with
blur, background images, and per-monitor input fields.

%prep
%autosetup -n hyprlock-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/hyprlock
%config(noreplace) %{_sysconfdir}/pam.d/hyprlock
%{_datadir}/hypr/hyprlock.conf

%changelog
* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.9.6-1
- Initial package (clone for biyuan/software)
