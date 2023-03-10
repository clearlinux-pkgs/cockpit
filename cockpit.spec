#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cockpit
Version  : 287
Release  : 152
URL      : https://github.com/cockpit-project/cockpit/releases/download/287/cockpit-287.tar.xz
Source0  : https://github.com/cockpit-project/cockpit/releases/download/287/cockpit-287.tar.xz
Summary  : Web Console for Linux servers
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+ MIT
Requires: cockpit-bin = %{version}-%{release}
Requires: cockpit-config = %{version}-%{release}
Requires: cockpit-data = %{version}-%{release}
Requires: cockpit-lib = %{version}-%{release}
Requires: cockpit-libexec = %{version}-%{release}
Requires: cockpit-license = %{version}-%{release}
Requires: cockpit-man = %{version}-%{release}
Requires: cockpit-services = %{version}-%{release}
Requires: glib-networking
Requires: polkit
Requires: sos
BuildRequires : Linux-PAM-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : krb5-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pcp-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(krb5)
BuildRequires : pkgconfig(krb5-gssapi)
BuildRequires : pkgconfig(libssh)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : util-linux
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Update-cockpit-tmpfile-configuration.patch
Patch2: 0002-Add-PAM-configuration-file.patch

%description
The Cockpit Web Console enables users to administer GNU/Linux servers using a
web browser.

It offers network configuration, log inspection, diagnostic reports, SELinux
troubleshooting, interactive command-line sessions, and more.

Dummy package from building optional packages only; never install or publish me.

%package bin
Summary: bin components for the cockpit package.
Group: Binaries
Requires: cockpit-data = %{version}-%{release}
Requires: cockpit-libexec = %{version}-%{release}
Requires: cockpit-config = %{version}-%{release}
Requires: cockpit-license = %{version}-%{release}
Requires: cockpit-services = %{version}-%{release}

%description bin
bin components for the cockpit package.


%package config
Summary: config components for the cockpit package.
Group: Default

%description config
config components for the cockpit package.


%package data
Summary: data components for the cockpit package.
Group: Data

%description data
data components for the cockpit package.


%package doc
Summary: doc components for the cockpit package.
Group: Documentation
Requires: cockpit-man = %{version}-%{release}

%description doc
doc components for the cockpit package.


%package lib
Summary: lib components for the cockpit package.
Group: Libraries
Requires: cockpit-data = %{version}-%{release}
Requires: cockpit-libexec = %{version}-%{release}
Requires: cockpit-license = %{version}-%{release}

%description lib
lib components for the cockpit package.


%package libexec
Summary: libexec components for the cockpit package.
Group: Default
Requires: cockpit-config = %{version}-%{release}
Requires: cockpit-license = %{version}-%{release}

%description libexec
libexec components for the cockpit package.


%package license
Summary: license components for the cockpit package.
Group: Default

%description license
license components for the cockpit package.


%package man
Summary: man components for the cockpit package.
Group: Default

%description man
man components for the cockpit package.


%package services
Summary: services components for the cockpit package.
Group: Systemd services

%description services
services components for the cockpit package.


