Name:           python3-screeninfo
Version:        0.8.1
Release:        1%{?dist}
Summary:        Fetch location and size of physical screens

License:        MIT
URL:            https://github.com/rr-/screeninfo
Source0:        https://files.pythonhosted.org/packages/ec/bb/e69e5e628d43f118e0af4fc063c20058faa8635c95a1296764acc8167e27/screeninfo-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core

%description
Screeninfo fetches the location and size of physical screens,
a helper dependency for wallpaper and display tooling.

%prep
%autosetup -n screeninfo-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE.md
%{python3_sitelib}/screeninfo/
%{python3_sitelib}/screeninfo-%{version}*.dist-info/

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 0.8.1-1
- Initial package (clone terra's package into biyuan/software)
