Name:           jetbrainsmono-nerd-fonts
Version:        3.5.1
Release:        1%{?dist}
Summary:        JetBrains Mono Nerd Font (patched with icons)

License:        OFL-1.1
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/JetBrainsMono.tar.xz#/%{name}-%{version}.tar.xz

BuildArch:      noarch

%description
JetBrains Mono patched with Nerd Fonts icon glyphs, for terminals,
editors and status bars (Waybar, quickshell) that need icon fonts.

%prep
%setup -q -c -n %{name}-%{version} -T
tar xf %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/nerd-fonts/JetBrainsMono
install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/nerd-fonts/JetBrainsMono/

%files
%license OFL.txt
%{_datadir}/fonts/nerd-fonts/JetBrainsMono/

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 3.5.1-1
- Initial package (clone terra's fonts into biyuan/software)
