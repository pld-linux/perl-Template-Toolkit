#
# Conditional build:
%bcond_without 	autodeps	# don't BR packages needed only for resolving deps
%bcond_without 	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Template
%define		pnam	Toolkit
Summary:	Fast, powerful and easily extensible template processing system
Summary(pl):	Rozbudowany i wydajny system szablonów
Name:		perl-Template-Toolkit
Version:	2.13
Release:	4
# same as perl
License:	GPL v1+ or or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/Template/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.template-toolkit.com/download/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	251c7fb54f522ab11c27ca406beaefe3
Patch0:		%{name}-paths.patch
URL:		http://www.template-toolkit.org/
BuildRequires:	perl-devel >= 1:5.8.0
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
BuildRequires:	perl-XML-DOM >= 1.27
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
Summary(pl):	Przyk³ady zastosowania pakietu Template Toolkit
Group:		Development/Languages/Perl

%description examples
Examples for Template Toolkit

%description examples -l pl
Przyk³ady zastosowania Template Toolkit.

%package Plugin-GD
Summary:	GD plugins for Template Toolkit - graphics operations
Summary(pl):	Wtyczki GD dla pakietu Template Toolkit - operacje graficzne
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-GD
GD plugins for Template Toolkit - interface to GD graphics library.

%description Plugin-GD -l pl
Wtyczki GD dla pakietu Template Tookit. Stanowi± one interfejs do
biblioteki graficznej GD.

%package Plugin-Autoformat
Summary:	Autoformat plugin for Template Toolkit - text formatting
Summary(pl):	Wtyczka Autoformat dla pakietu Template Toolkit - formatowanie tekstu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-Autoformat
Autoformat plugin for Template Toolkit - interface to Text::Autoformat
module which provides advanced text wrapping and formatting.

%description Plugin-Autoformat -l pl
Wtyczka Autoformat dla pakietu Template Toolkit. Stanowi ona interfejs
do modu³u Text::Autoformat umo¿liwiaj±cego zaawansowane zawijanie i
formatowanie tekstu.

%package Plugin-Date
Summary:	Date plugin for Template Toolkit - date formatting
Summary(pl):	Wtyczka Date dla pakietu Template Toolkit - formatowanie daty
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
#Requires:	perl-Date-Calc
Requires:	perl-Date-Manip

%description Plugin-Date
Date plugin for Template Toolkit - to generate formatted date strings.

%description Plugin-Date -l pl
Wtyczka Date dla pakietu Template Toolkit. S³u¿y ona do generowania
sformatowanych ³añcuchów znaków opisuj±cych datê.

%package Plugin-DBI
Summary:	DBI plugin for Template Toolkit - database access
Summary(pl):	Wtyczka DBI dla pakietu Template Toolkit - dostêp do baz danych
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-DBI
DBI plugin for Template Toolkit - interface to the DBI module. It
provides an interface to the Perl DBI/DBD modules, allowing you to
integrate SQL queries into your template documents. It also provides
an interface via the Tie::DBI module (if installed on your system) so
that you can access database records without having to embed any SQL
in your templates.

%description Plugin-DBI -l pl
Wtyczka DBI dla pakietu Template Toolkit - bêd±ca interfejsem do
modu³u DBI. Daje dostêp do modu³ów Perla DBI/DBD, pozwalaj±c na
integrowanie zapytañ SQL do dokumentów szablonów. Udostêpnia tak¿e
interfejs poprzez modu³ Tie::DBI (je¶li jest zainstalowany), co
pozwala na dostêp do rekordów bazy danych bez potrzeby osadzania SQL-a
w szablonach.

%package Plugin-Image
Summary:	Image plugin for Template Toolkit - encapsulating information about images
Summary(pl):	Wtyczka Image dla pakietu Template Toolkit - wstawianie informacji o obrazkach
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-Image
Image plugin for Template Toolkit - interface to the Image::Info or
Image::Size modules for determining the size of image files.

%description Plugin-Image -l pl
Wtyczka Image dla pakietu Template Toolkit - bêd±ca interfejsem do
modu³u Image::Info lub Image::Size, s³u¿±ca do okre¶lania rozmiaru
obrazków.

%package Plugin-Pod
Summary:	Pod plugin for Template Toolkit - Pod parser and object model
Summary(pl):	Wtyczka Pod dla pakietu Template Toolkit - analizator i model obiektowy Pod
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-Pod
Pod plugin for Template Toolkit - interface to the POD::POM module,
which parses Pod documents and converts them to a simple object model.

%description Plugin-Pod -l pl
Wtyczka Pod dla pakietu Template Toolkit - bêd±ca interfejsem do
modu³u Pod::POM, który analizuje dokumenty Pod i przekszta³ca je na
prosty obiektowy model.

%package Plugin-Dumper
Summary:	Dumper plugin for Template Toolkit - dumping data structures
Summary(pl):	Wtyczka Dumper dla pakietu Template Toolkit - wypisywanie struktur danych
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-Dumper
Dumper plugin for Template Toolkit - interface to Data::Dumper module,
which translates data structures to strings.