%prep
%setup -q -n cockpit-287
cd %{_builddir}/cockpit-287
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678460828
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --enable-pcp
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1678460828
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cockpit
cp %{_builddir}/cockpit-%{version}/COPYING %{buildroot}/usr/share/package-licenses/cockpit/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-base64.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-browser-storage.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-cache.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-chan.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-dbus-address.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-dbus-framed.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-dbus.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-echo.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-events.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-external.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-file.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-format.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-framed-cache.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-framed.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-http.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-journal-renderer.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-locale.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-location.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-metrics.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-no-jquery.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-permissions.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-promise.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-protocol.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-series.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-spawn-proc.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-spawn.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-stream.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-user.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-utf8.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/base1/test-websocket.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/kdump/test-config-client.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/networkmanager/test-utils.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/shell/machines/test-machines.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/dist/storaged/test-util.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb || :
cp %{_builddir}/cockpit-%{version}/node_modules/chrome-remote-interface/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/762f77e8237dfc3015f3e4476035b80fee52af15 || :
cp %{_builddir}/cockpit-%{version}/node_modules/commander/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/63513188251d15fcdc716703fbee89be4a3a20e6 || :
cp %{_builddir}/cockpit-%{version}/node_modules/sizzle/LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/aba8f1f7a4b149e9eec362828f7e8d4bedd68378 || :
cp %{_builddir}/cockpit-%{version}/node_modules/ws/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/5267b8c02607adefda571a85283fcd110ae081ba || :
cp %{_builddir}/cockpit-%{version}/src/bridge/mock-resource/system/cockpit/test-priority/sub/COPYING %{buildroot}/usr/share/package-licenses/cockpit/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/cockpit-%{version}/src/bridge/mock-resource/system/cockpit/test/sub/COPYING %{buildroot}/usr/share/package-licenses/cockpit/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/cockpit-%{version}/tools/debian/copyright %{buildroot}/usr/share/package-licenses/cockpit/d3e41a6a93ea087e3c49d55d20451d23845153f0 || :
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/lib/firewalld/services/cockpit.xml
rm -f %{buildroot}*/var/lib/pcp/config/pmlogconf/tools/cockpit
## install_append content
rm -fr %{buildroot}/usr/share/cockpit/apps
rm -fr %{buildroot}/usr/share/cockpit/dump
rm -fr %{buildroot}/usr/share/cockpit/ostree
rm -fr %{buildroot}/usr/share/cockpit/ovirt
rm -fr %{buildroot}/usr/share/cockpit/packagekit
rm -fr %{buildroot}/usr/share/cockpit/pcp
rm -fr %{buildroot}/usr/share/cockpit/playground
rm -fr %{buildroot}/usr/share/cockpit/selinux
rm -fr %{buildroot}/usr/share/cockpit/subscriptions
rm -fr %{buildroot}/usr/share/cockpit/subscriptions
install -m 0644 -D tools/cockpit.clear.pam %{buildroot}/usr/share/pam.d/cockpit
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cockpit-bridge

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/cockpit-tempfiles.conf

