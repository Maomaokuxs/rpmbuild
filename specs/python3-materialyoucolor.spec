Name:           python3-materialyoucolor
Version:        3.0.4
Release:        1%{?dist}
Summary:        Material You color generation in pure Python

License:        MIT
URL:            https://pypi.org/project/materialyoucolor/
Source0:        https://files.pythonhosted.org/packages/eb/23/2e63e7bdfcc1aa7ba955386ad09e3bd8a535a1092d7af501659b63cb6282/materialyoucolor-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

%description
Material You color generation algorithms in pure Python,
used by kde-material-you-colors to derive color schemes
from wallpapers.

%prep
%autosetup -n materialyoucolor-%{version} -p1

%build
# Upstream setup.py builds an optional C++ extension via pybind11;
# terra ships the pure-Python flavor, do the same.
export MYCP_PURE_PYTHON=1
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%{python3_sitelib}/materialyoucolor/
%{python3_sitelib}/materialyoucolor-%{version}*.dist-info/

%changelog
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 3.0.4-1
- Initial package (self-containment for kde-material-you-colors)
