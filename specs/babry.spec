Name:           babry
Version:        0.1.0
Release:        1%{?dist}
Summary:        Smart boundary-aware screenshot tool for Linux Wayland

License:        Apache-2.0
URL:            https://github.com/kregonia/babry
Source0:        https://github.com/kregonia/babry/releases/download/v%{version}/babry-amd64-linux
Source1:        https://raw.githubusercontent.com/kregonia/babry/v%{version}/LICENSE

BuildArch:      x86_64

Requires:       fontconfig
Requires:       libxkbcommon
Requires:       libwayland-client

%description
Babry is a smart boundary-aware screenshot tool for Linux Wayland.

%prep

%build

%install
install -Dm755 %{SOURCE0} %{buildroot}%{_bindir}/babry
install -Dm644 %{SOURCE1} %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/babry
%{_licensedir}/%{name}/LICENSE

%changelog
* Tue Oct 13 2026 Biyuan <biyuan@example.com> - 0.1.0-1
- Initial package
