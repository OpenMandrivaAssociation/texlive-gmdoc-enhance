# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gmdoc-enhance
# catalog-date 2009-03-01 13:29:14 +0100
# catalog-license lppl
# catalog-version v0.2
Name:		texlive-gmdoc-enhance
Version:	v0.2
Release:	3
Summary:	Some enhancements to the gmdoc package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmdoc-enhance
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides some enhancements for the gmdoc package:
nicer formatting for multiple line inline comments, an ability
to "comment out" some code, and a macro to input other files in
"normal" LaTeX mode.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gmdoc-enhance/gmdoc-enhance.sty
%doc %{_texmfdistdir}/doc/latex/gmdoc-enhance/README
%doc %{_texmfdistdir}/doc/latex/gmdoc-enhance/gmdoc-enhance.pdf
#- source
%doc %{_texmfdistdir}/source/latex/gmdoc-enhance/gmdoc-enhance.dtx
%doc %{_texmfdistdir}/source/latex/gmdoc-enhance/gmdoc-enhance.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.2-2
+ Revision: 752358
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.2-1
+ Revision: 718563
- texlive-gmdoc-enhance
- texlive-gmdoc-enhance
- texlive-gmdoc-enhance
- texlive-gmdoc-enhance

