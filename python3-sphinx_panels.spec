Summary:	Sphinx extension for creating panels in a grid layout
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do tworzenia paneli w układzie siatkowym
Name:		python3-sphinx_panels
Version:	0.6.0
Release:	5
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-panels/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-panels/sphinx-panels-%{version}.tar.gz
# Source0-md5:	f2e926a14ad27d66d59fc329339d496e
Patch0:		sphinx_panels-deprecated.patch
Patch1:		sphinx_panels-requires.patch
# https://github.com/executablebooks/sphinx-panels/pulls
Patch2:		sphinx_panels-PR83.patch
URL:		https://pypi.org/project/sphinx-panels/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension for creating document components optimised for
HTML+CSS.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do tworzenia komponentów dokumentów
zoptymalizowanych pod kątem HTML+CSS.

%prep
%setup -q -n sphinx-panels-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/sphinx_panels
%{py3_sitescriptdir}/sphinx_panels-%{version}-py*.egg-info
