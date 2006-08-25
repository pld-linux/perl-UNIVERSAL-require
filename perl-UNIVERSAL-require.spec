#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	UNIVERSAL
%define	pnam	require
Summary:	UNIVERSAL::require - require() modules from a variable
Summary(pl):	UNIVERSAL::require - wymaganie modu��w ze zmiennej
Name:		perl-UNIVERSAL-require
Version:	0.10
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4ea51136ee7052bb37dc52c7cb8945b0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Conflicts:	perl-UNIVERSAL-exports < 0.03-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you've ever had to do this...

eval "require $module";

to get around the bareword caveats on require(), this module is for
you. It creates a universal require() class method that will work with
every Perl module and it's secure. So instead of doing some arcane
eval() work, you can do this:

$module->require;

%description -l pl
Je�li kiedykolwiek by�o nam potrzebne...

eval "require $module";

do obej�cia przeciwno�ci require(), ten modu� jest dla nas. Tworzy
uniwersaln� metod� klasy require() dzia�aj�c� z ka�dym modu�em Perla,
a jednocze�nie bezpieczn�. Czyli zamiast wykonywania jakich� tajemnych
dzia�a� z eval(), mo�na zrobi�:

$module->require;

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
%doc Changes
%{perl_vendorlib}/UNIVERSAL/*.pm
%{_mandir}/man3/*
