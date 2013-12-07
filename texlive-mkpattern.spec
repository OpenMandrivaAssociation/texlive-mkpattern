# revision 15878
# category Package
# catalog-ctan /language/hyphenation/utils/mkpattern
# catalog-date 2008-08-22 16:39:18 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-mkpattern
Version:	1.2
Release:	6
Summary:	A utility for making hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/utils/mkpattern
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpattern.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpattern.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 754020
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719046
- texlive-mkpattern
- texlive-mkpattern
- texlive-mkpattern
- texlive-mkpattern

