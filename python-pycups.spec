
%define		module	pycups

Summary:	Set of Python bindings for the CUPS API
Summary(pl.UTF-8):	Zbiór wiązań Pythona do API CUPS-a
Name:		python-%{module}
Version:	1.9.60
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
# Source0-md5:	083f3dd657df986e712a6fae36427457
URL:		http://cyberelk.net/tim/software/pycups/
BuildRequires:	cups-devel >= 1.2.1
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycups is a set of Python bindings for the CUPS API.

%description -l pl.UTF-8
pycups to zbiór wiązań Pythona do API CUPS-a.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="-DVERSION=\\\"%{version}\\\" %{rpmcflags}"
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
%{py_sitedir}/*.egg-info
