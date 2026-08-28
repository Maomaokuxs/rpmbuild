Name:           miyu
Version:        0.4.5
Release:        1%{?dist}
Summary:        终端里的二次元 AI 助手

License:        MIT
URL:            https://github.com/SHORiN-KiWATA/Miyu

Source0:        https://github.com/SHORiN-KiWATA/Miyu/releases/download/v%{version}/miyu-%{version}-1-x86_64.pkg.tar.zst

%description
Miyu 是一个活在终端里的二次元少女 AI 助手，由大模型驱动。

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/miyu

# 解压 Arch 包，提取二进制和数据文件
tar xf %{SOURCE0} --zstd
install -m 755 usr/bin/miyu %{buildroot}%{_bindir}/miyu
cp -a usr/share/miyu/* %{buildroot}%{_datadir}/miyu/ 2>/dev/null || true

%files
%{_bindir}/miyu
%{_datadir}/miyu/

%changelog
* Thu Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 0.4.5-1
- Update to 0.4.5

* Sun Jul 26 2026 Maomaokuxs <biyuanh@qq.com> - 0.3.0-1
- Update to 0.3.0
