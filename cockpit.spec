#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cockpit
Version  : 216
Release  : 76
URL      : https://github.com/cockpit-project/cockpit/releases/download/216/cockpit-216.tar.xz
Source0  : https://github.com/cockpit-project/cockpit/releases/download/216/cockpit-216.tar.xz
Summary  : A systemd web based user interface for Linux servers
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 LGPL-2.1 LGPL-2.1+ MIT
Requires: cockpit-bin = %{version}-%{release}
Requires: cockpit-config = %{version}-%{release}
Requires: cockpit-data = %{version}-%{release}
Requires: cockpit-lib = %{version}-%{release}
Requires: cockpit-libexec = %{version}-%{release}
Requires: cockpit-license = %{version}-%{release}
Requires: cockpit-locales = %{version}-%{release}
Requires: cockpit-man = %{version}-%{release}
Requires: cockpit-services = %{version}-%{release}
Requires: glib-networking
Requires: polkit
Requires: sos
BuildRequires : Linux-PAM-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gettext
BuildRequires : glib-networking
BuildRequires : gnutls-dev
BuildRequires : go
BuildRequires : intltool
BuildRequires : krb5-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libssh)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : polkit
BuildRequires : sos
BuildRequires : util-linux
BuildRequires : xmlto
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


%package locales
Summary: locales components for the cockpit package.
Group: Default

%description locales
locales components for the cockpit package.


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
%setup -q -n cockpit-216
cd %{_builddir}/cockpit-216
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585926702
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --disable-pcp
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1585926702
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cockpit
cp %{_builddir}/cockpit-216/COPYING %{buildroot}/usr/share/package-licenses/cockpit/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/cockpit-216/COPYING.node %{buildroot}/usr/share/package-licenses/cockpit/fa3832069bea5dddee0594cb8e1b3aac37e04a32
cp %{_builddir}/cockpit-216/node_modules/bootstrap-datepicker/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/cockpit-216/node_modules/c3/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/b8a7b224c14ae490a5c53b6d7bbcb970177fbada
cp %{_builddir}/cockpit-216/node_modules/d3/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/23c26dbe97cdb9acbbdaf25808a25054e58bad3b
cp %{_builddir}/cockpit-216/node_modules/deep-equal/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/88b9d26be531a3fde8ee0dbed3153a75cb97f8ba
cp %{_builddir}/cockpit-216/node_modules/jquery-flot/LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/59d7f8d2480093f4a8c1a1f4d481f142176a0007
cp %{_builddir}/cockpit-216/node_modules/js-sha1/LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/bfe9c3e1924a8566cdd46938adb257c23ef43ff1
cp %{_builddir}/cockpit-216/node_modules/json-stable-stringify-without-jsonify/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/b2e68ce937c1f851926f7e10280cc93221d4f53c
cp %{_builddir}/cockpit-216/node_modules/moment/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/aab97739ef7d50750adbc9ffbfd1cbf9608eb678
cp %{_builddir}/cockpit-216/node_modules/mustache/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/8eec64b336c12d18faec369a7ccbaa2f2e325c80
cp %{_builddir}/cockpit-216/node_modules/patternfly-react/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/4afa2e9ea3eed023212af4d846f57ee5091fdcb8
cp %{_builddir}/cockpit-216/node_modules/patternfly/LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/4afa2e9ea3eed023212af4d846f57ee5091fdcb8
cp %{_builddir}/cockpit-216/node_modules/prop-types/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/87b0e4891924461043a2c240ea5ff70e761e04a1
cp %{_builddir}/cockpit-216/node_modules/qunit-tap/GPL-LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/e812f25edc98891abec39521a8f1b9c99457c395
cp %{_builddir}/cockpit-216/node_modules/qunit-tap/MIT-LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/0dc94fefdb96a580733d0dea1840c360968ce3e9
cp %{_builddir}/cockpit-216/node_modules/qunit/LICENSE.txt %{buildroot}/usr/share/package-licenses/cockpit/63bb5355e45b95926a176415104c0a90ea118955
cp %{_builddir}/cockpit-216/node_modules/react-bootstrap/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/56cfd5bbe171e0d7512df57aaaae03c06368308e
cp %{_builddir}/cockpit-216/node_modules/react-dom/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/1506731a652bba9abdf804ba3c95651ec5a68bdc
cp %{_builddir}/cockpit-216/node_modules/react/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/1506731a652bba9abdf804ba3c95651ec5a68bdc
cp %{_builddir}/cockpit-216/node_modules/redux-thunk/LICENSE.md %{buildroot}/usr/share/package-licenses/cockpit/8377bf32b37fd605c430e4fe198f840fd8fd36b7
cp %{_builddir}/cockpit-216/node_modules/redux/LICENSE.md %{buildroot}/usr/share/package-licenses/cockpit/8377bf32b37fd605c430e4fe198f840fd8fd36b7
cp %{_builddir}/cockpit-216/node_modules/remarkable/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/c1aefeeef90e1125f931eb1b5e1a6b7b69aa0851
cp %{_builddir}/cockpit-216/node_modules/throttle-debounce/LICENSE.md %{buildroot}/usr/share/package-licenses/cockpit/a3f347512649b3397fc1772a859556544088662a
cp %{_builddir}/cockpit-216/node_modules/uuid/LICENSE.md %{buildroot}/usr/share/package-licenses/cockpit/65e6555c3308c1d9538808d6c67e75924b8ad912
cp %{_builddir}/cockpit-216/node_modules/xterm/LICENSE %{buildroot}/usr/share/package-licenses/cockpit/c3e520d9acf9c9c7f67ca01a848883d79c802ef1
cp %{_builddir}/cockpit-216/src/bridge/mock-resource/system/cockpit/test-priority/sub/COPYING %{buildroot}/usr/share/package-licenses/cockpit/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/cockpit-216/src/bridge/mock-resource/system/cockpit/test/sub/COPYING %{buildroot}/usr/share/package-licenses/cockpit/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/cockpit-216/tools/debian/copyright %{buildroot}/usr/share/package-licenses/cockpit/94660bd4a2de82b710dafceaf81bcb889d2506c3
%make_install
%find_lang cockpit
## Remove excluded files
rm -f %{buildroot}/usr/lib/firewalld/services/cockpit.xml
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
/usr/bin/remotectl

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/cockpit-tempfiles.conf

