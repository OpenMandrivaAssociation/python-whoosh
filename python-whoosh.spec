Summary:	Fast, pure-Python full text indexing, search, and spell checking library.
Name:		python-whoosh
Version:	2.7.4
Release:	2
License:	Two-clause BSD license
Group:		Development/Python
URL:		https://pypi.org/project/whoosh/
Source0:	https://files.pythonhosted.org/packages/source/W/Whoosh/Whoosh-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Fast, pure-Python full text indexing, search, and spell checking library.

%prep
%autosetup -p1 -n Whoosh-%{version}

%files
%{py_sitedir}/whoosh
%{py_sitedir}/Whoosh-*.*-info

#----------------------------------------------------------------------

%build
%py_build

%install
%py_install

