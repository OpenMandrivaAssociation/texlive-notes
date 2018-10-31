Name:		texlive-notes
Version:	1.0.1
Release:	2
Summary:	Mark sections of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/notes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides environments to highlight significant
portions of text within a document, by putting the text in a
box and adding an icon in the margin. (The icons are provided
as 'fig' sources, processable by xfig.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/notes/hand.eps
%{_texmfdistdir}/tex/latex/notes/hand.pdf
%{_texmfdistdir}/tex/latex/notes/hand.png
%{_texmfdistdir}/tex/latex/notes/info.eps
%{_texmfdistdir}/tex/latex/notes/info.pdf
%{_texmfdistdir}/tex/latex/notes/info.png
%{_texmfdistdir}/tex/latex/notes/notes.sty
%{_texmfdistdir}/tex/latex/notes/warn.eps
%{_texmfdistdir}/tex/latex/notes/warn.pdf
%{_texmfdistdir}/tex/latex/notes/warn.png
%doc %{_texmfdistdir}/doc/latex/notes/book.layout
%doc %{_texmfdistdir}/doc/latex/notes/hand.fig
%doc %{_texmfdistdir}/doc/latex/notes/info.fig
%doc %{_texmfdistdir}/doc/latex/notes/makedoc
%doc %{_texmfdistdir}/doc/latex/notes/makedoc.bat
%doc %{_texmfdistdir}/doc/latex/notes/notes.inc
%doc %{_texmfdistdir}/doc/latex/notes/notes.pdf
%doc %{_texmfdistdir}/doc/latex/notes/testnotes.tex
%doc %{_texmfdistdir}/doc/latex/notes/warn.fig
#- source
%doc %{_texmfdistdir}/source/latex/notes/Makefile
%doc %{_texmfdistdir}/source/latex/notes/notes.drv
%doc %{_texmfdistdir}/source/latex/notes/notes.dtx
%doc %{_texmfdistdir}/source/latex/notes/notes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
