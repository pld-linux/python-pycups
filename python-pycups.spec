#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pycups
Summary:	Set of Python 2 bindings for the CUPS API
Summary(pl.UTF-8):	Zbiór wiązań Pythona 2 do API CUPS-a
Name:		python-%{module}
Version:	1.9.73
Release:	12
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
# Source0-md5:	ee0e7204d7a2ae942e2f4c4508afdbfb
URL:		http://cyberelk.net/tim/software/pycups/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	cups-devel >= 1.2.1
BuildRequires:	epydoc
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
Requires:	python-modules
Obsoletes:	python-cups
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Python 2 bindings for the CUPS API, known as
pycups. It was written for use with system-config-printer, but can be
put to other uses as well.

%description -l pl.UTF-8
Ten pakiet udostępnia wiązania Pythona 2 do API CUPS-a, znane jako
pycups. Został napisany z myślą o pakiecie system-config-printer, ale
może mieć także inne zastosowania.

%package -n python3-pycups
Summary:	Set of Python 3 bindings for the CUPS API
Summary(pl.UTF-8):	Zbiór wiązań Pythona 3 do API CUPS-a
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-pycups
This package provides Python 3 bindings for the CUPS API, known as
pycups. It was written for use with system-config-printer, but can be
put to other uses as well.

%description -n python3-pycups -l pl.UTF-8
Ten pakiet udostępnia wiązania Pythona 3 do API CUPS-a, znane jako
pycups. Został napisany z myślą o pakiecie system-config-printer, ale
może mieć także inne zastosowania.

%package doc
Summary:	Documentation for pycups
Summary(pl.UTF-8):	Dokumentacja do pycupsa
Group:		Documentation

%description doc
Documentation for pycups.

%description doc -l pl.UTF-8
Dokumentacja do pycupsa.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
CC="%{__cc}" \
CFLAGS="%{rpmcflags} -fno-strict-aliasing" \
%py_build \
	--build-base build-2
%endif

%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcflags} -fno-strict-aliasing" \
%py3_build \
	--build-base build-3
%endif

%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{py_sitedir}/cups.so
%{py_sitedir}/pycups-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pycups
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{py3_sitedir}/cups.cpython-*.so
%{py3_sitedir}/pycups-%{version}-py*.egg-info
%endif

%files doc
%defattr(644,root,root,755)
%doc html/*
