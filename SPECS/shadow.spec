#TARBALL:	https://github.com/shadow-maint/shadow/releases/download/4.6/shadow-4.6.tar.xz
#MD5SUM:	b491fecbf1232632c32ff8f1437fd60e;SOURCES/shadow-4.6.tar.xz
#-----------------------------------------------------------------------------
Summary:	The Shadow package contains programs for handling passwords in a secure way.
Name:		shadow
Version:	4.6
Release:	1
License:	Artistic
Group:		LFS/Base
Vendor:	Elizabeth
Source0:	https://github.com/shadow-maint/shadow/releases/download/4.5/%{name}-%{version}.tar.xz
Requires:	filesystem
%description
The Shadow package contains programs for handling passwords in a secure way.
#-----------------------------------------------------------------------------
%prep
%setup -q -n %{NAME}-%{VERSION}
	sed -i 's/groups$(EXEEXT) //' src/Makefile.in
	find man -name Makefile.in -exec sed -i 's/groups\.1 / /'   {} \;
	find man -name Makefile.in -exec sed -i 's/getspnam\.3 / /' {} \;
	find man -name Makefile.in -exec sed -i 's/passwd\.5 / /'   {} \;
	sed -i -e 's@#ENCRYPT_METHOD DES@ENCRYPT_METHOD SHA512@' \
		-e 's@/var/spool/mail@/var/mail@' etc/login.defs
	sed -i 's/1000/999/' etc/useradd
%build
	./configure \
		--sysconfdir=/etc \
		--with-group-name-max-length=32
	make %{?_smp_mflags}
%install
	make DESTDIR=%{buildroot} install
	install -vdm 755 %{buildroot}/bin
	mv -v %{buildroot}/usr/bin/passwd %{buildroot}/bin
#-----------------------------------------------------------------------------
#	Copy license/copying file
	install -D -m644 COPYING %{buildroot}/usr/share/licenses/%{name}/LICENSE
#-----------------------------------------------------------------------------
#	Create file list
	rm -rf %{buildroot}/%{_mandir}/cs
	rm -rf %{buildroot}/%{_mandir}/da
	rm -rf %{buildroot}/%{_mandir}/de
	rm -rf %{buildroot}/%{_mandir}/fi
	rm -rf %{buildroot}/%{_mandir}/fr
	rm -rf %{buildroot}/%{_mandir}/hu
	rm -rf %{buildroot}/%{_mandir}/id
	rm -rf %{buildroot}/%{_mandir}/it
	rm -rf %{buildroot}/%{_mandir}/ja
	rm -rf %{buildroot}/%{_mandir}/ko
	rm -rf %{buildroot}/%{_mandir}/pl
	rm -rf %{buildroot}/%{_mandir}/pt_BR
	rm -rf %{buildroot}/%{_mandir}/ru
	rm -rf %{buildroot}/%{_mandir}/sv
	rm -rf %{buildroot}/%{_mandir}/tr
	rm -rf %{buildroot}/%{_mandir}/zh_CN
	rm -rf %{buildroot}/%{_mandir}/zh_TW
	find "${RPM_BUILD_ROOT}" -not -type d -print > filelist.rpm
	sed -i "s|^${RPM_BUILD_ROOT}||" filelist.rpm
	sed -i '/man/d' filelist.rpm
#-----------------------------------------------------------------------------
%files -f filelist.rpm
	%defattr(-,root,root)
	%{_mandir}/man1/*
	%{_mandir}/man3/*
	%{_mandir}/man5/*
	%{_mandir}/man8/*
%post
	pwconv
	grpconv
#-----------------------------------------------------------------------------
%changelog
*	Tue Mar 26 2019 baho-utot <baho-utot@columbus.rr.com> 4.6-1
*	Tue Jan 09 2018 baho-utot <baho-utot@columbus.rr.com> 4.5-1
-	Initial build.	First version