%description Plugin-Dumper -l pl
Wtyczka Dumper dla pakietu Template Toolkit - bêd±ca interfejsem do
modu³u Data::Dumper, który przekszta³ca struktury danych na ³añcuchy
znaków.

%package Plugin-XML-DOM
Summary:	XML::DOM plugin for Template Toolkit
Summary(pl):	Wtyczka XML::DOM dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-XML-DOM
XML::DOM plugin for Template Toolkit - interface to the XML::DOM
module.

%description Plugin-XML-DOM -l pl
Wtyczka XML::DOM dla pakietu Template Toolkit - interfejs do modu³u
XML::DOM.

%package Plugin-XML-RSS
Summary:	XML::RSS plugin for Template Toolkit - parsing RSS files
Summary(pl):	Wtyczka XML::RSS dla pakietu Template Toolkit - analiza plików RSS
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-XML-RSS
XML::RSS plugin for Template Toolkit - interface to the XML::RSS
module. It creates an XML::RSS object, which is then used to parse
specified RSS file. An RSS (Rich Site Summary) file is typically
used to store short news 'headlines' describing different links
within a site.

%description Plugin-XML-RSS -l pl
Wtyczka XML::RSS dla pakietu Template Toolkit - interfejs do modu³u
XML::RSS. Tworzy on obiekt XML::RSS, który mo¿na u¿yæ do analizy
podanego pliku RSS. Pliki RSS (Rich Site Summary - obfite streszczenie
witryny) zwykle s± u¿ywane do zapisywania krótkich nowinek opisuj±cych
odno¶niki na witrynie.

%package Plugin-XML-Simple
Summary:	XML::Simple plugin for Template Toolkit
Summary(pl):	Wtyczka XML::Simple dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-XML-Simple
XML::Simple plugin for Template Toolkit - interface to the XML::Simple
module.

%description Plugin-XML-Simple -l pl
Wtyczka XML::Simple dla pakietu Template Toolkit - interfejs do modu³u
XML::Simple.

%package Plugin-XML-Style
Summary:	XML::Style plugin for Template Toolkit - simple stylesheet-like transformations
Summary(pl):	Wtyczka XML::Style dla pakietu Template Tookit - proste przekszta³cenia styli
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-XML-Style
XML::Style plugin for Template Toolkit. It defines a filter for
performing simple stylesheet based transformations of XML text.

%description Plugin-XML-Style -l pl
Wtyczka XML::Style dla pakietu Template Toolkit. Definiuje ona filtr
do wykonywania opartych na arkuszu styli przekszta³ceñ tekstu XML.

%package Plugin-XML-XPath
Summary:	XML::XPath plugin for Template Toolkit
Summary(pl):	Wtyczka XML::XPath dla pakietu Template Toolkit
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Plugin-XML-XPath
XML::XPath plugin for Template Toolkit - interface to the XML::XPath
module. All methods implemented by the XML::XPath modules are
available. In addition, the XML::XPath::Node::Element module
implements present($view) and content($view) methods method for
seamless integration with Template Toolkit VIEWs. The
XML::XPath::Node::Text module is also adorned with a present($view)
method which presents itself via the view using the 'text' template.

%description Plugin-XML-XPath -l pl
Wtyczka XML::XPath dla pakietu Template Toolkit - bêd±ca interfejsem
do modu³u XML::XPath. Dostêpne s± wszystkie metody zaimplementowane w
modu³ach XML::XPath, a ponadto modu³ XML::XPath::Node::Element zawiera
implementacje metod present($view) i content($view) do spójnej
integracji z widokami Toolkitu. Modu³ XML::XPath::Node::Text jest
dodatkowo ulepszony o metodê present($view) prezentuj±c± siê przez
widok przy u¿yciu szablonu 'text'.

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
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT
# For arch-independent plugins. Plugins shipped with TT are
# arch-independent too, but moving them to %{perl_vendorlib}
# is PITA
%{__install} -d $RPM_BUILD_ROOT%{perl_vendorlib}/Template
%{__install} -d $RPM_BUILD_ROOT%{perl_vendorlib}/Template/Plugin

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
# For arch-independent plugins
%dir %{perl_vendorlib}/Template/Plugin
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

%files Plugin-GD
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/GD

%files Plugin-Autoformat
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Autoformat.pm

%files Plugin-Date
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Date.pm

%files Plugin-DBI
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/DBI.pm

%files Plugin-Image
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Image.pm

%files Plugin-Pod
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Pod.pm

%files Plugin-Dumper
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Dumper.pm

%files Plugin-XML-DOM
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/DOM.pm

%files Plugin-XML-RSS
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/RSS.pm

%files Plugin-XML-Simple
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/Simple.pm

%files Plugin-XML-Style
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/Style.pm

%files Plugin-XML-XPath
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/XML/XPath.pm
