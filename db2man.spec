Summary:	Docbook refentry to roff converter
Summary(pl):	Konwerter z docbook/refentry do roff
Name:		db2man
Version:	0.1
Release:	1
License:	unknown
Group:		Applications/Publishing/XML
URL:		http://www.ocaml-programming.de/programming/download-caml.html
Source0:	http://www.ocaml-programming.de/packages/%{name}-%{version}.tar.gz
BuildRequires:	ocaml-tony-devel
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml >= 3.04-7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool converts a "docbook" document that is represented as XML
file to manual pages. All "refentry" sections are transformed to
"troff"-formatted documents. Currently, only a subset of the "docbook"
tags that are allowed in "refentry" are supported. Unknown tags are
simply ignored.

%description -l pl
Narzêdzie to konwertuje dokument w formacie XML-docbook do stron
podrêcznika systemowego. Wszystkie sekcje "refentry" s± transformowane
w formatowane troffem dokumenty. Chwilowo, dozwolony jest tylko
podzbiór tagów docbooka, nieznane tagi s± po prostu ignorowane.

%prep
%setup -q -n %{name}

%build
ocamlfind ocamlopt -o db2man -package tony -linkpkg db2man.ml

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install db2man $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
