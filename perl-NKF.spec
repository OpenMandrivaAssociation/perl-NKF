%define module  NKF
%define name    perl-%{module}
%define version 2.0.7
%define ver     207
%define release %mkrel 4

Name:       %name
Version:    %version
Release:    %release
Summary:    Perl extension for Network Kanji Filter
License:    BSD-like
Group:      System/Internationalization
URL:        http://sourceforge.jp/projects/nkf
Source0:    http://prdownloads.sourceforge.jp/nkf/20770/nkf%{ver}.tar.bz2
BuildRequires:  perl-devel
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
This is a Perl Extension version of nkf (Netowrk Kanji Filter ) %{version}
It converts the last argument and return converted result. Conversion
details are specified by flags before the last argument.

%prep
%setup -q -n nkf%{ver}/NKF.mod

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make  CFLAGS='%{optflags}'

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorarch}/NKF.pm
%{perl_vendorarch}/auto/NKF
%{_mandir}/man3/*


