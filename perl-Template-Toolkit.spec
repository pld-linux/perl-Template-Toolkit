
# Conditional build:
%bcond_without 	autodeps	# don't BR packages needed only for resolving deps
%bcond_with 	tests		# perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Template
%define	pnam	Toolkit
Summary:	Fast, powerful and easily extensible template processing system
Summary(pl):	Rozbudowany i wydajny system szablonów
Name:		perl-Template-Toolkit
Version:	2.10
Release:	1.90
License:	GPL
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.template-toolkit.com/download/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0c344240ceca9d7746d0a23b066521f0
Patch0:		%{name}-paths.patch
URL:		http://www.template-toolkit.org/
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-AppConfig >= 1.52
%if %{with autodeps} || %{with tests}
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
BuildRequires:	perl(XML::DOM) >= 1.27
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
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


%package examples
Summary:	Examples for Template Toolkit
Summary(pl):	Przyk³ady zastosowania Template Toolkit
Group:		Development/Languages/Perl

%description examples
Examples for Template Toolkit

%description examples -l pl
Przyk³ady zastosowania Template Toolkit.

%define plugin1	GD
%define plugin2	Autoformat
%define plugin3	Date
%define plugin4	DBI
%define plugin5	Image
%define plugin6	Pod
%define plugin7	Dumper
%define plugin8	XML-DOM
%define plugin9	XML-RSS
%define plugin10	XML-Simple
%define plugin11	XML-Style
%define plugin12	XML-XPath

%package Plugin-%{plugin1}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin1}
%{plugin1} plugins for Template Toolkit.

%package Plugin-%{plugin2}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin2}
%{plugin2} plugin for Template Toolkit.

# Date
%package Plugin-%{plugin3}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
#Requires:	perl-Date-Calc
Requires:	perl-Date-Manip
%description Plugin-%{plugin3}
%{plugin3} plugin for Template Toolkit.

%package Plugin-%{plugin4}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin4}
%{plugin4} plugin for Template Toolkit.

%package Plugin-%{plugin5}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin5}
%{plugin5} plugin for Template Toolkit.

%package Plugin-%{plugin6}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin6}
%{plugin6} plugin for Template Toolkit.

%package Plugin-%{plugin7}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin7}
%{plugin7} plugin for Template Toolkit.

%package Plugin-%{plugin8}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin8}
%{plugin8} plugin for Template Toolkit.

%package Plugin-%{plugin9}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin9}
%{plugin9} plugin for Template Toolkit.

%package Plugin-%{plugin10}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin10}
%{plugin10} plugin for Template Toolkit.

%package Plugin-%{plugin11}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin11}
%{plugin11} plugin for Template Toolkit.

%package Plugin-%{plugin12}
Summary:	GD plugins for Template Toolkit
Group:		Development/Languages/Perl
%description Plugin-%{plugin12}
%{plugin12} plugin for Template Toolkit.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor  \
	TT_DBI=n \
	TT_LATEX=y \
	TT_PREFIX=%{_examplesdir}/%{name}-%{version} \
	TT_IMAGES=%{_examplesdir}/%{name}-%{version}/images \
	TT_ACCEPT=y

%{__make} OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}
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
%{perl_vendorarch}/Template.pm
%{perl_vendorarch}/Template/*.pm
%{perl_vendorarch}/Template/Stash
%{perl_vendorarch}/Template/Namespace
%dir %{perl_vendorarch}/Template/Plugin
%dir %{perl_vendorarch}/Template/Plugin/XML
# These are not plugins, but base classes
%{perl_vendorarch}/Template/Plugin/Filter.pm
%{perl_vendorarch}/Template/Plugin/Procedural.pm
# Simple plugins with no excessive requirements
%{perl_vendorarch}/Template/Plugin/CGI.pm
%{perl_vendorarch}/Template/Plugin/Datafile.pm
%{perl_vendorarch}/Template/Plugin/Directory.pm
%{perl_vendorarch}/Template/Plugin/File.pm
%{perl_vendorarch}/Template/Plugin/Format.pm
%{perl_vendorarch}/Template/Plugin/HTML.pm
%{perl_vendorarch}/Template/Plugin/Iterator.pm
%{perl_vendorarch}/Template/Plugin/String.pm
%{perl_vendorarch}/Template/Plugin/Table.pm
%{perl_vendorarch}/Template/Plugin/URL.pm
%{perl_vendorarch}/Template/Plugin/View.pm
%{perl_vendorarch}/Template/Plugin/Wrap.pm
%dir %{perl_vendorarch}/auto/Template
%dir %{perl_vendorarch}/auto/Template/Stash
%dir %{perl_vendorarch}/auto/Template/Stash/XS
%{perl_vendorarch}/auto/Template/Stash/XS/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Template/Stash/XS/*.so
%{_mandir}/man[13]/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files Plugin-%{plugin1}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/GD

%files Plugin-%{plugin2}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/%{plugin2}.pm

%files Plugin-%{plugin3}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/%{plugin3}.pm

%files Plugin-%{plugin4}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/%{plugin4}.pm

%files Plugin-%{plugin5}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/%{plugin5}.pm

%files Plugin-%{plugin6}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/%{plugin6}.pm

%files Plugin-%{plugin7}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/%{plugin7}.pm

%files Plugin-%{plugin8}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/DOM.pm

%files Plugin-%{plugin9}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/RSS.pm

%files Plugin-%{plugin10}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/Simple.pm

%files Plugin-%{plugin11}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/Style.pm

%files Plugin-%{plugin12}
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/XPath.pm
