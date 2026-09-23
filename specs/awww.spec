Name:           awww
Version:        0.12.1
Release:        1%{?dist}
Summary:        Animated wallpaper daemon for Wayland

License:        GPL-3.0-only
URL:            https://codeberg.org/LGFae/awww
Source0:        https://codeberg.org/LGFae/awww/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust

%description
awww is an animated wallpaper daemon for Wayland compositors,
with a client (awww) and daemon (awww-daemon). Set static or
animated wallpapers with transitions and effects.

%prep
%setup -q -n %{name}

%build
cargo build --release

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 target/release/awww target/release/awww-daemon %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/awww
%{_bindir}/awww-daemon

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 0.12.1-1
- Initial package (clone terra's package into biyuan/software)
