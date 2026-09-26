Name:           python3-imageio-ffmpeg
Version:        0.6.0
Release:        1%{?dist}
Summary:        FFMPEG wrapper for Python (with bundled static binary)

License:        BSD-2-Clause
URL:            https://github.com/imageio/imageio-ffmpeg
Source0:        https://files.pythonhosted.org/packages/a0/2d/43c8522a2038e9d0e7dbdf3a61195ecc31ca576fb1527a528c877e87d973/imageio_ffmpeg-%{version}-py3-none-manylinux2014_x86_64.whl

BuildRequires:  python3-devel
BuildRequires:  python3
BuildRequires:  unzip

# NOTE: no BuildArch/ExclusiveArch on purpose — rpkg preprocess_spec
# fails with "No compatible architectures" when both are set (same
# convention as miyu/flclash/mcloud repacks; builder is x86_64 anyway).

%description
imageio-ffmpeg is a Python wrapper for FFmpeg, shipping a static
ffmpeg binary so no system FFmpeg is needed. Required by waypaper
for video wallpaper support.

%prep
%setup -q -c -n %{name}-%{version} -T
unzip -q -o %{SOURCE0}

%build

%install
sitelib=$(python3 -c "import sysconfig; print(sysconfig.get_path('purelib'))")
mkdir -p %{buildroot}$sitelib
cp -a imageio_ffmpeg %{buildroot}$sitelib/
mkdir -p %{buildroot}$sitelib/imageio_ffmpeg-%{version}.dist-info
cp -a imageio_ffmpeg-%{version}.dist-info/{METADATA,WHEEL,top_level.txt,LICENSE} \
    %{buildroot}$sitelib/imageio_ffmpeg-%{version}.dist-info/
chmod +x %{buildroot}$sitelib/imageio_ffmpeg/binaries/ffmpeg-linux-*

%files
%license imageio_ffmpeg-%{version}.dist-info/LICENSE
%{python3_sitelib}/imageio_ffmpeg/
%{python3_sitelib}/imageio_ffmpeg-%{version}.dist-info/

%changelog
* Sat Sep 26 2026 Maomaokuxs <biyuanh@qq.com> - 0.6.0-1
- Initial package (wheel repack, ffmpeg binary for waypaper video wallpapers)
