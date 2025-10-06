# Hyper-V KVP daemon binary name
%global hv_kvp_daemon hypervkvpd
# Hyper-V VSS daemon binary name
%global hv_vss_daemon hypervvssd
# Hyper-V FCOPY daemon binary name
%global hv_fcopy_uio_daemon hv_fcopy_uio_daemon
# snapshot version
%global snapver .20220731git
# use hardened build
%global _hardened_build 1
# udev rules prefix
%global udev_prefix 70

Name:     hyperv-daemons
Version:  0
Release:  0.49%{?snapver}%{?dist}
Summary:  Hyper-V daemons suite

License:  GPL-2.0-only
URL:      http://www.kernel.org

# Source files obtained from kernel upstream 4.17-rc1 (60cc43fc888428bb2f18f08997432d426a243338)
# git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
Source0:  COPYING

# HYPERV KVP DAEMON
Source1:  hv_kvp_daemon.c
Source2:  hv_get_dhcp_info.sh
Source3:  hv_get_dns_info.sh
Source4:  hv_set_ifconfig.sh
Source5:  hypervkvpd.service
Source6:  hypervkvp.rules

# HYPERV VSS DAEMON
Source100:  hv_vss_daemon.c
Source101:  hypervvssd.service
Source102:  hypervvss.rules

# HYPERV FCOPY UIO DAEMON
# source taken from https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/snapshot/linux-6.10-rc5.tar.gz
Source200:  hv_fcopy_uio_daemon.c
Source201:  hypervfcopyd.service
Source202:  vmbus_bufring.c
Source203:  vmbus_bufring.h
# HYPERV TOOLS
Source301:  lsvmbus

# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch1: hpvd-Do-not-set-NM_CONTROLLED-no.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch2: hpvd-Add-vmbus_testing-tool-build-files.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch3: hpvd-hv_set_ifconfig.sh-Use-nmcli-commands.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch4: hpvd-Use-filename-for-connection-profile.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch5: hpvd-redhat-hv_set_if_config-Workaround-for-gateway-numbe.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch6: hpvd-tools-hv-Remove-an-extraneous-the.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch7: hpvd-tools-hv-kvp-remove-unnecessary-void-conversions.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch8: hpvd-vmbus_testing-fix-wrong-python-syntax-for-integer-va.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch9: hpvd-hv-hv_kvp_daemon-Support-for-keyfile-based-connectio.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch10: hpvd-hv-hv_kvp_daemon-Some-small-fixes-for-handling-NM-ke.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch11: hpvd-hv-hv_kvp_daemon-Handle-IPv4-and-Ipv6-combination-fo.patch
# For RHEL-40107 - [Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.
# For RHEL-40679 - [Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5
Patch12: hpvd-Changes-for-adding-keyfile-support-in-RHEL-specific-.patch
# For RHEL-65434 - [Hyper-V][RHEL-10]KVP daemon inspects /etc/sysconfig/network-scripts/ifcfg-* files to get DHCP information
Patch13: hpvd-Use-NetworkManager-information-to-report-DHCP-settin.patch
# For RHEL-65434 - [Hyper-V][RHEL-10]KVP daemon inspects /etc/sysconfig/network-scripts/ifcfg-* files to get DHCP information
Patch14: hpvd-Use-NetworkManager-information-to-report-DNS-setting.patch

# Hyper-V is available only on x86 and aarch64 architectures
# The base empty (a.k.a. virtual) package can not be noarch
# due to http://www.rpm.org/ticket/78
ExclusiveArch:  i686 x86_64 aarch64

Requires:       hypervkvpd = %{version}-%{release}
Requires:       hypervvssd = %{version}-%{release}

# FCopy UIO driver does not seem to be supported on arm
%ifnarch aarch64
Requires:       hypervfcopyd = %{version}-%{release}
%else
Obsoletes:      hypervfcopyd <= %{version}-%{release}
%endif
BuildRequires:  gcc

%description
Suite of daemons that are needed when Linux guest
is running on Windows Host with Hyper-V.


%package -n hypervkvpd
Summary: Hyper-V key value pair (KVP) daemon
Requires: %{name}-license = %{version}-%{release}
BuildRequires: systemd, kernel-headers
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description -n hypervkvpd
Hypervkvpd is an implementation of Hyper-V key value pair (KVP)
functionality for Linux. The daemon first registers with the
kernel driver. After this is done it collects information
requested by Windows Host about the Linux Guest. It also supports
IP injection functionality on the Guest.


%package -n hypervvssd
Summary: Hyper-V VSS daemon
Requires: %{name}-license = %{version}-%{release}
BuildRequires: systemd, kernel-headers
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description -n hypervvssd
Hypervvssd is an implementation of Hyper-V VSS functionality
for Linux. The daemon is used for host initiated guest snapshot
on Hyper-V hypervisor. The daemon first registers with the
kernel driver. After this is done it waits for instructions
from Windows Host if to "freeze" or "thaw" the filesystem
on the Linux Guest.

