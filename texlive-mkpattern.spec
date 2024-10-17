Name:		texlive-mkpattern
Version:	15878
Release:	2
Summary:	A utility for making hyphenation patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/utils/mkpattern
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpattern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpattern.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Mkpattern is a general purpose program for the generation of
hyphenation patterns, with definition of letter sets and
template-like constructions. It also provides an easy way to
handle different input and output encodings, and featgures
generation of clean UTF-8 patterns. The package was used for
the creation of the Galician patterns.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/mkpattern/mkpatter.tex
%doc %{_texmfdistdir}/doc/plain/mkpattern/README
%doc %{_texmfdistdir}/doc/plain/mkpattern/mkpatdoc.tex
%doc %{_texmfdistdir}/doc/plain/mkpattern/mkpatter.pdf
%doc %{_texmfdistdir}/doc/plain/mkpattern/mkpattern-exmpl.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
