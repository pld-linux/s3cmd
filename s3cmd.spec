Summary:	S3cmd tool for Amazon Simple Storage Service (S3)
Summary(pl.UTF-8):	Narzędzie s3cmd do obsługi Amazon Simple Storage Service (S3)
Name:		s3cmd
Version:	2.4.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://downloads.sourceforge.net/s3tools/%{name}-%{version}.tar.gz
# Source0-md5:	f206e8670b3f0cf9b40c5af72eb96eb6
Patch0:		file-magic.patch
Patch1:		%{name}-regex-escapes.patch
Patch2:		%{name}-py3-configparser.patch
Patch3:		%{name}-py3-dict-keys.patch
URL:		https://s3tools.org/s3cmd
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules
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

%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

rm -r $RPM_BUILD_ROOT%{_docdir}/packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md NEWS
%attr(755,root,root) %{_bindir}/s3cmd
%{py3_sitescriptdir}/S3
%{py3_sitescriptdir}/s3cmd-%{version}-py*.egg-info
%{_mandir}/man1/s3cmd.1*
