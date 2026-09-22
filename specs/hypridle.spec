Name:           hypridle
Version:        0.1.8
Release:        1%{?dist}
Summary:        Hyprland idle daemon

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hypridle
Source0:        https://github.com/hyprwm/hypridle/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hyprwayland-scanner
BuildRequires:  pkgconfig(hyprland-protocols) >= 0.6.0
BuildRequires:  pkgconfig(hyprlang) >= 0.6.0
BuildRequires:  pkgconfig(hyprutils) >= 0.2.0
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
hypridle is Hyprland's idle management daemon: run commands on
idle timeouts (screen lock, suspend, DPMS) and resume events.

%prep
%autosetup -n hypridle-%{version}

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/hypridle
%{_userunitdir}/hypridle.service
%{_datadir}/hypr/hypridle.conf

%changelog
* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.1.8-1
- Initial package (clone for biyuan/software)
