
%define		module	pycups

Summary:	Set of Python bindings for the CUPS API
Summary(pl):	Zbiór wi±zañ Pythona do API CUPS-a
Name:		python-%{module}
Version:	1.9.4
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
# Source0-md5:	4d9514fc2d48b5a36fa2ac2c285c8504
BuildRequires:	cups-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycups is a set of Python bindings for the CUPS API.

%description -l pl
pycups to zbiór wi±zañ Pythona do API CUPS-a.

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
