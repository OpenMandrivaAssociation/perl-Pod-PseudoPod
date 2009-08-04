%define upstream_name	 Pod-PseudoPod
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	A framework for parsing O'Reilly's PseudoPod
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AR/ARANDAL/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-Pod-Simple
BuildRequires:  perl-HTML-Parser
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
PseudoPod is an extended set of Pod tags used by O'Reilly and Associates
publishing for book manuscripts. Standard Pod doesn't have all the markup
options you need to mark up files for publishing production. PseudoPod adds a
few extra tags for footnotes, tables, sidebars, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
