#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: c1050fe
#
Name     : intel-cmt-cat
Version  : v23.11
Release  : 22
URL      : https://github.com/intel/intel-cmt-cat/archive/v23.11/intel-cmt-cat-v23.11.tar.gz
Source0  : https://github.com/intel/intel-cmt-cat/archive/v23.11/intel-cmt-cat-v23.11.tar.gz
Summary  : Provides command line interface to CMT, MBM, CAT, CDP and MBA technologies
Group    : Development/Tools
License  : BSD-3-Clause
Requires: intel-cmt-cat-bin = %{version}-%{release}
Requires: intel-cmt-cat-lib = %{version}-%{release}
Requires: intel-cmt-cat-license = %{version}-%{release}
Requires: intel-cmt-cat-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0002-Add-destdir-support.patch

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
%setup -q -n intel-cmt-cat-23.11
cd %{_builddir}/intel-cmt-cat-23.11
%patch -P 1 -p1
pushd ..
cp -a intel-cmt-cat-23.11 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701971885
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}

pushd ../buildavx2
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701971885
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-cmt-cat
cp %{_builddir}/intel-cmt-cat-23.11/LICENSE %{buildroot}/usr/share/package-licenses/intel-cmt-cat/a4a43e608149714ad15f92d9f363b39bf0ea8894 || :
cp %{_builddir}/intel-cmt-cat-23.11/appqos/LICENSE %{buildroot}/usr/share/package-licenses/intel-cmt-cat/ae790ed217e8133bdd20c1d2c3401a4b3a587220 || :
cp %{_builddir}/intel-cmt-cat-23.11/lib/python/LICENSE %{buildroot}/usr/share/package-licenses/intel-cmt-cat/ae790ed217e8133bdd20c1d2c3401a4b3a587220 || :
pushd ../buildavx2/
%make_install_v3 DESTDIR=%{buildroot} PREFIX=/usr NOLDCONFIG=y LIB_INSTALL_DIR=%{buildroot}/usr/lib64 MAN_DIR=%{buildroot}/usr/share/man/man8
popd
%make_install DESTDIR=%{buildroot} PREFIX=/usr NOLDCONFIG=y LIB_INSTALL_DIR=%{buildroot}/usr/lib64 MAN_DIR=%{buildroot}/usr/share/man/man8
## install_append content
#mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/membw
/usr/bin/pqos
/usr/bin/pqos-msr
/usr/bin/pqos-os
/usr/bin/rdtset

%files dev
%defattr(-,root,root,-)
/usr/include/pqos.h
/usr/lib64/libpqos.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpqos.so.5
/usr/lib64/libpqos.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-cmt-cat/a4a43e608149714ad15f92d9f363b39bf0ea8894
/usr/share/package-licenses/intel-cmt-cat/ae790ed217e8133bdd20c1d2c3401a4b3a587220

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/membw.8
/usr/share/man/man8/pqos-msr.8
/usr/share/man/man8/pqos-os.8
/usr/share/man/man8/pqos.8
/usr/share/man/man8/rdtset.8
