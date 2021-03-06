%define		pdir	CORBA
%define		pnam	IOP-IOR
Summary:	CORBA::IOP::IOR - decode, munge, and re-encode CORBA IORs
Summary(pl.UTF-8):	CORBA::IOP::IOR - rozkodowanie, transformacja i ponowne zakodowanie
Name:		perl-CORBA-IOP-IOR
Version:	0.1
Release:	12
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f023de34d86dee8b76eff1785910e27b
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/CORBA-IOP-IOR/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CORBA::IOP::IOR is Perl module that decodes, munges, and re-encodes
CORBA IORs.

%description -l pl.UTF-8
CORBA::IOP::IOR jest modułem Perla, który rozkodowuje, transformuje i
ponownie koduje IOR-y CORBA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/CORBA
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
