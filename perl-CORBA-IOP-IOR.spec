%include	/usr/lib/rpm/macros.perl
%define		pdir	CORBA
%define		pnam	IOP-IOR
Summary:	CORBA::IOP::IOR Perl module
Summary(cs):	Modul CORBA::IOP::IOR pro Perl
Summary(da):	Perlmodul CORBA::IOP::IOR
Summary(de):	CORBA::IOP::IOR Perl Modul
Summary(es):	Módulo de Perl CORBA::IOP::IOR
Summary(fr):	Module Perl CORBA::IOP::IOR
Summary(it):	Modulo di Perl CORBA::IOP::IOR
Summary(ja):	CORBA::IOP::IOR Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	CORBA::IOP::IOR ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul CORBA::IOP::IOR
Summary(pl):	Modu³ Perla CORBA::IOP::IOR
Summary(pt):	Módulo de Perl CORBA::IOP::IOR
Summary(pt_BR):	Módulo Perl CORBA::IOP::IOR
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl CORBA::IOP::IOR
Summary(sv):	CORBA::IOP::IOR Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl CORBA::IOP::IOR
Summary(zh_CN):	CORBA::IOP::IOR Perl Ä£¿é
Name:		perl-CORBA-IOP-IOR
Version:	0.1
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CORBA::IOP::IOR - Decode, munge, and re-encode CORBA IORs.

%description -l cs
Modul CORBA::IOP::IOR pro Perl.

%description -l da
Perlmodul CORBA::IOP::IOR.

%description -l de
CORBA::IOP::IOR Perl Modul.

%description -l es
Módulo de Perl CORBA::IOP::IOR.

%description -l fr
Module Perl CORBA::IOP::IOR.

%description -l it
Modulo di Perl CORBA::IOP::IOR.

%description -l ja
CORBA::IOP::IOR Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
CORBA::IOP::IOR ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul CORBA::IOP::IOR.

%description -l pl
Modu³ perla CORBA::IOP::IOR

%description -l pt
Módulo de Perl CORBA::IOP::IOR.

%description -l pt_BR
Módulo Perl CORBA::IOP::IOR.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl CORBA::IOP::IOR.

%description -l sv
CORBA::IOP::IOR Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl CORBA::IOP::IOR.

%description -l zh_CN
CORBA::IOP::IOR Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/CORBA
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