%files data
%defattr(-,root,root,-)
/usr/share/cockpit/base1/cockpit.min.css.gz
/usr/share/cockpit/base1/cockpit.min.js.gz
/usr/share/cockpit/base1/fonts/fontawesome.woff
/usr/share/cockpit/base1/fonts/glyphicons.woff
/usr/share/cockpit/base1/fonts/patternfly.woff
/usr/share/cockpit/base1/jquery.min.js.gz
/usr/share/cockpit/base1/manifest.json
/usr/share/cockpit/base1/mustache.min.js.gz
/usr/share/cockpit/base1/patternfly.min.css.gz
/usr/share/cockpit/branding/centos/apple-touch-icon.png
/usr/share/cockpit/branding/centos/branding.css
/usr/share/cockpit/branding/centos/favicon.ico
/usr/share/cockpit/branding/centos/logo.png
/usr/share/cockpit/branding/debian/branding.css
/usr/share/cockpit/branding/debian/favicon.ico
/usr/share/cockpit/branding/debian/logo.png
/usr/share/cockpit/branding/default/apple-touch-icon.png
/usr/share/cockpit/branding/default/bg-login.jpg
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
/usr/share/cockpit/branding/registry/branding.css
/usr/share/cockpit/branding/rhel/apple-touch-icon.png
/usr/share/cockpit/branding/rhel/bg-login.jpg
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
/usr/share/cockpit/dashboard/dashboard.css.gz
/usr/share/cockpit/dashboard/dashboard.min.js.gz
/usr/share/cockpit/dashboard/index.html.gz
/usr/share/cockpit/dashboard/manifest.json
/usr/share/cockpit/dashboard/po.ca.js.gz
/usr/share/cockpit/dashboard/po.cs.js.gz
/usr/share/cockpit/dashboard/po.de.js.gz
/usr/share/cockpit/dashboard/po.es.js.gz
/usr/share/cockpit/dashboard/po.fr.js.gz
/usr/share/cockpit/dashboard/po.it.js.gz
/usr/share/cockpit/dashboard/po.ja.js.gz
/usr/share/cockpit/dashboard/po.js.gz
/usr/share/cockpit/dashboard/po.ko.js.gz
/usr/share/cockpit/dashboard/po.nl.js.gz
/usr/share/cockpit/dashboard/po.pl.js.gz
/usr/share/cockpit/dashboard/po.pt_BR.js.gz
/usr/share/cockpit/dashboard/po.ru.js.gz
/usr/share/cockpit/dashboard/po.sv.js.gz
/usr/share/cockpit/dashboard/po.uk.js.gz
/usr/share/cockpit/dashboard/po.zh_CN.js.gz
/usr/share/cockpit/dashboard/po.zh_TW.js.gz
/usr/share/cockpit/docker/console.html.gz
/usr/share/cockpit/docker/console.min.js.gz
/usr/share/cockpit/docker/docker.css.gz
/usr/share/cockpit/docker/docker.min.js.gz
/usr/share/cockpit/docker/images/drive-harddisk-symbolic.svg.gz
/usr/share/cockpit/docker/index.html.gz
/usr/share/cockpit/docker/manifest.json
/usr/share/cockpit/docker/po.ca.js.gz
/usr/share/cockpit/docker/po.cs.js.gz
/usr/share/cockpit/docker/po.de.js.gz
/usr/share/cockpit/docker/po.es.js.gz
/usr/share/cockpit/docker/po.fr.js.gz
/usr/share/cockpit/docker/po.it.js.gz
/usr/share/cockpit/docker/po.ja.js.gz
/usr/share/cockpit/docker/po.js.gz
/usr/share/cockpit/docker/po.ko.js.gz
/usr/share/cockpit/docker/po.nl.js.gz
/usr/share/cockpit/docker/po.pl.js.gz
/usr/share/cockpit/docker/po.pt_BR.js.gz
/usr/share/cockpit/docker/po.ru.js.gz
/usr/share/cockpit/docker/po.sv.js.gz
/usr/share/cockpit/docker/po.uk.js.gz
/usr/share/cockpit/docker/po.zh_CN.js.gz
/usr/share/cockpit/docker/po.zh_TW.js.gz
/usr/share/cockpit/kdump/index.html.gz
/usr/share/cockpit/kdump/kdump.css.gz
/usr/share/cockpit/kdump/kdump.min.js.gz
/usr/share/cockpit/kdump/manifest.json
/usr/share/cockpit/kdump/po.ca.js.gz
/usr/share/cockpit/kdump/po.cs.js.gz
/usr/share/cockpit/kdump/po.de.js.gz
/usr/share/cockpit/kdump/po.es.js.gz
/usr/share/cockpit/kdump/po.fr.js.gz
/usr/share/cockpit/kdump/po.it.js.gz
/usr/share/cockpit/kdump/po.ja.js.gz
/usr/share/cockpit/kdump/po.js.gz
/usr/share/cockpit/kdump/po.ko.js.gz
/usr/share/cockpit/kdump/po.nl.js.gz
/usr/share/cockpit/kdump/po.pl.js.gz
/usr/share/cockpit/kdump/po.pt_BR.js.gz
/usr/share/cockpit/kdump/po.ru.js.gz
/usr/share/cockpit/kdump/po.sv.js.gz
/usr/share/cockpit/kdump/po.uk.js.gz
/usr/share/cockpit/kdump/po.zh_CN.js.gz
/usr/share/cockpit/kdump/po.zh_TW.js.gz
/usr/share/cockpit/machines/index.html.gz
/usr/share/cockpit/machines/machines.css.gz
/usr/share/cockpit/machines/machines.min.js.gz
/usr/share/cockpit/machines/manifest.json
/usr/share/cockpit/machines/po.ca.js.gz
/usr/share/cockpit/machines/po.cs.js.gz
/usr/share/cockpit/machines/po.de.js.gz
/usr/share/cockpit/machines/po.es.js.gz
/usr/share/cockpit/machines/po.fr.js.gz
/usr/share/cockpit/machines/po.it.js.gz
/usr/share/cockpit/machines/po.ja.js.gz
/usr/share/cockpit/machines/po.js.gz
/usr/share/cockpit/machines/po.ko.js.gz
/usr/share/cockpit/machines/po.nl.js.gz
/usr/share/cockpit/machines/po.pl.js.gz
/usr/share/cockpit/machines/po.pt_BR.js.gz
/usr/share/cockpit/machines/po.ru.js.gz
/usr/share/cockpit/machines/po.sv.js.gz
/usr/share/cockpit/machines/po.uk.js.gz
/usr/share/cockpit/machines/po.zh_CN.js.gz
/usr/share/cockpit/machines/po.zh_TW.js.gz
/usr/share/cockpit/motd/inactive.motd
/usr/share/cockpit/motd/update-motd
/usr/share/cockpit/networkmanager/firewall.css.gz
/usr/share/cockpit/networkmanager/firewall.html.gz
/usr/share/cockpit/networkmanager/firewall.min.js.gz
/usr/share/cockpit/networkmanager/index.html.gz
/usr/share/cockpit/networkmanager/manifest.json
/usr/share/cockpit/networkmanager/network.css.gz
/usr/share/cockpit/networkmanager/network.min.js.gz
/usr/share/cockpit/networkmanager/po.ca.js.gz
/usr/share/cockpit/networkmanager/po.cs.js.gz
/usr/share/cockpit/networkmanager/po.de.js.gz
/usr/share/cockpit/networkmanager/po.es.js.gz
/usr/share/cockpit/networkmanager/po.fr.js.gz
/usr/share/cockpit/networkmanager/po.it.js.gz
/usr/share/cockpit/networkmanager/po.ja.js.gz
/usr/share/cockpit/networkmanager/po.js.gz
/usr/share/cockpit/networkmanager/po.ko.js.gz
/usr/share/cockpit/networkmanager/po.nl.js.gz
/usr/share/cockpit/networkmanager/po.pl.js.gz
/usr/share/cockpit/networkmanager/po.pt_BR.js.gz
/usr/share/cockpit/networkmanager/po.ru.js.gz
/usr/share/cockpit/networkmanager/po.sv.js.gz
/usr/share/cockpit/networkmanager/po.uk.js.gz
/usr/share/cockpit/networkmanager/po.zh_CN.js.gz
/usr/share/cockpit/networkmanager/po.zh_TW.js.gz
/usr/share/cockpit/shell/images/server-error.png
/usr/share/cockpit/shell/images/server-large.png
/usr/share/cockpit/shell/images/server-small.png
/usr/share/cockpit/shell/index.css.gz
/usr/share/cockpit/shell/index.html
/usr/share/cockpit/shell/index.min.js.gz
/usr/share/cockpit/shell/manifest.json
/usr/share/cockpit/shell/po.ca.js.gz
/usr/share/cockpit/shell/po.cs.js.gz
/usr/share/cockpit/shell/po.de.js.gz
/usr/share/cockpit/shell/po.es.js.gz
/usr/share/cockpit/shell/po.fr.js.gz
/usr/share/cockpit/shell/po.it.js.gz
/usr/share/cockpit/shell/po.ja.js.gz
/usr/share/cockpit/shell/po.js.gz
/usr/share/cockpit/shell/po.ko.js.gz
/usr/share/cockpit/shell/po.nl.js.gz
/usr/share/cockpit/shell/po.pl.js.gz
/usr/share/cockpit/shell/po.pt_BR.js.gz
/usr/share/cockpit/shell/po.ru.js.gz
/usr/share/cockpit/shell/po.sv.js.gz
/usr/share/cockpit/shell/po.uk.js.gz
/usr/share/cockpit/shell/po.zh_CN.js.gz
/usr/share/cockpit/shell/po.zh_TW.js.gz
/usr/share/cockpit/shell/shell.html.gz
/usr/share/cockpit/sosreport/index.html.gz
/usr/share/cockpit/sosreport/manifest.json
/usr/share/cockpit/sosreport/po.ca.js.gz
/usr/share/cockpit/sosreport/po.cs.js.gz
/usr/share/cockpit/sosreport/po.de.js.gz
/usr/share/cockpit/sosreport/po.es.js.gz
/usr/share/cockpit/sosreport/po.fr.js.gz
/usr/share/cockpit/sosreport/po.it.js.gz
/usr/share/cockpit/sosreport/po.ja.js.gz
/usr/share/cockpit/sosreport/po.js.gz
/usr/share/cockpit/sosreport/po.ko.js.gz
/usr/share/cockpit/sosreport/po.nl.js.gz
/usr/share/cockpit/sosreport/po.pl.js.gz
/usr/share/cockpit/sosreport/po.pt_BR.js.gz
/usr/share/cockpit/sosreport/po.ru.js.gz
/usr/share/cockpit/sosreport/po.sv.js.gz
/usr/share/cockpit/sosreport/po.uk.js.gz
/usr/share/cockpit/sosreport/po.zh_CN.js.gz
/usr/share/cockpit/sosreport/po.zh_TW.js.gz
/usr/share/cockpit/sosreport/sosreport.css.gz
/usr/share/cockpit/sosreport/sosreport.min.js.gz
/usr/share/cockpit/sosreport/sosreport.png
/usr/share/cockpit/ssh/manifest.json
/usr/share/cockpit/static/fonts/OpenSans-Bold-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-BoldItalic-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-ExtraBold-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-ExtraBoldItalic-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-Italic-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-Light-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-LightItalic-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-Regular-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-Semibold-webfont.woff
/usr/share/cockpit/static/fonts/OpenSans-SemiboldItalic-webfont.woff
/usr/share/cockpit/static/fonts/RedHatDisplay-Black.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-BlackItalic.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-Bold.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-BoldItalic.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-Italic.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-Medium.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-MediumItalic.woff2
/usr/share/cockpit/static/fonts/RedHatDisplay-Regular.woff2
/usr/share/cockpit/static/fonts/RedHatText-Bold.woff2
/usr/share/cockpit/static/fonts/RedHatText-BoldItalic.woff2
/usr/share/cockpit/static/fonts/RedHatText-Italic.woff2
/usr/share/cockpit/static/fonts/RedHatText-Medium.woff2
/usr/share/cockpit/static/fonts/RedHatText-MediumItalic.woff2
/usr/share/cockpit/static/fonts/RedHatText-Regular.woff2
/usr/share/cockpit/static/login.min.html
/usr/share/cockpit/static/login.po.ca.html
/usr/share/cockpit/static/login.po.cs.html
/usr/share/cockpit/static/login.po.de.html
/usr/share/cockpit/static/login.po.es.html
/usr/share/cockpit/static/login.po.fr.html
/usr/share/cockpit/static/login.po.html
/usr/share/cockpit/static/login.po.it.html
/usr/share/cockpit/static/login.po.ja.html
/usr/share/cockpit/static/login.po.ko.html
/usr/share/cockpit/static/login.po.nl.html
/usr/share/cockpit/static/login.po.pl.html
/usr/share/cockpit/static/login.po.pt_BR.html
/usr/share/cockpit/static/login.po.ru.html
/usr/share/cockpit/static/login.po.sv.html
/usr/share/cockpit/static/login.po.uk.html
/usr/share/cockpit/static/login.po.zh_CN.html
/usr/share/cockpit/static/login.po.zh_TW.html
/usr/share/cockpit/storaged/images/storage-array.png
/usr/share/cockpit/storaged/images/storage-disk.png
/usr/share/cockpit/storaged/index.html.gz
/usr/share/cockpit/storaged/manifest.json
/usr/share/cockpit/storaged/po.ca.js.gz
/usr/share/cockpit/storaged/po.cs.js.gz
/usr/share/cockpit/storaged/po.de.js.gz
/usr/share/cockpit/storaged/po.es.js.gz
/usr/share/cockpit/storaged/po.fr.js.gz
/usr/share/cockpit/storaged/po.it.js.gz
/usr/share/cockpit/storaged/po.ja.js.gz
/usr/share/cockpit/storaged/po.js.gz
/usr/share/cockpit/storaged/po.ko.js.gz
/usr/share/cockpit/storaged/po.nl.js.gz
/usr/share/cockpit/storaged/po.pl.js.gz
/usr/share/cockpit/storaged/po.pt_BR.js.gz
/usr/share/cockpit/storaged/po.ru.js.gz
/usr/share/cockpit/storaged/po.sv.js.gz
/usr/share/cockpit/storaged/po.uk.js.gz
/usr/share/cockpit/storaged/po.zh_CN.js.gz
/usr/share/cockpit/storaged/po.zh_TW.js.gz
/usr/share/cockpit/storaged/storage.css.gz
/usr/share/cockpit/storaged/storage.min.js.gz
/usr/share/cockpit/systemd/graphs.css.gz
/usr/share/cockpit/systemd/graphs.html.gz
/usr/share/cockpit/systemd/graphs.min.js.gz
/usr/share/cockpit/systemd/hwinfo.css.gz
/usr/share/cockpit/systemd/hwinfo.html.gz
/usr/share/cockpit/systemd/hwinfo.min.js.gz
/usr/share/cockpit/systemd/index.html.gz
/usr/share/cockpit/systemd/logs.css.gz
/usr/share/cockpit/systemd/logs.html.gz
/usr/share/cockpit/systemd/logs.min.js.gz
/usr/share/cockpit/systemd/manifest.json
/usr/share/cockpit/systemd/overview.css.gz
/usr/share/cockpit/systemd/overview.min.js.gz
/usr/share/cockpit/systemd/po.ca.js.gz
/usr/share/cockpit/systemd/po.cs.js.gz
/usr/share/cockpit/systemd/po.de.js.gz
/usr/share/cockpit/systemd/po.es.js.gz
/usr/share/cockpit/systemd/po.fr.js.gz
/usr/share/cockpit/systemd/po.it.js.gz
/usr/share/cockpit/systemd/po.ja.js.gz
/usr/share/cockpit/systemd/po.js.gz
/usr/share/cockpit/systemd/po.ko.js.gz
/usr/share/cockpit/systemd/po.nl.js.gz
/usr/share/cockpit/systemd/po.pl.js.gz
/usr/share/cockpit/systemd/po.pt_BR.js.gz
/usr/share/cockpit/systemd/po.ru.js.gz
/usr/share/cockpit/systemd/po.sv.js.gz
/usr/share/cockpit/systemd/po.uk.js.gz
/usr/share/cockpit/systemd/po.zh_CN.js.gz
/usr/share/cockpit/systemd/po.zh_TW.js.gz
/usr/share/cockpit/systemd/services.css.gz
/usr/share/cockpit/systemd/services.html.gz
/usr/share/cockpit/systemd/services.min.js.gz
/usr/share/cockpit/systemd/terminal.css.gz
/usr/share/cockpit/systemd/terminal.html.gz
/usr/share/cockpit/systemd/terminal.min.js.gz
/usr/share/cockpit/tuned/manifest.json
/usr/share/cockpit/tuned/performance.css.gz
/usr/share/cockpit/tuned/performance.min.js.gz
/usr/share/cockpit/tuned/po.ca.js.gz
/usr/share/cockpit/tuned/po.cs.js.gz
/usr/share/cockpit/tuned/po.de.js.gz
/usr/share/cockpit/tuned/po.es.js.gz
/usr/share/cockpit/tuned/po.fr.js.gz
/usr/share/cockpit/tuned/po.it.js.gz
/usr/share/cockpit/tuned/po.ja.js.gz
/usr/share/cockpit/tuned/po.js.gz
/usr/share/cockpit/tuned/po.ko.js.gz
/usr/share/cockpit/tuned/po.nl.js.gz
/usr/share/cockpit/tuned/po.pl.js.gz
/usr/share/cockpit/tuned/po.pt_BR.js.gz
/usr/share/cockpit/tuned/po.ru.js.gz
/usr/share/cockpit/tuned/po.sv.js.gz
/usr/share/cockpit/tuned/po.uk.js.gz
/usr/share/cockpit/tuned/po.zh_CN.js.gz
/usr/share/cockpit/tuned/po.zh_TW.js.gz
/usr/share/cockpit/users/index.html.gz
/usr/share/cockpit/users/manifest.json
/usr/share/cockpit/users/po.ca.js.gz
/usr/share/cockpit/users/po.cs.js.gz
/usr/share/cockpit/users/po.de.js.gz
/usr/share/cockpit/users/po.es.js.gz
/usr/share/cockpit/users/po.fr.js.gz
/usr/share/cockpit/users/po.it.js.gz
/usr/share/cockpit/users/po.ja.js.gz
/usr/share/cockpit/users/po.js.gz
/usr/share/cockpit/users/po.ko.js.gz
/usr/share/cockpit/users/po.nl.js.gz
/usr/share/cockpit/users/po.pl.js.gz
/usr/share/cockpit/users/po.pt_BR.js.gz
/usr/share/cockpit/users/po.ru.js.gz
/usr/share/cockpit/users/po.sv.js.gz
/usr/share/cockpit/users/po.uk.js.gz
/usr/share/cockpit/users/po.zh_CN.js.gz
/usr/share/cockpit/users/po.zh_TW.js.gz
/usr/share/cockpit/users/users.css.gz
/usr/share/cockpit/users/users.min.js.gz
/usr/share/metainfo/cockpit.appdata.xml
/usr/share/metainfo/org.cockpit-project.cockpit-docker.metainfo.xml
/usr/share/metainfo/org.cockpit-project.cockpit-kdump.metainfo.xml
/usr/share/metainfo/org.cockpit-project.cockpit-machines.metainfo.xml
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
/usr/libexec/cockpit-desktop
/usr/libexec/cockpit-session
/usr/libexec/cockpit-ssh
/usr/libexec/cockpit-tls
/usr/libexec/cockpit-ws
/usr/libexec/cockpit-wsinstance-factory

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cockpit/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/cockpit/0dc94fefdb96a580733d0dea1840c360968ce3e9
/usr/share/package-licenses/cockpit/1506731a652bba9abdf804ba3c95651ec5a68bdc
/usr/share/package-licenses/cockpit/23c26dbe97cdb9acbbdaf25808a25054e58bad3b
/usr/share/package-licenses/cockpit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/cockpit/4afa2e9ea3eed023212af4d846f57ee5091fdcb8
/usr/share/package-licenses/cockpit/56cfd5bbe171e0d7512df57aaaae03c06368308e
/usr/share/package-licenses/cockpit/59d7f8d2480093f4a8c1a1f4d481f142176a0007
/usr/share/package-licenses/cockpit/63bb5355e45b95926a176415104c0a90ea118955
/usr/share/package-licenses/cockpit/65e6555c3308c1d9538808d6c67e75924b8ad912
/usr/share/package-licenses/cockpit/8377bf32b37fd605c430e4fe198f840fd8fd36b7
/usr/share/package-licenses/cockpit/87b0e4891924461043a2c240ea5ff70e761e04a1
/usr/share/package-licenses/cockpit/88b9d26be531a3fde8ee0dbed3153a75cb97f8ba
/usr/share/package-licenses/cockpit/8eec64b336c12d18faec369a7ccbaa2f2e325c80
/usr/share/package-licenses/cockpit/94660bd4a2de82b710dafceaf81bcb889d2506c3
/usr/share/package-licenses/cockpit/a3f347512649b3397fc1772a859556544088662a
/usr/share/package-licenses/cockpit/aab97739ef7d50750adbc9ffbfd1cbf9608eb678
/usr/share/package-licenses/cockpit/b2e68ce937c1f851926f7e10280cc93221d4f53c
/usr/share/package-licenses/cockpit/b8a7b224c14ae490a5c53b6d7bbcb970177fbada
/usr/share/package-licenses/cockpit/bfe9c3e1924a8566cdd46938adb257c23ef43ff1
/usr/share/package-licenses/cockpit/c1aefeeef90e1125f931eb1b5e1a6b7b69aa0851
/usr/share/package-licenses/cockpit/c3e520d9acf9c9c7f67ca01a848883d79c802ef1
/usr/share/package-licenses/cockpit/e812f25edc98891abec39521a8f1b9c99457c395
/usr/share/package-licenses/cockpit/fa3832069bea5dddee0594cb8e1b3aac37e04a32

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cockpit-bridge.1
/usr/share/man/man1/cockpit-desktop.1
/usr/share/man/man1/cockpit.1
/usr/share/man/man5/cockpit.conf.5
/usr/share/man/man8/cockpit-tls.8
/usr/share/man/man8/cockpit-ws.8
/usr/share/man/man8/pam_cockpit_cert.8
/usr/share/man/man8/pam_ssh_add.8
/usr/share/man/man8/remotectl.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/cockpit-motd.service
/usr/lib/systemd/system/cockpit-wsinstance-http-redirect.service
/usr/lib/systemd/system/cockpit-wsinstance-http-redirect.socket
/usr/lib/systemd/system/cockpit-wsinstance-http.service
/usr/lib/systemd/system/cockpit-wsinstance-http.socket
/usr/lib/systemd/system/cockpit-wsinstance-https-factory.socket
/usr/lib/systemd/system/cockpit-wsinstance-https-factory@.service
/usr/lib/systemd/system/cockpit-wsinstance-https@.service
/usr/lib/systemd/system/cockpit-wsinstance-https@.socket
/usr/lib/systemd/system/cockpit.service
/usr/lib/systemd/system/cockpit.socket
/usr/lib/systemd/system/system-cockpithttps.slice

%files locales -f cockpit.lang
%defattr(-,root,root,-)

