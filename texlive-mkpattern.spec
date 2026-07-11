%global tl_name mkpattern
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	A utility for making hyphenation patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/utils/mkpattern
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpattern.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpattern.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Mkpattern is a general purpose program for the generation of hyphenation
patterns, with definition of letter sets and template-like
constructions. It also provides an easy way to handle different input
and output encodings, and features generation of clean UTF-8 patterns.
The package was used for the creation of the Galician patterns.

