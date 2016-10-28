Name:           frobtads
Version:        1.2.3
Release:        2%{?dist}
Summary:        Text interpreter for Tads games

License:        non-commercial
URL:            http://www.tads.org/frobtads.htm
Source0:        http://www.tads.org/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libcurl-devel
BuildRequires:  ncurses-devel
Provides:       bundled(md5-deutsch-c++)
Provides:       bundled(sha2-gladman)
Provides:       bundled(tads2) = 2.5.17
Provides:       bundled(tads3) = 3.1.3

%description
TADS stands for "Text Adventure Development System". It's a set of
tools that allow easy implementation of text adventures, or "Interactive
Fiction". The tools include a compiler along with supporting libraries,
a debugger and an interpreter. An interpreter is needed to run the
compiler's output, as it generates "byte code" programs (much like
Java).


%package devel
Summary:        Tads Compilers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
TADS stands for "Text Adventure Development System". It's a set of
tools that allow easy implementation of text adventures, or "Interactive
Fiction". The tools include a compiler along with supporting libraries,
a debugger and an interpreter. An interpreter is needed to run the
compiler's output, as it generates "byte code" programs (much like
Java).

This package contains Tads 2 and Tads 3 compilers.


%prep
%setup -q


%build
CXXFLAGS=-fpermissive \
%configure
make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_pkgdocdir}-devel
rm -rf %{buildroot}%{_datadir}/frobtads/tads3/doc


%files
%doc doc/AUTHORS doc/BUGS doc/NEWS doc/README doc/THANKS
%license doc/COPYING tads3/LICENSE.TXT
%dir %{_datadir}/frobtads/
%dir %{_datadir}/frobtads/tads3/
%{_bindir}/frob
%{_datadir}/frobtads/tads3/res/

%files devel
%doc doc/COMPILERS tads3/doc/*
%{_bindir}/tadsc
%{_bindir}/t3make
%{_datadir}/frobtads/tads2/
%{_datadir}/frobtads/tads3/include/
%{_datadir}/frobtads/tads3/lib/


%changelog
* Fri Oct 28 2016 František Dvořák <valtri@civ.zcu.cz> - 1.2.3-2
- Add build flags needed for ix86 and arm platforms

* Mon Dec 28 2015 František Dvořák <valtri@civ.zcu.cz> - 1.2.3-1
- Initial package
