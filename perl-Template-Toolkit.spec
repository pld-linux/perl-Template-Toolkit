#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Template
%define	pnam	Toolkit
Summary:	Template::Toolkit Perl extension
Summary(pl):	Rozszerzenie perla: Template::Toolkit
Name:		perl-Template-Toolkit
Version:	2.08
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
URL:		http://www.template-toolkit.org
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-AppConfig >= 1.52
BuildRequires:	perl-DBI >= 1.14
BuildRequires:	perl-GD >= 1.32
BuildRequires:	perl-GD-Graph >= 1.33
BuildRequires:	perl-GD-Graph3d >= 0.55
BuildRequires:	perl-GD-TextUtil >= 0.80
BuildRequires:	perl-Pod-POM >= 0.1
BuildRequires:	perl-Text-Autoformat >= 1.03
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	perl-XML-RSS >= 0.9
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-XML-XPath >= 1.00
BuildRequires:	perl-libxml-enno
BuildRequires:	perl(XML::DOM) >= 1.27
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	tetex-dvips
Requires:	tetex-latex
Requires:	tetex-pdftex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system. It
was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.

It can be used as a stand-alone Perl module or embedded within an
Apache/mod_perl server for generating highly configurable dynamic web
content. A number of Perl scripts are also provided which can greatly
simplify the process of creating and managing static web content and
other offline document systems.

%description -l pl
Template Toolkit to zestaw modu³ów z implementacj± szybkiego,
elastycznego, potê¿nego i rozszerzalnego systemu przetwarzania
wzorców. Oryginalnie zosta³ zaprojektowany i nadal jest u¿ywany
g³ównie do generowania dynamicznych stron WWW, ale mo¿e byæ tak¿e
u¿yty do przetwarzania dowolnych innych rodzajów dokumentów
tekstowych: HTML, XML, POD, PostScript, LaTeX itd.

Mo¿e byæ u¿ywany jako samodzielny modu³ Perla, lub wbudowany w serwer
Apache/mod_perl do wysoko konfigurowalnego generowania dynamicznych
stron WWW. Za³±czonych jest wiele skryptów Perla, które mog± upro¶ciæ
proces tworzenia i zarz±dzania statycznymi stronami WWW oraz innymi
systemami dokumentów offline.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL \
	TT_DBI=n \
	TT_LATEX=y \
	TT_PREFIX=%{_examplesdir}/%{name}-%{version} \
	TT_IMAGES=%{_examplesdir}/%{name}-%{version}/images \
	TT_ACCEPT=y

%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}
# GD tests fail as in perl-GD (2.01)
# possible explanation - see perl-GD.spec

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes HACKING README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/Template.pm
%{perl_sitearch}/Template
%dir %{perl_sitearch}/auto/Template
%dir %{perl_sitearch}/auto/Template/Stash
%dir %{perl_sitearch}/auto/Template/Stash/XS
%{perl_sitearch}/auto/Template/Stash/XS/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Template/Stash/XS/*.so
%{_mandir}/man[13]/*
%{_examplesdir}/%{name}-%{version}
