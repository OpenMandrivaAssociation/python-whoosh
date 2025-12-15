%define oname Whoosh_Reloaded

Summary:	Fast, pure-Python full text indexing, search, and spell checking library.
Name:		python-whoosh
Version:	2.7.5
Release:	1
License:	BSD-2-Clause
Group:		Development/Python
# Original upstream is unmaintained:
# https://github.com/whoosh-community/whoosh/issues/561
# This fork is actively maintained and making releases
URL:		https://github.com/Sygil-Dev/whoosh-reloaded
# As original upstream is unmaintained and pypi org ownership cannot
# be changed pull the forked releases from git
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:		noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cached-property)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)


%description
Fast, pure-Python full text indexing, search, and spell checking library.

%prep
%autosetup -n whoosh-reloaded-%{version} -p1
# Remove bundled egg-info
rm -rf src/%{oname}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.md
%license LICENSE.txt
%{python_sitelib}/whoosh
%{python_sitelib}/%{oname}-%{version}*.*-info
