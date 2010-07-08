#
Summary:	S3cmd tool for Amazon Simple Storage Service (S3)
Name:		s3cmd
Version:	0.9.9.91
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/s3tools/%{name}-%{version}.tar.gz
# Source0-md5:	0b8334ab4ffb1e09d6964861dc001e0f
URL:		http://s3tools.org/s3cmd
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S3cmd lets you copy files from/to Amazon S3 (Simple Storage Service)
using a simple to use command line client. Supports rsync-like backup,
GPG encryption, and more. Also supports management of Amazon's
CloudFront content delivery network.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

rm -r $RPM_BUILD_ROOT%{_docdir}/packages/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/S3
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man1/*
