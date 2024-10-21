Name:		peg
Version:	0.1.19
Release:	1
Summary:	Recursive-descent parser generators for C
License:	MIT
Group:		Development/Tools
URL:		https://www.piumarta.com/software/peg/
Source0:	https://www.piumarta.com/software/peg/%{name}-%{version}.tar.gz
Patch0:		2001_makefile_configuration.patch
Patch1:		2002_examples_fixes.patch

Provides:	leg = %{version}-%{release}
Provides:	leg%{_isa} = %{version}-%{release}

%description
This package provides peg and leg, two utilities that read a Parsing
Expression Grammar (PEG) and generate a recursive-descent parser for
it.

Unlike lex and yacc, peg and leg support unlimited backtracking,
provide ordered choice as a means for disambiguation, and can combine
scanning (lexical analysis) and parsing (syntactic analysis) into a
single activity.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
%make_build

PATH="..:$PATH" \
%make_build -C examples
%make_build -C examples clean

%install
%make_install ROOT=%{buildroot} PREFIX=%{_prefix}

%files
%doc ChangeLog README.txt examples/
%license LICENSE.txt
%{_bindir}/leg
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
