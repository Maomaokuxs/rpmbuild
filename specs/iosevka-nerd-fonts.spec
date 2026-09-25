# 400MB+ TTF 几乎压不动，用 gzip-1 换速度(包大一点无所谓)
%define _binary_payload w1.gzdio
%global debug_package %{nil}

Name:           iosevka-nerd-fonts
Version:        3.5.1
Release:        1%{?dist}
Summary:        Iosevka patched with Nerd Fonts glyphs
License:        MIT AND OFL-1.1
URL:            https://github.com/ryanoasis/nerd-fonts
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v3.5.1/Iosevka.tar.xz#/%{name}-%{version}.tar.xz
BuildArch:      noarch

%description
Iosevka monospace font patched with Nerd Fonts icons
(81 TTFs: proportional IosevkaNerdFont + IosevkaNerdFontMono),
for terminals, editors and status bars.

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
tar -xf %{SOURCE0} -C %{name}-%{version}
cp %{name}-%{version}/LICENSE.md .

%build
# nothing to compile

%install
mkdir -p %{buildroot}%{_datadir}/fonts/%{name}
install -m 644 %{name}-%{version}/*.ttf %{buildroot}%{_datadir}/fonts/%{name}/

%files
%license LICENSE.md
%{_datadir}/fonts/%{name}/

%changelog
* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 3.5.1-1
- Initial package, Nerd Fonts v3.5.1 Iosevka (81 TTFs)
