%define module  NKF
%define upstream_version     207

Name:       perl-%{module}
Version:    %perl_convert_version %{upstream_version}
Release:    4
Summary:    Perl extension for Network Kanji Filter
License:    BSD-like
Group:      System/Internationalization
URL:        https://sourceforge.jp/projects/nkf
Source0:    http://prdownloads.sourceforge.jp/nkf/20770/nkf%{upstream_version}.tar.bz2
BuildRequires:  perl-devel

%description
This is a Perl Extension version of nkf (Netowrk Kanji Filter).
It converts the last argument and return converted result. Conversion
details are specified by flags before the last argument.

%prep
%setup -q -n nkf%{upstream_version}/NKF.mod

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make  CFLAGS='%{optflags} -fPIC'

%install
%makeinstall_std

%files
%{perl_vendorarch}/NKF.pm
%{perl_vendorarch}/auto/NKF
%{_mandir}/man3/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0.7-8mdv2012.0
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.0.7-7mdv2011.0
+ Revision: 556065
- rebuild for perl 5.12

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.0.7-6mdv2010.0
+ Revision: 430516
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.0.7-5mdv2009.0
+ Revision: 258140
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0.7-4mdv2009.0
+ Revision: 246221
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.0.7-2mdv2008.1
+ Revision: 152230
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 2.0.7-1mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.7-1mdv2007.0
+ Revision: 134334
- add URL
- new version

* Wed Feb 08 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.71-8mdk
- drop translated stuff in spec file (per policy)
- fix conflict with nkf (#18901)

* Sat Feb 05 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.71-7mdk
- rebuild for new perl

