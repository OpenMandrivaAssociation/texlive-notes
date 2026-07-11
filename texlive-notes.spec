%global tl_name notes
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Mark sections of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/notes
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides environments to highlight significant portions of
text within a document, by putting the text in a box and adding an icon
in the margin. (The icons are provided as 'fig' sources, processable by
xfig.)

