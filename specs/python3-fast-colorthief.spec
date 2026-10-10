Name:           python3-fast-colorthief
Version:        0.0.5
Release:        8%{?dist}
Summary:        Dominant colors in image

License:        MIT
URL:            https://pypi.org/project/fast-colorthief/
Source0:        https://files.pythonhosted.org/packages/46/2b/9d4ae88af21fc22a87333632e9b26ec1ec711e0ed61ad48faeeff5068f76/fast-colorthief-0.0.5.tar.gz

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

# C extension, no debuginfo needed for pure-python wrapper
%global debug_package %{nil}

%description
fast-colorthief extracts dominant colors from images.
Required by kde-material-you-colors.

%prep
%autosetup -n fast-colorthief-%{version} -p1
# F45 的 CMake 移除了对 <3.5 的兼容，上游写死了老版本
find . -name CMakeLists.txt -exec sed -i "s/cmake_minimum_required(VERSION [0-9.]*)/cmake_minimum_required(VERSION 3.5)/" {} \;

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files fast_colorthief version fast_colorthief_backend

%files -f %{pyproject_files}

%changelog
* Sat Oct 10 2026 Maomaokuxs <biyuanh@qq.com> - 0.0.5-1
- Initial package (self-containment for kde-material-you-colors, was terra-provided)
