Name:		ajenti
Version:	0.6.1
Release:	%mkrel 1
Summary:	The admin panel you dreamed about has just arrived
Group:		Monitoring 
License:	LGPLv3
Url:		http://ajenti.org
BuildRequires:	python-devel python-setuptools
BuildRequires:	fdupes python-lxml python-OpenSSL python-gevent python-imaging-devel
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

Requires:	python-OpenSSL python-lxml python-gevent python-setuptools python-psutil python-imaging
BuildArch:	noarch

%description
Ajenti is a web-interface for Linux server administration.

Authors:
--------
	Eugeny Pankov <john.pankov (at) gmail.com>
	Dmitry Zamaruev <dmitry.zamaruev (at) gmail.com>


%prep
%setup -q

%build
python setup.py build

%install
%{__python} setup.py install --single-version-externally-managed -O1 --skip-build --root=$RPM_BUILD_ROOT --prefix=/usr
#rm -r %{buildroot}/var/lib/%{name}/plugins/.placeholder

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}-panel
%{_bindir}/%{name}-pkg
%{_sysconfdir}/%{name}
%{_sysconfdir}/init.d/%{name}
%{python_sitelib}/*
%{_var}/lib/%{name}/plugins/

%post
service ajenti start