%ifnarch aarch64
# FCOPY UIO driver does not seem to be saupported on arm etc.
%package -n hypervfcopyd
Summary: Hyper-V FCOPY UIO daemon
Requires: %{name}-license = %{version}-%{release}
BuildRequires: systemd, kernel-headers
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description -n hypervfcopyd
Hypervfcopyd is an implementation of file copy service functionality
for Linux Guest running on Hyper-V. The daemon enables host to copy
a file (over VMBUS) into the Linux Guest. The daemon first registers
with the kernel driver. After this is done it waits for instructions
from Windows Host.
%endif

%package license
Summary:    License of the Hyper-V daemons suite
BuildArch:  noarch

%description license
Contains license of the Hyper-V daemons suite.

%package -n hyperv-tools
Summary:    Tools for Hyper-V guests
BuildArch:  noarch

%description -n hyperv-tools
Contains tools and scripts useful for Hyper-V guests.

%prep
%setup -Tc
cp -pvL %{SOURCE0} COPYING

cp -pvL %{SOURCE1} hv_kvp_daemon.c
cp -pvL %{SOURCE2} hv_get_dhcp_info.sh
cp -pvL %{SOURCE3} hv_get_dns_info.sh
cp -pvL %{SOURCE4} hv_set_ifconfig.sh
cp -pvL %{SOURCE100} hv_vss_daemon.c

%ifnarch aarch64
cp -pvL %{SOURCE200} hv_fcopy_uio_daemon.c
cp -pvL %{SOURCE202} vmbus_bufring.c
cp -pvL %{SOURCE203} vmbus_bufring.h
%endif
cp -pvL %{SOURCE301} lsvmbus

%autopatch -p1

%build
# HYPERV KVP DAEMON
%{__cc} $RPM_OPT_FLAGS -c hv_kvp_daemon.c
%{__cc} $RPM_LD_FLAGS  hv_kvp_daemon.o -o %{hv_kvp_daemon}

# HYPERV VSS DAEMON
%{__cc} $RPM_OPT_FLAGS -c hv_vss_daemon.c
%{__cc} $RPM_LD_FLAGS hv_vss_daemon.o -o %{hv_vss_daemon}


%ifnarch aarch64
# HYPERV FCOPY UIO DAEMON
%{__cc} $RPM_OPT_FLAGS -c hv_fcopy_uio_daemon.c
%{__cc} $RPM_OPT_FLAGS -c vmbus_bufring.c
%{__cc} $RPM_LD_FLAGS vmbus_bufring.o hv_fcopy_uio_daemon.o -o %{hv_fcopy_uio_daemon}
%endif

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sbindir}
install -p -m 0755 %{hv_kvp_daemon} %{buildroot}%{_sbindir}
install -p -m 0755 %{hv_vss_daemon} %{buildroot}%{_sbindir}

%ifnarch aarch64
install -p -m 0755 %{hv_fcopy_uio_daemon} %{buildroot}%{_sbindir}
%endif

# Systemd unit file
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE101} %{buildroot}%{_unitdir}
%ifnarch aarch64
install -p -m 0644 %{SOURCE201} %{buildroot}%{_unitdir}
%endif
# Udev rules
mkdir -p %{buildroot}%{_udevrulesdir}
install -p -m 0644 %{SOURCE6} %{buildroot}%{_udevrulesdir}/%{udev_prefix}-hypervkvp.rules
install -p -m 0644 %{SOURCE102} %{buildroot}%{_udevrulesdir}/%{udev_prefix}-hypervvss.rules
# Shell scripts for the KVP daemon
mkdir -p %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}
install -p -m 0755 hv_get_dhcp_info.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_get_dhcp_info
install -p -m 0755 hv_get_dns_info.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_get_dns_info
install -p -m 0755 hv_set_ifconfig.sh %{buildroot}%{_libexecdir}/%{hv_kvp_daemon}/hv_set_ifconfig
# Directory for pool files
mkdir -p %{buildroot}%{_sharedstatedir}/hyperv

# Tools
install -p -m 0755 lsvmbus %{buildroot}%{_sbindir}/
sed -i 's,#!/usr/bin/env python,#!/usr/bin/python3,' %{buildroot}%{_sbindir}/lsvmbus
install -p -m 0755 vmbus_testing %{buildroot}%{_sbindir}/

%post -n hypervkvpd
if [ $1 -gt 1 ] ; then
	# Upgrade
	systemctl --no-reload disable hypervkvpd.service >/dev/null 2>&1 || :
fi

%preun -n hypervkvpd
%systemd_preun hypervkvpd.service

