Name:           fcitx5-mellow-themes
Version:        1.10.1
Release:        1%{?dist}
Summary:        Mellow themes for fcitx5 (rounded rectangle design)

License:        BSD-2-Clause
URL:            https://github.com/sanweiya/fcitx5-mellow-themes
# Upstream has no tags; snapshot of main branch (theme.conf says 1.10)
Source0:        https://github.com/sanweiya/fcitx5-mellow-themes/archive/refs/heads/main.tar.gz

BuildArch:      noarch
Requires:       fcitx5

%description
Mellow is a set of aesthetic, modern fcitx5 themes featuring rounded
rectangle design. This package ships all 10 variants (graphite,
sakura, vermilion, wechat, youlan, each in light and dark).

%prep
%setup -q -n fcitx5-mellow-themes-main

%build

%install
mkdir -p %{buildroot}%{_datadir}/fcitx5/themes
cp -a mellow-graphite mellow-graphite-dark \
      mellow-sakura mellow-sakura-dark \
      mellow-vermilion mellow-vermilion-dark \
      mellow-wechat mellow-wechat-dark \
      mellow-youlan mellow-youlan-dark \
      %{buildroot}%{_datadir}/fcitx5/themes/

%files
%license LICENSE
%{_datadir}/fcitx5/themes/mellow-*/

%changelog
* Sat Sep 19 2026 Maomaokuxs <biyuanh@qq.com> - 1.10-1
- Initial package (10 themes; KWin blur variants discontinued upstream)
