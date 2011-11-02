Name:		texlive-gmdoc-enhance
Version:	v0.2
Release:	1
Summary:	Some enhancements to the gmdoc package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmdoc-enhance
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides some enhancements for the gmdoc package:
nicer formatting for multiple line inline comments, an ability
to "comment out" some code, and a macro to input other files in
"normal" LaTeX mode.

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
