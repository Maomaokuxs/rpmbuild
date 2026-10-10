Name:           python3-pywal16
Version:        3.8.15
Release:        1%{?dist}
Summary:        Generate and change color-schemes on the fly

License:        MIT
URL:            https://pypi.org/project/pywal16/
Source0:        https://files.pythonhosted.org/packages/5c/20/051723abec22086f7d808064a148568880878f251a6edeff0e46dfe785c7/pywal16-3.8.15.tar.gz

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
pywal16 generates color schemes from images and applies them
on the fly. Required by kde-material-you-colors.

%prep
%autosetup -n pywal16-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pywal

%files -f %{pyproject_files}
%license LICENSE.md
%{_bindir}/wal

%changelog
* Sat Oct 10 2026 Maomaokuxs <biyuanh@qq.com> - 3.8.15-1
- Initial package (self-containment for kde-material-you-colors, was terra-provided)
