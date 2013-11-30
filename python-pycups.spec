%define		module	pycups
Summary:	Set of Python bindings for the CUPS API
Summary(pl.UTF-8):	Zbiór wiązań Pythona do API CUPS-a
Name:		python-%{module}
Version:	1.9.66
Release:	1
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
# Source0-md5:	a6cc4d40ac908dd9182ed93739b4bb79
URL:		http://cyberelk.net/tim/software/pycups/
BuildRequires:	cups-devel >= 1.2.1
BuildRequires:	epydoc
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
Obsoletes:	python-cups
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Python bindings for the CUPS API, known as
pycups. It was written for use with system-config-printer, but can be
put to other uses as well.

%description -l pl.UTF-8
Ten pakiet udostępnia wiązania Pythona do API CUPS-a, znane jako
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
%{__make} \
	CFLAGS="%{rpmcflags} -fno-strict-aliasing"

%{__make} doc
%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{py_sitedir}/cups.so
%{py_sitedir}/pycups-%{version}-py*.egg-info

%files doc
%defattr(644,root,root,755)
%doc html/*
