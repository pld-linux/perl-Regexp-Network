%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Network
Summary:	Regexp::Network perl module - useful routines for DHCP
Summary(pl):	Modu³ perla Regexp::Network - procedury przydatne do DHCP
Name:		perl-Regexp-Network
Version:	1.3
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Memoize >= 1.00
BuildRequires:	perl-Module-Info >= 0.12
BuildRequires:	perl-Test-Simple >= 0.42
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Network module provides useful routines and constants and
stuff for analysing assorted network log files and data.

%description -l pl
Modu³ Regexp::Network udostêpnia procedury, sta³e itp. przydatne do
analizy logów i danych zwi±zanych z sieci±.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Regexp/Network.pm
%{_mandir}/man3/*
