Name:           frobtads
Version:        1.2.3
Release:        20%{?dist}
Summary:        Text interpreter for Tads games

License:        non-commercial
URL:            http://www.tads.org/frobtads.htm
Source0:        http://www.tads.org/%{name}/%{name}-%{version}.tar.gz
Patch1:         frobtads-1.2.3-gcc10-fix.patch
Patch2:         frobtads-1.2.3-gcc11-fix.patch

BuildRequires:  gcc-c++
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
%autosetup -p1


%build
CXXFLAGS="-fpermissive %optflags"
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
* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 06 2021 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.3-14
- Fix FTBFS

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.3-11
- Fix FTBFS

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-7
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 28 2016 František Dvořák <valtri@civ.zcu.cz> - 1.2.3-2
- Add build flags needed for ix86 and arm platforms

* Mon Dec 28 2015 František Dvořák <valtri@civ.zcu.cz> - 1.2.3-1
- Initial package
