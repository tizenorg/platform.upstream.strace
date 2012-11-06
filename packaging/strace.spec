#
# spec file for package strace
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           strace
BuildRequires:  libacl-devel
BuildRequires:  libaio-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  xz
# bug437293
%ifarch ppc64
Obsoletes:      strace-64bit
%endif
#
Version:        4.7
Release:        0
License:        BSD-3-Clause
Summary:        A utility to trace the system calls of a program
Url:            http://sourceforge.net/projects/strace/
Group:          Development/Tools/Debuggers
Source:         http://dl.sourceforge.net/strace/strace-%{version}.tar.xz
Source2:        baselibs.conf
Patch0:         strace-%{version}.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
With strace, you can trace the activity of a program.  Information
about any system calls the program makes and the signals it receives
and processes can be seen.  Child processes can also be tracked.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%ifarch alpha
CFLAGS="$CFLAGS -ffixed-8"
%endif
%configure \
%ifarch %sparc
	--host=%_target_platform
%endif

make %{?_smp_mflags}

# Have to exclude make check for qemu builds, which apparently don't support PTRACE.
%if !(0%{?qemu_user_space_build})
%check
make check
%endif

%install
%make_install

%files
%defattr(-,root,root)
%doc README README-linux NEWS
%{_bindir}/strace
%{_bindir}/strace-graph
%{_bindir}/strace-log-merge
%doc %{_mandir}/man1/strace.1.gz

%changelog