%postun -n hypervkvpd
# hypervkvpd daemon does NOT support restarting (driver, neither)
%systemd_postun hypervkvpd.service
# If removing the package, delete %%{_sharedstatedir}/hyperv directory
if [ "$1" -eq "0" ] ; then
    rm -rf %{_sharedstatedir}/hyperv || :
fi


%post -n hypervvssd
if [ $1 -gt 1 ] ; then
	# Upgrade
	systemctl --no-reload disable hypervvssd.service >/dev/null 2>&1 || :
fi

%postun -n hypervvssd
%systemd_postun hypervvssd.service

%preun -n hypervvssd
%systemd_preun hypervvssd.service

%ifnarch aarch64
%post -n hypervfcopyd
if [ $1 -gt 1 ] ; then
	# Upgrade
	systemctl --no-reload disable hypervfcopyd.service >/dev/null 2>&1 || :
fi

%postun -n hypervfcopyd
%systemd_postun hypervfcopyd.service

%preun -n hypervfcopyd
%systemd_preun hypervfcopyd.service
%endif

%files
# the base package does not contain any files.

%files -n hypervkvpd
%{_sbindir}/%{hv_kvp_daemon}
%{_unitdir}/hypervkvpd.service
%{_udevrulesdir}/%{udev_prefix}-hypervkvp.rules
%dir %{_libexecdir}/%{hv_kvp_daemon}
%{_libexecdir}/%{hv_kvp_daemon}/*
%dir %{_sharedstatedir}/hyperv

%files -n hypervvssd
%{_sbindir}/%{hv_vss_daemon}
%{_unitdir}/hypervvssd.service
%{_udevrulesdir}/%{udev_prefix}-hypervvss.rules

%ifnarch aarch64
%files -n hypervfcopyd
%{_sbindir}/%{hv_fcopy_uio_daemon}
%{_unitdir}/hypervfcopyd.service
%endif

%files license
%doc COPYING

%files -n hyperv-tools
%{_sbindir}/lsvmbus
%{_sbindir}/vmbus_testing

%changelog
* Thu Nov 21 2024 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.49.20220731git
- hpvd-Use-NetworkManager-information-to-report-DHCP-settin.patch [RHEL-65434]
- hpvd-Use-NetworkManager-information-to-report-DNS-setting.patch [RHEL-65434]
- Resolves: RHEL-65434
  ([Hyper-V][RHEL-10]KVP daemon inspects /etc/sysconfig/network-scripts/ifcfg-* files to get DHCP information)

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 0-0.48.20220731git
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Fri Jul 12 2024 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.47.20220731git
- hpvd-Add-support-for-newer-fcopy-UIO-hyperv-daemons-modul.patch [RHEL-44617]
- hpvd-Update-main-package-dep-on-hypervfcopyd-to-be-arch-d.patch [RHEL-44617]
- hpvd-Particularize-hypervfcopyd-service-requirements.patch [RHEL-44617]
- Resolves: RHEL-44617
  ([RHEL-10] Add support for fcopy UIO userland module in hyperv-daemons)

* Thu Jun 27 2024 Miroslav Rezanina <mrezanin@redhat.com> - 0-0.46.20220731git
- hpvd-Add-support-for-patching-hyperv-daemons.patch [RHEL-40107 RHEL-40679]
- hpvd-Do-not-set-NM_CONTROLLED-no.patch [RHEL-40107 RHEL-40679]
- hpvd-Add-vmbus_testing-tool-build-files.patch [RHEL-40107 RHEL-40679]
- hpvd-hv_set_ifconfig.sh-Use-nmcli-commands.patch [RHEL-40107 RHEL-40679]
- hpvd-Use-filename-for-connection-profile.patch [RHEL-40107 RHEL-40679]
- hpvd-redhat-hv_set_if_config-Workaround-for-gateway-numbe.patch [RHEL-40107 RHEL-40679]
- hpvd-tools-hv-Remove-an-extraneous-the.patch [RHEL-40107 RHEL-40679]
- hpvd-tools-hv-kvp-remove-unnecessary-void-conversions.patch [RHEL-40107 RHEL-40679]
- hpvd-vmbus_testing-fix-wrong-python-syntax-for-integer-va.patch [RHEL-40107 RHEL-40679]
- hpvd-hv-hv_kvp_daemon-Support-for-keyfile-based-connectio.patch [RHEL-40107 RHEL-40679]
- hpvd-hv-hv_kvp_daemon-Some-small-fixes-for-handling-NM-ke.patch [RHEL-40107 RHEL-40679]
- hpvd-hv-hv_kvp_daemon-Handle-IPv4-and-Ipv6-combination-fo.patch [RHEL-40107 RHEL-40679]
- hpvd-Changes-for-adding-keyfile-support-in-RHEL-specific-.patch [RHEL-40107 RHEL-40679]
- hpvd-Remove-hyperv_fcopy_daemon-as-the-c10s-kernel-does-n.patch [RHEL-40107 RHEL-40679]
- Resolves: RHEL-40107
  ([Hyper-V][RHEL10] Request to update hypervkvpd related file /usr/libexec/hypervkvpd/hv_set_ifconfig same as RHEL 9.5 hv_set_ifconfig file.)
- Resolves: RHEL-40679
  ([Hyper-V][RHEL10] Request to update hyperv-daemons vmbus_testing, hv_kvp_daemon.c, hv_vss_daemon.c files as same as RHEL 9.5)

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 0-0.45.20220731git
- Bump release for June 2024 mass rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.44.20220731git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.43.20220731git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.42.20220731git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.41.20220731git
- Switch to SPDX identifiers for the license field

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.40.20220731git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.39.20220731git
- Enable aarch64 build (#2111394)
- Fix typos in shell scripts

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.38.20220710git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.37.20220710git
- Update to 5.19-rc6

* Fri Jul 01 2022 Chris Patterson <cpatterson@microsoft.com> - 0-0.37.20190303git
- Only start kvpd under Hyper-V
- Minimize dependencies for kvpd to ensure it starts before cloud-init

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.36.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.35.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.34.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.33.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.32.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Tom Stellard <tstellar@redhat.com> - 0-0.31.20190303git
- Use __cc macro instead of hard-coding gcc

* Fri Nov 08 2019 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.30.20190303git
- Rebase to 5.4-rc6
- Add IgnoreOnIsolate to systemd units

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.29.20190303git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.28.20190303git
- Rebase to 5.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.27.20180415git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.20180415git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.25.20180415git
- Switch lsvmbus to Python3

* Thu Apr 26 2018 Tomas Hozza <thozza@redhat.com> - 0-0.24.20180415git
- Added gcc as an explicit BuildRequires

* Thu Apr 19 2018 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.23.20180415git
- Rebase to 4.17-rc1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20170105git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.21.20170105git
- Rebase to 4.15-rc2, drop fedora patches as changes are upstream
- Start kvpd after network.target

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20170105git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20170105git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20170105git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.17.20160728git
- Use '-gt' instead of '>' to do the right comparison (#1412033)

* Thu Jan 05 2017 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.16.20160728git
- Rebase to 4.9
- hyperv-tools subpackage added

* Thu Jul 28 2016 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.15.20160728git
- Rebase to 4.8-rc0 (20160728 git snapshot)
- Disable services and remove ConditionVirtualization, multi-user.target
  dependencies switching to udev-only activation (#1331577)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20150702git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.13.20150702git
- Add udev rules to properly restart services (#1195029)
- Spec cleanup

* Thu Jul 02 2015 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.12.20150702git
- Rebase to 4.2-rc0 (20150702 git snapshot)
- Switch to new chardev-based communication layer (#1195029)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.11.20150108git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 08 2015 Vitaly Kuznetsov <vkuznets@redhat.com> - 0-0.10.20150108git
- Rebase to 3.19-rc3 (20150108 git snapshot)
- Drop 'nodaemon' patches, use newly introduced '-n' option

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.20140714git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Tomas Hozza <thozza@redhat.com> - 0-0.8.20140714git
- Update the File copy daemon to the latest git snapshot
- Fix hyperfcopyd.service to check for /dev/vmbus/hv_fcopy

* Wed Jun 11 2014 Tomas Hozza <thozza@redhat.com> - 0-0.7.20140611git
- Fix FTBFS (#1106781)
- Use kernel-headers instead of kernel-devel for building
- package new Hyper-V fcopy daemon as hypervfcopyd sub-package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20140219git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Tomas Hozza <thozza@redhat.com> - 0-0.5.20140219git
- rebase to the latest git snapshot next-20140219
  - KVP, VSS: removed inclusion of linux/types.h
  - VSS: Ignore VFAT mounts during freeze operation

* Fri Jan 10 2014 Tomas Hozza <thozza@redhat.com> - 0-0.4.20131022git
- provide 'hyperv-daemons' package for convenient installation of all daemons

* Tue Oct 22 2013 Tomas Hozza <thozza@redhat.com> - 0-0.3.20131022git
- rebase to the latest git snapshot next-20130927 (obtained 2013-10-22)
  - KVP, VSS: daemon use single buffer for send/recv
  - KVP: FQDN is obtained on start and cached

* Fri Sep 20 2013 Tomas Hozza <thozza@redhat.com> - 0-0.2.20130826git
- Use 'hypervkvpd' directory in libexec for KVP daemon scripts (#1010268)
- daemons are now WantedBy multi-user.target instead of basic.target (#1010260)

* Mon Aug 26 2013 Tomas Hozza <thozza@redhat.com> - 0-0.1.20130826git
- Initial package
