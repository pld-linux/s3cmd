Summary:	S3cmd tool for Amazon Simple Storage Service (S3)
Summary(pl.UTF-8):	Narzędzie s3cmd do obsługi Amazon Simple Storage Service (S3)
Name:		s3cmd
Version:	1.0.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/s3tools/%{name}-%{version}.tar.gz
# Source0-md5:	dc62becc03a3e6100843611ebe2707c2
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

%description -l pl.UTF-8
s3cmd pozwala kopiować pliki z/do usługi Amazon S3 (Simple Storage
Service) przy użyciu prostego w użyciu klienta działającego z linii
poleceń. Obsługuje tworzenie kopii zapasowych w stylu rsynca,
szyfrowanie GPG itp. Pozwala także na zarządzanie siecią udostępniania
treści Amazon CloudFront.

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

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/packages/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/s3cmd
%{py_sitescriptdir}/S3
%{py_sitescriptdir}/s3cmd-%{version}-py*.egg-info
%{_mandir}/man1/s3cmd.1*
