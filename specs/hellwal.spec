Name:           hellwal
Version:        1.0.8
Release:        1%{?dist}
Summary:        Fast, extensible color palette generator in C

License:        MIT
URL:            https://github.com/danihek/hellwal
Source0:        https://github.com/danihek/hellwal/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Hellwal is a pywal-like color palette generator written in C.
It extracts a color palette from a wallpaper image and renders it
into templates for your terminal, editor, Waybar, and more.

%prep
%setup -q -n hellwal-%{version}

%build
make CFLAGS="%{optflags}" LDFLAGS="-lm"

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 hellwal %{buildroot}%{_bindir}/hellwal

%files
%{_bindir}/hellwal

%changelog
* Sat Sep 19 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.8-1
- Update to 1.0.8 (upstream tag has no v prefix)

* Thu Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.7-1
- Initial package