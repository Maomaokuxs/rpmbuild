Name:           grub-btrfs
Version:        4.14
Release:        1%{?dist}
Summary:        Include Btrfs snapshots in GRUB boot menu

License:        GPL-3.0
URL:            https://github.com/Antynea/grub-btrfs
Source0:        https://github.com/Antynea/grub-btrfs/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       grub2
Requires:       btrfs-progs

%description
grub-btrfs adds Btrfs snapshots to the GRUB boot menu,
allowing you to boot directly into a previous snapshot.

%prep
%setup -q

%build

%install
# 主脚本放到 grub.d，grub2-mkconfig 从这里加载
mkdir -p %{buildroot}%{_sysconfdir}/grub.d
install -m 755 41_snapshots-btrfs %{buildroot}%{_sysconfdir}/grub.d/

# 守护进程和数据文件
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/grub-btrfs
mkdir -p %{buildroot}%{_unitdir}
install -m 755 grub-btrfsd %{buildroot}%{_bindir}/
# config 可能是目录或文件
if [ -d config ]; then
    mkdir -p %{buildroot}%{_sysconfdir}/default/grub-btrfs
    cp -r config/* %{buildroot}%{_sysconfdir}/default/grub-btrfs/
else
    mkdir -p %{buildroot}%{_sysconfdir}/default/grub-btrfs
    install -m 644 config %{buildroot}%{_sysconfdir}/default/grub-btrfs/config
fi
cp grub-btrfsd.service %{buildroot}%{_unitdir}/

# 加入 Fedora 发行版自动检测块
sed -i '2i\
# Fedora auto-detection\
if [ -f /etc/fedora-release ]; then\
    GRUB_BTRFS_GRUB_DIRNAME="/boot/grub2"\
    GRUB_BTRFS_GBTRFS_DIRNAME="/boot/grub2"\
    GRUB_BTRFS_MKCONFIG="/usr/bin/grub2-mkconfig"\
    GRUB_BTRFS_SCRIPT_CHECK="grub2-script-check"\
fi\
' %{buildroot}%{_sysconfdir}/default/grub-btrfs/config

# 限制快照条目数量
if ! grep -q '^GRUB_BTRFS_LIMIT=' %{buildroot}%{_sysconfdir}/default/grub-btrfs/config 2>/dev/null; then
    echo 'GRUB_BTRFS_LIMIT=10' >> %{buildroot}%{_sysconfdir}/default/grub-btrfs/config
fi

%post
%systemd_post grub-btrfsd.service

%preun
%systemd_preun grub-btrfsd.service

%postun
%systemd_postun_with_restart grub-btrfsd.service

%files
%{_sysconfdir}/grub.d/41_snapshots-btrfs
%{_bindir}/grub-btrfsd
%{_sysconfdir}/default/grub-btrfs/
%{_unitdir}/grub-btrfsd.service
%{_datadir}/grub-btrfs/
%doc README.md

%changelog
* Thu Jul 10 2025 Maomaokuxs <biyuanh@qq.com> - 4.14-1
- Install 41_snapshots-btrfs to /etc/grub.d/
- Enable Fedora defaults in config
- Set GRUB_BTRFS_LIMIT=10
- Use upstream source without patches
