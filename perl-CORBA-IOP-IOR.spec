%include	/usr/lib/rpm/macros.perl
Summary:	CORBA-IOP-IOR perl module
Summary(pl):	Modu³ perla CORBA-IOP-IOR
Name:		perl-CORBA-IOP-IOR
Version:	0.1
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CORBA/CORBA-IOP-IOR-%{version}.tar.gz
Patch:		perl-CORBA-IOP-IOR-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CORBA-IOP-IOR - Decode, munge, and re-encode CORBA IORs.

%description -l pl
Modu³ perla CORBA-IOP-IOR

%prep
%setup -q -n CORBA-IOP-IOR-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}
make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CORBA/IOP
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/CORBA/IOP
%{perl_sitearch}/auto/CORBA/IOP

%dir /usr/src/examples/%{name}-%{version}
%attr(755,root,root) /usr/src/examples/%{name}-%{version}/*
