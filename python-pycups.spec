
%define		module	pycups

Summary:	Set of Python bindings for the CUPS API
Summary(pl):	Zbi�r wi�za� Pythona do API CUPS-a
Name:		python-%{module}
Version:	1.9.8
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
# Source0-md5:	ea37d221e78f39afc5ad04a67e9ee15b
BuildRequires:	cups-devel >= 1.2-0.rc2.1
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycups is a set of Python bindings for the CUPS API.

%description -l pl
pycups to zbi�r wi�za� Pythona do API CUPS-a.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS ChangeLog
%attr(755,root,root) %{py_sitedir}/*.so
