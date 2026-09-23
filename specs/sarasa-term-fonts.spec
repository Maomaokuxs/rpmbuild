Name:           sarasa-term-fonts
Version:        1.0.41
Release:        1%{?dist}
Summary:        Sarasa Term CJK programming font (terminal)

License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/SarasaTerm-TTF-%{version}.zip
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%{version}/LICENSE#/sarasa-term-LICENSE

BuildArch:      noarch
BuildRequires:  unzip

%description
Sarasa Term SC (更纱黑体终端·简体中文) is the Simplified Chinese
terminal-emulator variant of the Sarasa Gothic CJK programming
font family, with half-width latin glyphs for clean terminal
rendering. For other variants see sarasa-gothic-fonts and
sarasa-mono-fonts.

%prep
%setup -q -c -n %{name}-%{version} -T
unzip -q -o %{SOURCE0} 'SarasaTermSC-*.ttf'
cp %{SOURCE1} LICENSE

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/sarasa-term
install -m 644 SarasaTermSC-*.ttf %{buildroot}%{_datadir}/fonts/sarasa-term/

%files
%license LICENSE
%{_datadir}/fonts/sarasa-term/

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.41-1
- Initial package
