# revision 15878
# category Package
# catalog-ctan /language/hyphenation/utils/mkpattern
# catalog-date 2008-08-22 16:39:18 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-mkpattern
Version:	1.2
Release:	1
Summary:	A utility for making hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/utils/mkpattern
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpattern.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mkpattern.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Mkpattern is a general purpose program for the generation of
hyphenation patterns, with definition of letter sets and
template-like constructions. It also provides an easy way to
handle different input and output encodings, and featgures
generation of clean UTF-8 patterns. The package was used for
the creation of the Galician patterns.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/mkpattern/mkpatter.tex
%doc %{_texmfdistdir}/doc/plain/mkpattern/README
%doc %{_texmfdistdir}/doc/plain/mkpattern/mkpatdoc.tex
%doc %{_texmfdistdir}/doc/plain/mkpattern/mkpatter.pdf
%doc %{_texmfdistdir}/doc/plain/mkpattern/mkpattern-exmpl.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