%files data
%defattr(-,root,root,-)
/usr/share/cockpit/base1/cockpit.js.gz
/usr/share/cockpit/base1/manifest.json
/usr/share/cockpit/base1/po.cs.js.gz
/usr/share/cockpit/base1/po.de.js.gz
/usr/share/cockpit/base1/po.es.js.gz
/usr/share/cockpit/base1/po.fi.js.gz
/usr/share/cockpit/base1/po.fr.js.gz
/usr/share/cockpit/base1/po.he.js.gz
/usr/share/cockpit/base1/po.it.js.gz
/usr/share/cockpit/base1/po.ja.js.gz
/usr/share/cockpit/base1/po.ka.js.gz
/usr/share/cockpit/base1/po.ko.js.gz
/usr/share/cockpit/base1/po.nb_NO.js.gz
/usr/share/cockpit/base1/po.nl.js.gz
/usr/share/cockpit/base1/po.pl.js.gz
/usr/share/cockpit/base1/po.pt_BR.js.gz
/usr/share/cockpit/base1/po.ru.js.gz
/usr/share/cockpit/base1/po.sk.js.gz
/usr/share/cockpit/base1/po.sv.js.gz
/usr/share/cockpit/base1/po.tr.js.gz
/usr/share/cockpit/base1/po.uk.js.gz
/usr/share/cockpit/base1/po.zh_CN.js.gz
/usr/share/cockpit/base1/po.zh_TW.js.gz
/usr/share/cockpit/branding/arch/apple-touch-icon.png
/usr/share/cockpit/branding/arch/branding.css
/usr/share/cockpit/branding/arch/favicon.ico
/usr/share/cockpit/branding/arch/logo.png
/usr/share/cockpit/branding/centos/apple-touch-icon.png
/usr/share/cockpit/branding/centos/branding.css
/usr/share/cockpit/branding/centos/favicon.ico
/usr/share/cockpit/branding/centos/logo.png
/usr/share/cockpit/branding/debian/branding.css
/usr/share/cockpit/branding/debian/favicon.ico
/usr/share/cockpit/branding/debian/logo.png
/usr/share/cockpit/branding/default/apple-touch-icon.png
/usr/share/cockpit/branding/default/bg-plain.jpg
/usr/share/cockpit/branding/default/brand-large.png
/usr/share/cockpit/branding/default/branding.css
/usr/share/cockpit/branding/default/favicon.ico
/usr/share/cockpit/branding/default/logo.png
/usr/share/cockpit/branding/fedora/apple-touch-icon.png
/usr/share/cockpit/branding/fedora/branding.css
/usr/share/cockpit/branding/fedora/favicon.ico
/usr/share/cockpit/branding/fedora/logo.png
/usr/share/cockpit/branding/kubernetes/branding.css
/usr/share/cockpit/branding/opensuse/branding.css
/usr/share/cockpit/branding/opensuse/default-1920x1200.jpg
/usr/share/cockpit/branding/opensuse/favicon.ico
/usr/share/cockpit/branding/opensuse/square-hicolor.svg
/usr/share/cockpit/branding/registry/branding.css
/usr/share/cockpit/branding/rhel/apple-touch-icon.png
/usr/share/cockpit/branding/rhel/branding.css
/usr/share/cockpit/branding/rhel/favicon.ico
/usr/share/cockpit/branding/rhel/logo.png
/usr/share/cockpit/branding/scientific/apple-touch-icon.png
/usr/share/cockpit/branding/scientific/branding.css
/usr/share/cockpit/branding/scientific/favicon.ico
/usr/share/cockpit/branding/scientific/logo.png
/usr/share/cockpit/branding/ubuntu/branding.css
/usr/share/cockpit/branding/ubuntu/favicon.ico
/usr/share/cockpit/branding/ubuntu/logo.png
/usr/share/cockpit/kdump/index.html
/usr/share/cockpit/kdump/kdump.css.gz
/usr/share/cockpit/kdump/kdump.js.LICENSE.txt.gz
/usr/share/cockpit/kdump/kdump.js.gz
/usr/share/cockpit/kdump/manifest.json
/usr/share/cockpit/kdump/po.cs.js.gz
/usr/share/cockpit/kdump/po.de.js.gz
/usr/share/cockpit/kdump/po.es.js.gz
/usr/share/cockpit/kdump/po.fi.js.gz
/usr/share/cockpit/kdump/po.fr.js.gz
/usr/share/cockpit/kdump/po.he.js.gz
/usr/share/cockpit/kdump/po.it.js.gz
/usr/share/cockpit/kdump/po.ja.js.gz
/usr/share/cockpit/kdump/po.ka.js.gz
/usr/share/cockpit/kdump/po.ko.js.gz
/usr/share/cockpit/kdump/po.nb_NO.js.gz
/usr/share/cockpit/kdump/po.nl.js.gz
/usr/share/cockpit/kdump/po.pl.js.gz
/usr/share/cockpit/kdump/po.pt_BR.js.gz
/usr/share/cockpit/kdump/po.ru.js.gz
/usr/share/cockpit/kdump/po.sk.js.gz
/usr/share/cockpit/kdump/po.sv.js.gz
/usr/share/cockpit/kdump/po.tr.js.gz
/usr/share/cockpit/kdump/po.uk.js.gz
/usr/share/cockpit/kdump/po.zh_CN.js.gz
/usr/share/cockpit/kdump/po.zh_TW.js.gz
/usr/share/cockpit/metrics/index.css.gz
/usr/share/cockpit/metrics/index.html
/usr/share/cockpit/metrics/index.js.LICENSE.txt.gz
/usr/share/cockpit/metrics/index.js.gz
/usr/share/cockpit/metrics/manifest.json
/usr/share/cockpit/metrics/po.cs.js.gz
/usr/share/cockpit/metrics/po.de.js.gz
/usr/share/cockpit/metrics/po.es.js.gz
/usr/share/cockpit/metrics/po.fi.js.gz
/usr/share/cockpit/metrics/po.fr.js.gz
/usr/share/cockpit/metrics/po.he.js.gz
/usr/share/cockpit/metrics/po.it.js.gz
/usr/share/cockpit/metrics/po.ja.js.gz
/usr/share/cockpit/metrics/po.ka.js.gz
/usr/share/cockpit/metrics/po.ko.js.gz
/usr/share/cockpit/metrics/po.nb_NO.js.gz
/usr/share/cockpit/metrics/po.nl.js.gz
/usr/share/cockpit/metrics/po.pl.js.gz
/usr/share/cockpit/metrics/po.pt_BR.js.gz
/usr/share/cockpit/metrics/po.ru.js.gz
/usr/share/cockpit/metrics/po.sk.js.gz
/usr/share/cockpit/metrics/po.sv.js.gz
/usr/share/cockpit/metrics/po.tr.js.gz
/usr/share/cockpit/metrics/po.uk.js.gz
/usr/share/cockpit/metrics/po.zh_CN.js.gz
/usr/share/cockpit/metrics/po.zh_TW.js.gz
/usr/share/cockpit/motd/inactive.motd
/usr/share/cockpit/motd/update-motd
/usr/share/cockpit/networkmanager/firewall.css.gz
/usr/share/cockpit/networkmanager/firewall.html
/usr/share/cockpit/networkmanager/firewall.js.LICENSE.txt.gz
/usr/share/cockpit/networkmanager/firewall.js.gz
/usr/share/cockpit/networkmanager/index.html
/usr/share/cockpit/networkmanager/manifest.json
/usr/share/cockpit/networkmanager/network.css.gz
/usr/share/cockpit/networkmanager/network.js.LICENSE.txt.gz
/usr/share/cockpit/networkmanager/network.js.gz
/usr/share/cockpit/networkmanager/po.cs.js.gz
/usr/share/cockpit/networkmanager/po.de.js.gz
/usr/share/cockpit/networkmanager/po.es.js.gz
/usr/share/cockpit/networkmanager/po.fi.js.gz
/usr/share/cockpit/networkmanager/po.fr.js.gz
/usr/share/cockpit/networkmanager/po.he.js.gz
/usr/share/cockpit/networkmanager/po.it.js.gz
/usr/share/cockpit/networkmanager/po.ja.js.gz
/usr/share/cockpit/networkmanager/po.ka.js.gz
/usr/share/cockpit/networkmanager/po.ko.js.gz
/usr/share/cockpit/networkmanager/po.nb_NO.js.gz
/usr/share/cockpit/networkmanager/po.nl.js.gz
/usr/share/cockpit/networkmanager/po.pl.js.gz
/usr/share/cockpit/networkmanager/po.pt_BR.js.gz
/usr/share/cockpit/networkmanager/po.ru.js.gz
/usr/share/cockpit/networkmanager/po.sk.js.gz
/usr/share/cockpit/networkmanager/po.sv.js.gz
/usr/share/cockpit/networkmanager/po.tr.js.gz
/usr/share/cockpit/networkmanager/po.uk.js.gz
/usr/share/cockpit/networkmanager/po.zh_CN.js.gz
/usr/share/cockpit/networkmanager/po.zh_TW.js.gz
/usr/share/cockpit/shell/images/bg-plain.jpg
/usr/share/cockpit/shell/images/cockpit-icon.svg
/usr/share/cockpit/shell/images/server-error.png
/usr/share/cockpit/shell/images/server-large.png
/usr/share/cockpit/shell/images/server-small.png
/usr/share/cockpit/shell/index.css.gz
/usr/share/cockpit/shell/index.html
/usr/share/cockpit/shell/index.js.LICENSE.txt.gz
/usr/share/cockpit/shell/index.js.gz
/usr/share/cockpit/shell/manifest.json
/usr/share/cockpit/shell/po.cs.js.gz
/usr/share/cockpit/shell/po.de.js.gz
/usr/share/cockpit/shell/po.es.js.gz
/usr/share/cockpit/shell/po.fi.js.gz
/usr/share/cockpit/shell/po.fr.js.gz
/usr/share/cockpit/shell/po.he.js.gz
/usr/share/cockpit/shell/po.it.js.gz
/usr/share/cockpit/shell/po.ja.js.gz
/usr/share/cockpit/shell/po.ka.js.gz
/usr/share/cockpit/shell/po.ko.js.gz
/usr/share/cockpit/shell/po.nb_NO.js.gz
/usr/share/cockpit/shell/po.nl.js.gz
/usr/share/cockpit/shell/po.pl.js.gz
/usr/share/cockpit/shell/po.pt_BR.js.gz
/usr/share/cockpit/shell/po.ru.js.gz
/usr/share/cockpit/shell/po.sk.js.gz
/usr/share/cockpit/shell/po.sv.js.gz
/usr/share/cockpit/shell/po.tr.js.gz
/usr/share/cockpit/shell/po.uk.js.gz
/usr/share/cockpit/shell/po.zh_CN.js.gz
/usr/share/cockpit/shell/po.zh_TW.js.gz
/usr/share/cockpit/shell/shell.html
/usr/share/cockpit/sosreport/index.html
/usr/share/cockpit/sosreport/manifest.json
/usr/share/cockpit/sosreport/po.cs.js.gz
/usr/share/cockpit/sosreport/po.de.js.gz
/usr/share/cockpit/sosreport/po.es.js.gz
/usr/share/cockpit/sosreport/po.fi.js.gz
/usr/share/cockpit/sosreport/po.fr.js.gz
/usr/share/cockpit/sosreport/po.he.js.gz
/usr/share/cockpit/sosreport/po.it.js.gz
/usr/share/cockpit/sosreport/po.ja.js.gz
/usr/share/cockpit/sosreport/po.ka.js.gz
/usr/share/cockpit/sosreport/po.ko.js.gz
/usr/share/cockpit/sosreport/po.nb_NO.js.gz
/usr/share/cockpit/sosreport/po.nl.js.gz
/usr/share/cockpit/sosreport/po.pl.js.gz
/usr/share/cockpit/sosreport/po.pt_BR.js.gz
/usr/share/cockpit/sosreport/po.ru.js.gz
/usr/share/cockpit/sosreport/po.sk.js.gz
/usr/share/cockpit/sosreport/po.sv.js.gz
/usr/share/cockpit/sosreport/po.tr.js.gz
/usr/share/cockpit/sosreport/po.uk.js.gz
/usr/share/cockpit/sosreport/po.zh_CN.js.gz
/usr/share/cockpit/sosreport/po.zh_TW.js.gz
/usr/share/cockpit/sosreport/sosreport.css.gz
/usr/share/cockpit/sosreport/sosreport.js.LICENSE.txt.gz
/usr/share/cockpit/sosreport/sosreport.js.gz
/usr/share/cockpit/sosreport/sosreport.png
/usr/share/cockpit/ssh/manifest.json
/usr/share/cockpit/static/fonts/RedHatDisplay-Black.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-BlackItalic.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-Bold.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-BoldItalic.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-Italic.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-Medium.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-MediumItalic.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-Regular.woff2
/usr/share/cockpit/static/fonts/RedHatMono-Bold.woff2
/usr/share/cockpit/static/fonts/RedHatMono-BoldItalic.woff2
/usr/share/cockpit/static/fonts/RedHatMono-Italic.woff2
/usr/share/cockpit/static/fonts/RedHatMono-Medium.woff2
/usr/share/cockpit/static/fonts/RedHatMono-MediumItalic.woff2
/usr/share/cockpit/static/fonts/RedHatMono-Regular.woff2
/usr/share/cockpit/static/fonts/RedHatText-Bold.woff2
/usr/share/cockpit/static/fonts/RedHatText-BoldItalic.woff2
/usr/share/cockpit/static/fonts/RedHatText-Italic.woff2
/usr/share/cockpit/static/fonts/RedHatText-Medium.woff2
/usr/share/cockpit/static/fonts/RedHatText-MediumItalic.woff2
/usr/share/cockpit/static/fonts/RedHatText-Regular.woff2
/usr/share/cockpit/static/login.css
/usr/share/cockpit/static/login.html
/usr/share/cockpit/static/login.js
/usr/share/cockpit/static/manifest.json
/usr/share/cockpit/static/po.cs.js
/usr/share/cockpit/static/po.de.js
/usr/share/cockpit/static/po.es.js
/usr/share/cockpit/static/po.fi.js
/usr/share/cockpit/static/po.fr.js
/usr/share/cockpit/static/po.he.js
/usr/share/cockpit/static/po.it.js
/usr/share/cockpit/static/po.ja.js
/usr/share/cockpit/static/po.ka.js
/usr/share/cockpit/static/po.ko.js
/usr/share/cockpit/static/po.nb_NO.js
/usr/share/cockpit/static/po.nl.js
/usr/share/cockpit/static/po.pl.js
/usr/share/cockpit/static/po.pt_BR.js
/usr/share/cockpit/static/po.ru.js
/usr/share/cockpit/static/po.sk.js
/usr/share/cockpit/static/po.sv.js
/usr/share/cockpit/static/po.tr.js
/usr/share/cockpit/static/po.uk.js
/usr/share/cockpit/static/po.zh_CN.js
/usr/share/cockpit/static/po.zh_TW.js
/usr/share/cockpit/storaged/images/storage-array.png
/usr/share/cockpit/storaged/images/storage-disk.png
/usr/share/cockpit/storaged/index.html
/usr/share/cockpit/storaged/manifest.json
/usr/share/cockpit/storaged/po.cs.js.gz
/usr/share/cockpit/storaged/po.de.js.gz
/usr/share/cockpit/storaged/po.es.js.gz
/usr/share/cockpit/storaged/po.fi.js.gz
/usr/share/cockpit/storaged/po.fr.js.gz
/usr/share/cockpit/storaged/po.he.js.gz
/usr/share/cockpit/storaged/po.it.js.gz
/usr/share/cockpit/storaged/po.ja.js.gz
/usr/share/cockpit/storaged/po.ka.js.gz
/usr/share/cockpit/storaged/po.ko.js.gz
/usr/share/cockpit/storaged/po.nb_NO.js.gz
/usr/share/cockpit/storaged/po.nl.js.gz
/usr/share/cockpit/storaged/po.pl.js.gz
/usr/share/cockpit/storaged/po.pt_BR.js.gz
/usr/share/cockpit/storaged/po.ru.js.gz
/usr/share/cockpit/storaged/po.sk.js.gz
/usr/share/cockpit/storaged/po.sv.js.gz
/usr/share/cockpit/storaged/po.tr.js.gz
/usr/share/cockpit/storaged/po.uk.js.gz
/usr/share/cockpit/storaged/po.zh_CN.js.gz
/usr/share/cockpit/storaged/po.zh_TW.js.gz
/usr/share/cockpit/storaged/storage.css.gz
/usr/share/cockpit/storaged/storage.js.LICENSE.txt.gz
/usr/share/cockpit/storaged/storage.js.gz
/usr/share/cockpit/systemd/hwinfo.css.gz
/usr/share/cockpit/systemd/hwinfo.html
/usr/share/cockpit/systemd/hwinfo.js.LICENSE.txt.gz
/usr/share/cockpit/systemd/hwinfo.js.gz
/usr/share/cockpit/systemd/index.html
/usr/share/cockpit/systemd/logs.css.gz
/usr/share/cockpit/systemd/logs.html
/usr/share/cockpit/systemd/logs.js.LICENSE.txt.gz
/usr/share/cockpit/systemd/logs.js.gz
/usr/share/cockpit/systemd/manifest.json
/usr/share/cockpit/systemd/overview.css.gz
/usr/share/cockpit/systemd/overview.js.LICENSE.txt.gz
/usr/share/cockpit/systemd/overview.js.gz
/usr/share/cockpit/systemd/po.cs.js.gz
/usr/share/cockpit/systemd/po.de.js.gz
/usr/share/cockpit/systemd/po.es.js.gz
/usr/share/cockpit/systemd/po.fi.js.gz
/usr/share/cockpit/systemd/po.fr.js.gz
/usr/share/cockpit/systemd/po.he.js.gz
/usr/share/cockpit/systemd/po.it.js.gz
/usr/share/cockpit/systemd/po.ja.js.gz
/usr/share/cockpit/systemd/po.ka.js.gz
/usr/share/cockpit/systemd/po.ko.js.gz
/usr/share/cockpit/systemd/po.nb_NO.js.gz
/usr/share/cockpit/systemd/po.nl.js.gz
/usr/share/cockpit/systemd/po.pl.js.gz
/usr/share/cockpit/systemd/po.pt_BR.js.gz
/usr/share/cockpit/systemd/po.ru.js.gz
/usr/share/cockpit/systemd/po.sk.js.gz
/usr/share/cockpit/systemd/po.sv.js.gz
/usr/share/cockpit/systemd/po.tr.js.gz
/usr/share/cockpit/systemd/po.uk.js.gz
/usr/share/cockpit/systemd/po.zh_CN.js.gz
/usr/share/cockpit/systemd/po.zh_TW.js.gz
/usr/share/cockpit/systemd/services.css.gz
/usr/share/cockpit/systemd/services.html
/usr/share/cockpit/systemd/services.js.LICENSE.txt.gz
/usr/share/cockpit/systemd/services.js.gz
/usr/share/cockpit/systemd/terminal.css.gz
/usr/share/cockpit/systemd/terminal.html
/usr/share/cockpit/systemd/terminal.js.LICENSE.txt.gz
/usr/share/cockpit/systemd/terminal.js.gz
/usr/share/cockpit/tuned/manifest.json
/usr/share/cockpit/tuned/performance.css.gz
/usr/share/cockpit/tuned/performance.js.LICENSE.txt.gz
/usr/share/cockpit/tuned/performance.js.gz
/usr/share/cockpit/tuned/po.cs.js.gz
/usr/share/cockpit/tuned/po.de.js.gz
/usr/share/cockpit/tuned/po.es.js.gz
/usr/share/cockpit/tuned/po.fi.js.gz
/usr/share/cockpit/tuned/po.fr.js.gz
/usr/share/cockpit/tuned/po.he.js.gz
/usr/share/cockpit/tuned/po.it.js.gz
/usr/share/cockpit/tuned/po.ja.js.gz
/usr/share/cockpit/tuned/po.ka.js.gz
/usr/share/cockpit/tuned/po.ko.js.gz
/usr/share/cockpit/tuned/po.nb_NO.js.gz
/usr/share/cockpit/tuned/po.nl.js.gz
/usr/share/cockpit/tuned/po.pl.js.gz
/usr/share/cockpit/tuned/po.pt_BR.js.gz
/usr/share/cockpit/tuned/po.ru.js.gz
/usr/share/cockpit/tuned/po.sk.js.gz
/usr/share/cockpit/tuned/po.sv.js.gz
/usr/share/cockpit/tuned/po.tr.js.gz
/usr/share/cockpit/tuned/po.uk.js.gz
/usr/share/cockpit/tuned/po.zh_CN.js.gz
/usr/share/cockpit/tuned/po.zh_TW.js.gz
/usr/share/cockpit/users/index.html
/usr/share/cockpit/users/manifest.json
/usr/share/cockpit/users/po.cs.js.gz
/usr/share/cockpit/users/po.de.js.gz
/usr/share/cockpit/users/po.es.js.gz
/usr/share/cockpit/users/po.fi.js.gz
/usr/share/cockpit/users/po.fr.js.gz
/usr/share/cockpit/users/po.he.js.gz
/usr/share/cockpit/users/po.it.js.gz
/usr/share/cockpit/users/po.ja.js.gz
/usr/share/cockpit/users/po.ka.js.gz
/usr/share/cockpit/users/po.ko.js.gz
/usr/share/cockpit/users/po.nb_NO.js.gz
/usr/share/cockpit/users/po.nl.js.gz
/usr/share/cockpit/users/po.pl.js.gz
/usr/share/cockpit/users/po.pt_BR.js.gz
/usr/share/cockpit/users/po.ru.js.gz
/usr/share/cockpit/users/po.sk.js.gz
/usr/share/cockpit/users/po.sv.js.gz
/usr/share/cockpit/users/po.tr.js.gz
/usr/share/cockpit/users/po.uk.js.gz
/usr/share/cockpit/users/po.zh_CN.js.gz
/usr/share/cockpit/users/po.zh_TW.js.gz
/usr/share/cockpit/users/users.css.gz
/usr/share/cockpit/users/users.js.LICENSE.txt.gz
/usr/share/cockpit/users/users.js.gz
/usr/share/metainfo/cockpit.appdata.xml
/usr/share/metainfo/org.cockpit-project.cockpit-kdump.metainfo.xml
/usr/share/metainfo/org.cockpit-project.cockpit-networkmanager.metainfo.xml
/usr/share/metainfo/org.cockpit-project.cockpit-selinux.metainfo.xml
/usr/share/metainfo/org.cockpit-project.cockpit-sosreport.metainfo.xml
/usr/share/metainfo/org.cockpit-project.cockpit-storaged.metainfo.xml
/usr/share/pam.d/cockpit
/usr/share/pixmaps/cockpit-sosreport.png
/usr/share/pixmaps/cockpit.png
/usr/share/polkit-1/actions/org.cockpit-project.cockpit-bridge.policy

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/cockpit/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/security/pam_cockpit_cert.so
/usr/lib64/security/pam_ssh_add.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/cockpit-askpass
/usr/libexec/cockpit-certificate-ensure
/usr/libexec/cockpit-certificate-helper
/usr/libexec/cockpit-client
/usr/libexec/cockpit-client.ui
/usr/libexec/cockpit-desktop
/usr/libexec/cockpit-pcp
/usr/libexec/cockpit-session
/usr/libexec/cockpit-ssh
/usr/libexec/cockpit-tls
/usr/libexec/cockpit-ws
/usr/libexec/cockpit-wsinstance-factory

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cockpit/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/cockpit/5267b8c02607adefda571a85283fcd110ae081ba
/usr/share/package-licenses/cockpit/63513188251d15fcdc716703fbee89be4a3a20e6
/usr/share/package-licenses/cockpit/762f77e8237dfc3015f3e4476035b80fee52af15
/usr/share/package-licenses/cockpit/7f6646d26563f0355dbbf5b6632ac2b48c0c98fb
/usr/share/package-licenses/cockpit/aba8f1f7a4b149e9eec362828f7e8d4bedd68378
/usr/share/package-licenses/cockpit/d3e41a6a93ea087e3c49d55d20451d23845153f0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cockpit-bridge.1
/usr/share/man/man1/cockpit-desktop.1
/usr/share/man/man1/cockpit.1
/usr/share/man/man5/cockpit.conf.5
/usr/share/man/man8/cockpit-tls.8
/usr/share/man/man8/cockpit-ws.8
/usr/share/man/man8/pam_ssh_add.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/cockpit-motd.service
/usr/lib/systemd/system/cockpit-session.socket
/usr/lib/systemd/system/cockpit-session@.service
/usr/lib/systemd/system/cockpit-wsinstance-http.service
/usr/lib/systemd/system/cockpit-wsinstance-http.socket
/usr/lib/systemd/system/cockpit-wsinstance-https-factory.socket
/usr/lib/systemd/system/cockpit-wsinstance-https-factory@.service
/usr/lib/systemd/system/cockpit-wsinstance-https@.service
/usr/lib/systemd/system/cockpit-wsinstance-https@.socket
/usr/lib/systemd/system/cockpit.service
/usr/lib/systemd/system/cockpit.socket
/usr/lib/systemd/system/system-cockpithttps.slice
