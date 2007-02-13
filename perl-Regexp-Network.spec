#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Regexp
%define		pnam	Network
Summary:	Regexp::Network Perl module - useful routines for DHCP
Summary(pl.UTF-8):	Moduł Perla Regexp::Network - procedury przydatne do DHCP
Name:		perl-Regexp-Network
Version:	1.3
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ebba2ba5916a061507bcdc72c95f3a4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Memoize >= 1.00
BuildRequires:	perl-Module-Info >= 0.12
BuildRequires:	perl-Test-Simple >= 0.42
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Network module provides useful routines and constants and
stuff for analysing assorted network log files and data.

%description -l pl.UTF-8
Moduł Regexp::Network udostępnia procedury, stałe itp. przydatne do
analizy logów i danych związanych z siecią.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Regexp/Network.pm
%{_mandir}/man3/*
