Name:           lxgw-wenkai
Version:        1.522
Release:        1%{?dist}
Summary:        LXGW WenKai CJK font (regular and mono families)

License:        OFL-1.1
URL:            https://github.com/lxgw/LxgwWenKai
Source1:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/LXGWWenKai-Regular.ttf
Source2:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/LXGWWenKai-Medium.ttf
Source3:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/LXGWWenKai-Light.ttf
Source4:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/LXGWWenKaiMono-Regular.ttf
Source5:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/LXGWWenKaiMono-Medium.ttf
Source6:        https://github.com/lxgw/LxgwWenKai/releases/download/v%{version}/LXGWWenKaiMono-Light.ttf
Source7:        https://raw.githubusercontent.com/lxgw/LxgwWenKai/v%{version}/OFL.txt#/lxgw-wenkai-OFL.txt

BuildArch:      noarch

%description
LXGW WenKai (霞鹜文楷) is an open-source CJK font derived from
Fontworks Klee One, covering GB 2312 / Big5 / CNS 11643 / JIS X 0208
character sets. This package ships Regular, Medium and Light
weights in both proportional and monospace families.

%prep
cp %{SOURCE7} lxgw-wenkai-OFL.txt

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/lxgw-wenkai
install -m 644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{buildroot}%{_datadir}/fonts/lxgw-wenkai/

%files
%license lxgw-wenkai-OFL.txt
%{_datadir}/fonts/lxgw-wenkai/

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 1.522-1
- Initial package (6 TTFs: 3 weights x proportional/mono)
