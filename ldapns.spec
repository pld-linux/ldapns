Summary:	LDAP Nameservice clients and scripts
Summary(pl):	Klienci i skrypty LDAP Nameservice
Name:		ldapns
Version:	0.1
Release:	1
Group:		Networking
License:	GPL/LGPL
Vendor:		Raging Network Services
Source0:	ftp://ftp.rage.net/pub/LDAP/%{name}-%{version}.tgz
Patch0:		%{name}-0.1.patch
Requires:	gdbm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LDAP nameservice clients and scripts which allow a host to participate
in an RFC2307 compliant network nameservice scheme.

%description -l pl
Klienci i skrypty do serwisu nazw (Nameservice) LDAP pozwalaj±ce
uczestniczyæ w sieci zgodnej z RFC2307.

%prep
%setup -q -n ldapns
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install

gzip -9nf README.PAM README.NSS ANNOUNCE.NSS

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldcongif
%postun -p /sbin/ldcongif

%files
%defattr(644,root,root,755)
%doc {README.PAM,README.NSS,ANNOUNCE.NSS}.gz pam.conf
#%doc ANNOUNCEMENT CHANGES COPYRIGHT INSTALL README
#%doc doc/guides/guide.pdf doc/guides/guide.ps.Z doc/rfc/rfc*
%config %{_sysconfdir}/ldap/ldap.conf
%config %{_sysconfdir}/ldap/ldap.sec
%config %{_sysconfdir}/nsswitch.ldap
%config %{_sysconfdir}/pam.conf.ldap
/etc/pam.d.ldap/chfn
/etc/pam.d.ldap/chsh
/etc/pam.d.ldap/imap
/etc/pam.d.ldap/linuxconf
/etc/pam.d.ldap/linuxconf-pair
/etc/pam.d.ldap/login
/etc/pam.d.ldap/other
/etc/pam.d.ldap/passwd
/etc/pam.d.ldap/rexec
/etc/pam.d.ldap/rlogin
/etc/pam.d.ldap/rsh
/etc/pam.d.ldap/samba
/etc/pam.d.ldap/ssh
/etc/pam.d.ldap/su
/etc/pam.d.ldap/xdm

%attr(755,root,root) %{_sbindir}/ldapinit
%attr(755,root,root) %{_sbindir}/ldapmigrate
%attr(755,root,root) /lib/security/pam_ldap.so
%attr(755,root,root) /lib/libnss_ldap.so.1
%{_mandir}/man5/ldap.conf.5*
%{_mandir}/man8/ldapmigrate.8*
%{_mandir}/man8/ldapinit.8*
%{_mandir}/man8/nss_ldap.8*
%{_mandir}/man8/pam_ldap.8*
