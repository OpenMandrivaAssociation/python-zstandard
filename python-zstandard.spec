Name:		python-zstandard
Version:	0.21.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/z/zstandard/zstandard-%{version}.tar.gz
Summary:	Zstandard bindings for Python
URL:		https://pypi.org/project/zstandard/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)

%description
Zstandard bindings for Python

%prep
%autosetup -p1 -n zstandard-%{version}

%build
%py_build

%install
%py_install

%files
%{py_platsitedir}/zstandard
%{py_platsitedir}/zstandard-*.*-info