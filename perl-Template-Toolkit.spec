%define	pdir	Template
%define	pnam	Toolkit
%include	/usr/lib/rpm/macros.perl
Summary:	Template-Toolkit perl extension
Summary(pl):	Rozszerzenie perla: Template-Toolkit
Name:		perl-Template-Toolkit
Version:	2.06
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(is):	Þróunartól/Forritunarmál/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(no):	Utvikling/Programmeringsspråk/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Group(sl):	Razvoj/Jeziki/Perl
Group(sv):	Utveckling/Språk/Perl
Group(uk):	òÏÚÒÏÂËÁ/íÏ×É/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Requires:	tetex-pdftex
Requires:	tetex-latex
Requires:	tetex-dvips
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-libxml-enno
BuildRequires:  perl(XML::DOM) >= 1.27
BuildRequires:	perl-Text-Autoformat >= 1.03
BuildRequires:	perl-DBI >= 1.14
BuildRequires:	perl-GD >= 1.32
BuildRequires:	perl-GD-TextUtil >= 0.80
BuildRequires:  perl-GD-Graph >= 1.33
BuildRequires:	perl-GD-Graph3d >= 0.55
BuildRequires:  perl-Pod-POM >= 0.1
BuildRequires:  perl-XML-Parser >= 2.23
BuildRequires:  perl-XML-RSS >= 0.9
BuildRequires:	perl-XML-XPath >= 1.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
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
%setup -q -n Template-Toolkit-%{version}
%patch0 -p1

%build
perl Makefile.PL TT_DBI=n TT_LATEX=y TT_PREFIX=%{_examplesdir}/tt2 TT_IMAGES=%{_examplesdir}/tt2/images TT_ACCEPT=y
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes  HACKING  INSTALL  README  TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc %{_examplesdir}/tt2
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/Template.pm
%{perl_sitearch}/Template
%{perl_sitearch}/auto/Template
%{_mandir}/man[13]/*
