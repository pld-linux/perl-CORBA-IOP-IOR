%include	/usr/lib/rpm/macros.perl
%define		pdir	CORBA
%define		pnam	IOP-IOR
Summary:	CORBA::IOP::IOR - decode, munge, and re-encode CORBA IORs
Summary(pl):	CORBA::IOP::IOR - rozkodowanie, transformacja i ponowne zakodowanie 
Name:		perl-CORBA-IOP-IOR
Version:	0.1
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f023de34d86dee8b76eff1785910e27b
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CORBA::IOP::IOR is Perl module that decodes, munges, and re-encodes
CORBA IORs.

%description -l pl
CORBA::IOP::IOR jest modu³em Perla, który rozkodowuje, transformuje i
ponownie koduje IOR-y CORBA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/CORBA
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
