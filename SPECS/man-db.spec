#TARBALL:	http://download.savannah.gnu.org/releases/man-db/man-db-2.8.5.tar.xz
#MD5SUM:	c5c6c3434be14a5527d43b5ad0f09a13;SOURCES/man-db-2.8.5.tar.xz
#-----------------------------------------------------------------------------
Summary:	The Man-DB package contains programs for finding and viewing man pages.
Name:		man-db
Version:	2.8.5
Release:	1
License:	Other
URL:		Any
Group:		LFS/Base
Vendor:	Elizabeth
Source0:	man-db/%{name}-%{version}.tar.xz
Requires:	filesystem
%description
The Man-DB package contains programs for finding and viewing man pages.
#-----------------------------------------------------------------------------
%prep
%setup -q -n %{NAME}-%{VERSION}
%build
	./configure \
		--prefix=%{_prefix} \
		--docdir=%{_docdir}/%{NAME}-%{VERSION} \
		--sysconfdir=/etc \
		--disable-setuid \
		--enable-cache-owner=bin \
		--with-browser=%{_bindir}/lynx \
		--with-vgrind=%{_bindir}/vgrind \
		--with-grap=%{_bindir}/grap \
		--with-systemdtmpfilesdir= \
		--with-systemdsystemunitdir=
	make %{?_smp_mflags}
%install
	make DESTDIR=%{buildroot} install
#-----------------------------------------------------------------------------
#	Copy license/copying file
	install -D -m644 README %{buildroot}/usr/share/licenses/%{name}/LICENSE
#-----------------------------------------------------------------------------
#	rm  %{buildroot}%{_infodir}/dir
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
	sed -i '/man\/man/d' filelist.rpm
	sed -i '/man\/es/d'  filelist.rpm	
	sed -i '/man\/it/d'  filelist.rpm
	sed -i '/\/usr\/share\/info/d' filelist.rpm
#-----------------------------------------------------------------------------
%files -f filelist.rpm
	%defattr(-,root,root)
#	%%{_infodir}/*
	%{_mandir}/man1/*
	%{_mandir}/man5/*
	%{_mandir}/man8/*
	%{_mandir}/man8/*
	%{_mandir}/it/man1/*
	%{_mandir}/it/man5/*
	%{_mandir}/it/man8/*
#-----------------------------------------------------------------------------
%changelog
*	Tue Jan 09 2018 baho-utot <baho-utot@columbus.rr.com> 2.8.1-1
-	Initial build.	First version
