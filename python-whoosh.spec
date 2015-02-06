%define tarname	Whoosh
%define	rel		1
%if %mdkversion < 201100
%else
%endif

Summary:	Fast, pure Python full text indexing, search, and spell checking library

Name:		python-whoosh
Version:	2.6.0
Release:	2
Source0:	http://pypi.python.org/packages/source/W/Whoosh/Whoosh-%{version}.zip
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/Whoosh/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
PYTHONPATH=`dir -d build/lib*` sphinx-build -b html docs/source html
%__rm -rf html/.buildinfo html/.doctrees

chmod 644 *.txt
chmod 644 %{buildroot}%{py_puresitedir}/%{tarname}-%{version}-py%{py_ver}.egg-info/*

%clean

%files
%doc *.txt html/
%{py_puresitedir}/%{tarname}*
%{py_puresitedir}/whoosh*



