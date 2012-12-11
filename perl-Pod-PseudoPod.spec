%define upstream_name	 Pod-PseudoPod
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A framework for parsing O'Reilly's PseudoPod
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AR/ARANDAL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(Pod::Simple)

BuildArch:	noarch

%description
PseudoPod is an extended set of Pod tags used by O'Reilly and Associates
publishing for book manuscripts. Standard Pod doesn't have all the markup
options you need to mark up files for publishing production. PseudoPod adds a
few extra tags for footnotes, tables, sidebars, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Pod/PseudoPod.pm
%{perl_vendorlib}/Pod/PseudoPod/*
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Tue Mar 30 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.1
+ Revision: 529783
- update to 0.16

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.150.0-2mdv2010.0
+ Revision: 408772
- force rebuild
- rebuild using %%perl_convert_version

* Thu Jun 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2010.0
+ Revision: 387017
- update to new version 0.15

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.13-5mdv2009.0
+ Revision: 258230
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.13-4mdv2009.0
+ Revision: 246308
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.13-2mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-2mdv2008.0
+ Revision: 86795
- rebuild


* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 18:47:24 (59626)
- 0.13

* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 18:46:24 (59625)
Import perl-Pod-PseudoPod

* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-3mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-2mdk
- Buildrequires fix

* Fri Sep 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-1mdk
- Initial Mandriva release

