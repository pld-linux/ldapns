Summary:	LDAP Nameservice clients and scripts
Name:		ldapns
Version:	0.1
Release:	1
Group:		Networking
Copyright:	GPL/LGPL
Vendor:		Raging Network Services
Source:		ftp://ftp.rage.net/pub/LDAP/ldapns-0.1.tgz
Patch:		ldapns-0.1.patch
Requires:	gdbm
BuildRoot:	/tmp/%{name}-%{version}-root

%description
LDAP nameservice clients and scripts which allow a host to participate
in an RFC2307 compliant network nameservice scheme. 

%prep
%setup -n ldapns
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.PAM README.NSS ANNOUNCE.NSS pam.conf
#%doc ANNOUNCEMENT CHANGES COPYRIGHT INSTALL README
#%doc doc/guides/guide.pdf doc/guides/guide.ps.Z doc/rfc/rfc*
%config /etc/ldap/ldap.conf
%config /etc/ldap/ldap.sec
%config /etc/nsswitch.ldap
%config /etc/pam.conf.ldap
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

/usr/sbin/ldapinit
/usr/sbin/ldapmigrate
/lib/security/pam_ldap.so
/lib/libnss_ldap.so.1
/usr/man/man5/ldap.conf.5
/usr/man/man8/ldapmigrate.8
/usr/man/man8/ldapinit.8
/usr/man/man8/nss_ldap.8
/usr/man/man8/pam_ldap.8
