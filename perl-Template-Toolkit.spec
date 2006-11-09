#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Template
%define		pnam	Toolkit
Summary:	Fast, powerful and easily extensible template processing system
Summary(pl):	Rozbudowany i wydajny system szablonów
Name:		perl-Template-Toolkit
Version:	2.15
Release:	1
# same as perl
License:	GPL v1+ or or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://www.template-toolkit.com/download/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	26adb4e6d3f2f89e2b54a43f73b70a29
Patch0:		%{name}-paths.patch
URL:		http://www.template-toolkit.org/
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-AppConfig >= 1.52
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Pod-POM >= 0.1
BuildRequires:	perl-Text-Autoformat >= 1.03
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

%package Plugin-Autoformat
Summary:	Autoformat plugin for Template Toolkit - text formatting
Summary(pl):	Wtyczka Autoformat dla pakietu Template Toolkit - formatowanie tekstu
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}
#Requires:	perl-Date-Calc
Requires:	perl-Date-Manip

%description Plugin-Date
Date plugin for Template Toolkit - to generate formatted date strings.

%description Plugin-Date -l pl
Wtyczka Date dla pakietu Template Toolkit. S³u¿y ona do generowania
sformatowanych ³añcuchów znaków opisuj±cych datê.

%package Plugin-Dumper
Summary:	Dumper plugin for Template Toolkit - dumping data structures
Summary(pl):	Wtyczka Dumper dla pakietu Template Toolkit - wypisywanie struktur danych
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Plugin-Dumper
Dumper plugin for Template Toolkit - interface to Data::Dumper module,
which translates data structures to strings.

%description Plugin-Dumper -l pl
Wtyczka Dumper dla pakietu Template Toolkit - bêd±ca interfejsem do
modu³u Data::Dumper, który przekszta³ca struktury danych na ³añcuchy
znaków.

%package Plugin-Image
Summary:	Image plugin for Template Toolkit - encapsulating information about images
Summary(pl):	Wtyczka Image dla pakietu Template Toolkit - wstawianie informacji o obrazkach
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}

%description Plugin-Pod
Pod plugin for Template Toolkit - interface to the POD::POM module,
which parses Pod documents and converts them to a simple object model.

%description Plugin-Pod -l pl
Wtyczka Pod dla pakietu Template Toolkit - bêd±ca interfejsem do
modu³u Pod::POM, który analizuje dokumenty Pod i przekszta³ca je na
prosty obiektowy model.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor  \
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
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Template
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Template/Plugin

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
%{perl_vendorarch}/Template/Plugin/Math.pm
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
%{_mandir}/man1/*
%{_mandir}/man3/Template.*
%{_mandir}/man3/Template::[!P]*
%{_mandir}/man3/Template::P[!l]*
%{_mandir}/man3/Template::Plugin[!:]*
%{_mandir}/man3/Template::Plugin::[!ADIP]*
%{_mandir}/man3/Template::Plugin::D[!au]*
%{_mandir}/man3/Template::Plugin::Dat[!e]*
%{_mandir}/man3/Template::Plugin::I[!m]*
%{_mandir}/man3/Template::Plugin::P[!o]*


%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files Plugin-Autoformat
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Autoformat.pm
%{_mandir}/man3/Template::Plugin::Autoformat*

%files Plugin-Date
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Date.pm
%{_mandir}/man3/Template::Plugin::Date*

%files Plugin-Dumper
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Dumper.pm
%{_mandir}/man3/Template::Plugin::Dumper*

%files Plugin-Image
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Image.pm
%{_mandir}/man3/Template::Plugin::Image*

%files Plugin-Pod
%defattr(644,root,root,755)
%{perl_vendorarch}/Template/Plugin/Pod.pm
%{_mandir}/man3/Template::Plugin::Pod*
