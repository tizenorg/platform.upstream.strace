Name:           strace
BuildRequires:  libacl-devel
BuildRequires:  libaio-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  xz
Version:        4.7
Release:        0
License:        BSD-3-Clause
Summary:        A utility to trace the system calls of a program
Url:            http://sourceforge.net/projects/strace/
Group:          Development/Tools/Debuggers
Source:         http://dl.sourceforge.net/strace/strace-%{version}.tar.xz
Source2:        baselibs.conf

%description
With strace, you can trace the activity of a program.  Information
about any system calls the program makes and the signals it receives
and processes can be seen.  Child processes can also be tracked.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%configure 

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
%{_bindir}/strace
%{_bindir}/strace-graph
%{_bindir}/strace-log-merge
%doc %{_mandir}/man1/strace.1.gz

%changelog
