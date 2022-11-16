Name:		texlive-ptolemaicastronomy
Version:	50810
Release:	1
Summary:	Diagrams of sphere models for variably strict conditionals (Lewis counterfactuals)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ptolemaicastronomy
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptolemaicastronomy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptolemaicastronomy.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptolemaicastronomy.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
David K. Lewis (Counterfactuals, Blackwell 1973) introduced a
sphere semantics for counterfactual conditionals. He jokingly
referred to the diagrams depicting such sphere models as
Ptolemaic astronomy, hence the name of this package. The macros
provided in this package aid in the construction of sphere
model diagrams in the style of Lewis. The macros all make use
of TikZ.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ptolemaicastronomy
%{_texmfdistdir}/tex/latex/ptolemaicastronomy
%doc %{_texmfdistdir}/doc/latex/ptolemaicastronomy

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
