%define		module	pycups
Summary:	Set of Python bindings for the CUPS API
Summary(pl.UTF-8):	Zbiór wiązań Pythona do API CUPS-a
Name:		python-%{module}
Version:	1.9.60
Release:	2
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
# Source0-md5:	083f3dd657df986e712a6fae36427457
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
pycups to zbiór wiązań Pythona do API CUPS-a.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation

%description doc
Documentation for %{name}.

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
%doc ChangeLog README NEWS TODO
%attr(755,root,root) %{py_sitedir}/cups.so
%{py_sitedir}/pycups*.egg-info
