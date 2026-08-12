Name:           clipshare
Version:        1.4.4
Release:        1%{?dist}
Summary:        跨平台剪贴板共享工具

License:        MIT
URL:            https://github.com/aa2013/ClipShare

Source0:        https://github.com/aa2013/ClipShare/releases/download/v%{version}/clipshare-%{version}+26-linux.rpm

BuildArch:      x86_64

%description
ClipShare 是一款跨平台局域网剪贴板共享工具。

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
# 从 RPM 提取文件
rpm2cpio %{SOURCE0} | cpio -idmv 2>/dev/null
for d in opt usr; do
    [ -d "$d" ] && cp -a "$d"/* %{buildroot}/ 2>/dev/null
done

%files
/opt/clipshare/
/usr/share/applications/clipshare.desktop

%changelog
* Fri Jul 18 2025 Maomaokuxs <biyuanh@qq.com> - 1.4.4-1
- Initial packaging from upstream RPM
