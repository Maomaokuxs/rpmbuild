Name:           maple-mono-nf-cn
Version:        7.9
Release:        1%{?dist}
Summary:        Maple Mono NF CN coding font with CJK and icons

License:        OFL-1.1
URL:            https://github.com/subframe7536/maple-font
Source0:        https://github.com/subframe7536/maple-font/releases/download/v%{version}/MapleMono-NF-CN.zip
Source1:        https://raw.githubusercontent.com/subframe7536/maple-font/v%{version}/OFL.txt#/maple-mono-nf-cn-OFL.txt

BuildArch:      noarch
BuildRequires:  unzip

%description
Maple Mono NF CN is a monospace coding font with Nerd Font icons
and CJK glyph coverage, featuring coding ligatures and warm
rounded letterforms.

%prep
%setup -q -c -n %{name}-%{version} -T
unzip -q -o %{SOURCE0} '*.ttf'
cp %{SOURCE1} OFL.txt

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/maple-mono-nf-cn
install -m 644 *.ttf %{buildroot}%{_datadir}/fonts/maple-mono-nf-cn/

%files
%license OFL.txt
%{_datadir}/fonts/maple-mono-nf-cn/

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 7.9-1
- Initial package
