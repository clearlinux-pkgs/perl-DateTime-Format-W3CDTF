#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-W3CDTF
Version  : 0.08
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/DateTime-Format-W3CDTF-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/DateTime-Format-W3CDTF-0.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-feed-perl/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
Summary  : 'Parse and format W3CDTF datetime strings'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-DateTime-Format-W3CDTF-license = %{version}-%{release}
Requires: perl-DateTime-Format-W3CDTF-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DateTime)

%description
NAME
DateTime::Format::W3CDTF - Parse and format W3CDTF datetime strings
SYNOPSIS
use DateTime::Format::W3CDTF;

%package dev
Summary: dev components for the perl-DateTime-Format-W3CDTF package.
Group: Development
Provides: perl-DateTime-Format-W3CDTF-devel = %{version}-%{release}
Requires: perl-DateTime-Format-W3CDTF = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-W3CDTF package.


%package license
Summary: license components for the perl-DateTime-Format-W3CDTF package.
Group: Default

%description license
license components for the perl-DateTime-Format-W3CDTF package.


%package perl
Summary: perl components for the perl-DateTime-Format-W3CDTF package.
Group: Default
Requires: perl-DateTime-Format-W3CDTF = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-W3CDTF package.


%prep
%setup -q -n DateTime-Format-W3CDTF-0.08
cd %{_builddir}
tar xf %{_sourcedir}/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
cd %{_builddir}/DateTime-Format-W3CDTF-0.08
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/DateTime-Format-W3CDTF-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-W3CDTF
cp %{_builddir}/DateTime-Format-W3CDTF-0.08/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-W3CDTF/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-W3CDTF/808cdef4c992763637fe5a5a7551c6cd5186080b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::W3CDTF.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-W3CDTF/808cdef4c992763637fe5a5a7551c6cd5186080b
/usr/share/package-licenses/perl-DateTime-Format-W3CDTF/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/DateTime/Format/W3CDTF.pm
