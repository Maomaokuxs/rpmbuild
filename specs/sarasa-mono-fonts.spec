Name:           sarasa-mono-fonts
Version:        1.0.41
Release:        1%{?dist}
Summary:        Sarasa Mono CJK programming font (monospaced)

License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/SarasaMono-TTF-%{version}.zip
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%{version}/LICENSE#/sarasa-mono-LICENSE

BuildArch:      noarch
BuildRequires:  unzip

%description
Sarasa Mono (更纱黑体等宽) is the monospaced variant of the Sarasa
Gothic CJK programming font family, based on Source Han Sans and
Iosevka. For proportional and terminal variants see
sarasa-gothic-fonts and sarasa-term-fonts.

%prep
%setup -q -c -n %{name}-%{version} -T
unzip -q -o %{SOURCE0} 'SarasaMono-*.ttf'
cp %{SOURCE1} LICENSE

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/sarasa-mono
install -m 644 SarasaMono-*.ttf %{buildroot}%{_datadir}/fonts/sarasa-mono/

%files
%license LICENSE
%{_datadir}/fonts/sarasa-mono/

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.41-1
- Initial package
