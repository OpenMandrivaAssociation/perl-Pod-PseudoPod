%define module	Pod-PseudoPod
%define name	perl-%{module}
%define version 0.15
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A framework for parsing O'Reilly's PseudoPod
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AR/ARANDAL/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl-Pod-Simple
BuildRequires:  perl-HTML-Parser

%description
PseudoPod is an extended set of Pod tags used by O'Reilly and Associates
publishing for book manuscripts. Standard Pod doesn't have all the markup
options you need to mark up files for publishing production. PseudoPod adds a
few extra tags for footnotes, tables, sidebars, etc.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Pod/PseudoPod.pm
%{perl_vendorlib}/Pod/PseudoPod/*
%{_mandir}/*/*
%{_bindir}/*

