#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-cmt-cat
Version  : 3.0.1
Release  : 14
URL      : https://github.com/intel/intel-cmt-cat/archive/v3.0.1.tar.gz
Source0  : https://github.com/intel/intel-cmt-cat/archive/v3.0.1.tar.gz
Summary  : Provides command line interface to CMT, MBM, CAT, CDP and MBA technologies
Group    : Development/Tools
License  : BSD-3-Clause
Requires: intel-cmt-cat-bin = %{version}-%{release}
Requires: intel-cmt-cat-lib = %{version}-%{release}
Requires: intel-cmt-cat-license = %{version}-%{release}
Requires: intel-cmt-cat-man = %{version}-%{release}
BuildRequires : buildreq-cpan
Patch1: 0001-Don-t-set-cflags-in-embedded-application.patch
Patch2: 0002-Add-destdir-support.patch

%description
This software package provides basic support for
Cache Monitoring Technology (CMT), Memory Bandwidth Monitoring (MBM),
Cache Allocation Technology (CAT), Memory Bandwidth Allocation (MBA),
and Code Data Prioratization (CDP).

CMT, MBM, CAT and MBA are configured using Model Specific Registers (MSRs)
to measure last level cache occupancy, set up the class of service masks and
manage the association of the cores/logical threads to a class of service.
The software executes in user space, and access to the MSRs is
obtained through a standard Linux* interface. The virtual file system
provides an interface to read and write the MSR registers but
it requires root privileges.

%package bin
Summary: bin components for the intel-cmt-cat package.
Group: Binaries
Requires: intel-cmt-cat-license = %{version}-%{release}

%description bin
bin components for the intel-cmt-cat package.


%package dev
Summary: dev components for the intel-cmt-cat package.
Group: Development
Requires: intel-cmt-cat-lib = %{version}-%{release}
Requires: intel-cmt-cat-bin = %{version}-%{release}
Provides: intel-cmt-cat-devel = %{version}-%{release}
Requires: intel-cmt-cat = %{version}-%{release}

%description dev
dev components for the intel-cmt-cat package.


%package lib
Summary: lib components for the intel-cmt-cat package.
Group: Libraries
Requires: intel-cmt-cat-license = %{version}-%{release}

%description lib
lib components for the intel-cmt-cat package.


%package license
Summary: license components for the intel-cmt-cat package.
Group: Default

%description license
license components for the intel-cmt-cat package.


%package man
Summary: man components for the intel-cmt-cat package.
Group: Default

%description man
man components for the intel-cmt-cat package.


%prep
%setup -q -n intel-cmt-cat-3.0.1
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552574072
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1552574072
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-cmt-cat
cp LICENSE %{buildroot}/usr/share/package-licenses/intel-cmt-cat/LICENSE
%make_install DESTDIR=%{buildroot} PREFIX=/usr NOLDCONFIG=y LIB_INSTALL_DIR=%{buildroot}/usr/lib64 MAN_DIR=%{buildroot}/usr/share/man/man8

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pqos
/usr/bin/pqos-msr
/usr/bin/pqos-os
/usr/bin/rdtset

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libpqos.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpqos.so.3
/usr/lib64/libpqos.so.3.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-cmt-cat/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/pqos-msr.8
/usr/share/man/man8/pqos-os.8
/usr/share/man/man8/pqos.8
/usr/share/man/man8/rdtset.8
