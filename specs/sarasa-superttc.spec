Name:           sarasa-superttc
Version:        1.0.41
Release:        1%{?dist}
Summary:        Sarasa SuperTTC complete CJK font collection

License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/Sarasa-SuperTTC-%{version}.zip
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%{version}/LICENSE#/sarasa-superttc-LICENSE

BuildArch:      noarch
BuildRequires:  unzip

%description
Sarasa SuperTTC is the complete Sarasa Gothic collection in a
single 800MB TrueType Collection: all families (Gothic, UI, Mono,
Term, Fixed) and all locales (SC, TC, HC, J, K, CL) with every
weight. Install this one package instead of the split
sarasa-*-fonts packages if you want everything.

%prep
%setup -q -c -n %{name}-%{version} -T
unzip -q -o %{SOURCE0} 'Sarasa-SuperTTC.ttc'
cp %{SOURCE1} LICENSE

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/sarasa-superttc
install -m 644 Sarasa-SuperTTC.ttc %{buildroot}%{_datadir}/fonts/sarasa-superttc/

%files
%license LICENSE
%{_datadir}/fonts/sarasa-superttc/

%changelog
* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.41-1
- Initial package (single-file complete collection)
