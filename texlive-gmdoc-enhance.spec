%global tl_name gmdoc-enhance
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Some enhancements to the gmdoc package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmdoc-enhance
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmdoc-enhance.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides some enhancements for the gmdoc package: nicer
formatting for multiple line inline comments, an ability to "comment
out" some code, and a macro to input other files in "normal" LaTeX mode.

