#TARBALL:	http://ftp.gnu.org/gnu/groff/groff-1.22.4.tar.gz
#MD5SUM:	08fb04335e2f5e73f23ea4c3adbf0c5f;SOURCES/groff-1.22.4.tar.gz
#-----------------------------------------------------------------------------
Summary:	The Groff package contains programs for processing and formatting text.
Name:		groff
Version:	1.22.4
Release:	1
License:	GPLv3
URL:		Any
Group:		LFS/Base
Vendor:	Elizabeth
Source0:	http://ftp.gnu.org/gnu/groff/%{name}-%{version}.tar.gz
#Provides:	perl(main_subs.pl)
#Provides:	perl(man.pl)
#Provides:	perl(oop_fh.pl)
#Provides:	perl(subs.pl)
Requires:	filesystem
%description
The Groff package contains programs for processing and formatting text.
#-----------------------------------------------------------------------------
%prep
%setup -q -n %{NAME}-%{VERSION}
%build
	PAGE=letter ./configure --prefix=%{_prefix}
	make
%install
	make DESTDIR=%{buildroot} install
#-----------------------------------------------------------------------------
#	Copy license/copying file
	install -D -m644 COPYING %{buildroot}/usr/share/licenses/%{name}/LICENSE
#-----------------------------------------------------------------------------
#	Create file list
	rm  %{buildroot}%{_infodir}/dir
	find %{buildroot} -name '*.la' -delete
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
	sed -i '/man\/man/d' filelist.rpm
	sed -i '/\/usr\/share\/info/d' filelist.rpm
#-----------------------------------------------------------------------------
%files -f filelist.rpm
	%defattr(-,root,root)
	%{_infodir}/*
	%{_mandir}/man1/*
	%{_mandir}/man5/*
	%{_mandir}/man7/*
#-----------------------------------------------------------------------------
%changelog
*	Sat Apr 06 2019 baho-utot <baho-utot@columbus.rr.com> 1.22.4-1
-	LFS-8.4
*	Tue Jan 09 2018 baho-utot <baho-utot@columbus.rr.com> 1.22.3-1
-	Initial build.	First version
