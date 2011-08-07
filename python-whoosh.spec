%define tarname	Whoosh
%define name	python-whoosh
%define version 2.1.0
%define release %mkrel 1

Summary:	Fast, pure Python full text indexing, search, and spell checking library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	Apache 2.0
Group:		Development/Python
Url:		http://pypi.python.org/pypi/Whoosh/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx

%description
Whoosh is a fast, featureful full-text indexing and searching library
implemented in pure Python. Programmers can use it to easily add
search functionality to their applications and websites. Every part of
how Whoosh works can be extended or replaced to meet your needs
exactly.

Some of Whoosh's features include:

* Pythonic API.
* Pure-Python. No compilation or binary packages needed, no mysterious
  crashes.
* Fielded indexing and search.
* Fast indexing and retrieval -- faster than any other pure-Python,
  scoring, full-text search solution I know of.
* Pluggable scoring algorithm (including BM25F), text analysis,
  storage, posting format, etc.
* Powerful query language parsed by pyparsing.
* Pure Python spell-checker (as far as I know, the only one).

%prep
%setup -q -n %{tarname}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
PYTHONPATH=`dir -d build/lib*` sphinx-build -b html docs/source html
%__rm -rf html/.buildinfo html/.doctrees

chmod 644 *.txt
chmod 644 %{buildroot}%{py_sitedir}/%{tarname}-%{version}-py%{py_ver}.egg-info/*

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt html/


