%define tarname	Whoosh
%define name	python-whoosh
%define version 2.4.1
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release	%{rel}
%endif

Summary:	Fast, pure Python full text indexing, search, and spell checking library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/W/%{tarname}/%{tarname}-%{version}.tar.gz
License:	BSD
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
PYTHONPATH=`dir -d build/lib*` sphinx-build -b html docs/source html
%__rm -rf html/.buildinfo html/.doctrees

chmod 644 *.txt
chmod 644 %{buildroot}%{py_sitedir}/%{tarname}-%{version}-py%{py_ver}.egg-info/*

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt html/
%py_sitedir/%{tarname}*
%py_sitedir/whoosh*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 2.4.1-1
+ Revision: 814629
- Update to 2.4.1.

* Tue Oct 25 2011 Lev Givon <lev@mandriva.org> 2.3.0-1
+ Revision: 707175
- Update to 2.3.0.

* Sun Aug 07 2011 Lev Givon <lev@mandriva.org> 2.1.0-1
+ Revision: 693550
- Update to 2.1.0.

* Wed Jun 22 2011 Lev Givon <lev@mandriva.org> 1.8.4-1
+ Revision: 686708
- Update to 1.8.4.

* Fri Apr 22 2011 Lev Givon <lev@mandriva.org> 1.8.2-1
+ Revision: 656687
- Update to 0.8.2.

* Fri Mar 04 2011 Lev Givon <lev@mandriva.org> 1.7.6-1
+ Revision: 641548
- Update to 1.7.6.

* Mon Feb 21 2011 Lev Givon <lev@mandriva.org> 1.7.4-1
+ Revision: 639159
- Update to 1.7.4.

* Thu Dec 16 2010 Lev Givon <lev@mandriva.org> 1.4.1-1mdv2011.0
+ Revision: 622413
- Update to 1.4.1.

* Fri Nov 12 2010 Lev Givon <lev@mandriva.org> 1.3.3-2mdv2011.0
+ Revision: 596746
- Fix some file permissions.

* Tue Nov 09 2010 Lev Givon <lev@mandriva.org> 1.3.3-1mdv2011.0
+ Revision: 595332
- Update to 1.3.3.

* Mon Nov 08 2010 Lev Givon <lev@mandriva.org> 1.3.2-1mdv2011.0
+ Revision: 595112
- import python-whoosh


