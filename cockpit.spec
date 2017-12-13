#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cockpit
Version  : 157
Release  : 2
URL      : https://github.com/cockpit-project/cockpit/releases/download/157/cockpit-157.tar.xz
Source0  : https://github.com/cockpit-project/cockpit/releases/download/157/cockpit-157.tar.xz
Summary  : Empty Cockpit Machines
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause LGPL-2.1 LGPL-2.1+ MIT MPL-2.0
Requires: cockpit-bin
Requires: cockpit-config
Requires: cockpit-lib
Requires: cockpit-data
Requires: cockpit-doc
Requires: cockpit-locales
BuildRequires : Linux-PAM-dev
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gettext
BuildRequires : go
BuildRequires : intltool
BuildRequires : krb5-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libssh)
BuildRequires : pkgconfig(libssh_threads)
BuildRequires : pkgconfig(polkit-agent-1)
BuildRequires : pkgconfig(systemd)
BuildRequires : util-linux
BuildRequires : xmlto

%description
Empty cockpit-machines RPM

%package bin
Summary: bin components for the cockpit package.
Group: Binaries
Requires: cockpit-data
Requires: cockpit-config

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

%description doc
doc components for the cockpit package.


%package lib
Summary: lib components for the cockpit package.
Group: Libraries
Requires: cockpit-data

%description lib
lib components for the cockpit package.


%package locales
Summary: locales components for the cockpit package.
Group: Default

%description locales
locales components for the cockpit package.


%prep
%setup -q -n cockpit-157

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513189214
%configure --disable-static --disable-pcp
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1513189214
rm -rf %{buildroot}
%make_install
%find_lang cockpit

%files
%defattr(-,root,root,-)
%exclude /usr/lib/firewalld/services/cockpit.xml

%files bin
%defattr(-,root,root,-)
/usr/bin/cockpit-bridge
/usr/bin/remotectl
/usr/libexec/cockpit-askpass
/usr/libexec/cockpit-kube-auth
/usr/libexec/cockpit-kube-launch
/usr/libexec/cockpit-session
/usr/libexec/cockpit-ssh
/usr/libexec/cockpit-stub
/usr/libexec/cockpit-ws

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/cockpit.service
/usr/lib/systemd/system/cockpit.socket
/usr/lib/tmpfiles.d/cockpit-tempfiles.conf

%files data
%defattr(-,root,root,-)
/usr/share/applications/cockpit.desktop
/usr/share/cockpit/apps/apps.css.gz
/usr/share/cockpit/apps/apps.min.js.gz
/usr/share/cockpit/apps/default.png
/usr/share/cockpit/apps/index.html.gz
/usr/share/cockpit/apps/manifest.json
/usr/share/cockpit/apps/po.ca.js.gz
/usr/share/cockpit/apps/po.cs.js.gz
/usr/share/cockpit/apps/po.da.js.gz
/usr/share/cockpit/apps/po.de.js.gz
/usr/share/cockpit/apps/po.es.js.gz
/usr/share/cockpit/apps/po.fi.js.gz
/usr/share/cockpit/apps/po.fr.js.gz
/usr/share/cockpit/apps/po.hr.js.gz
/usr/share/cockpit/apps/po.hu.js.gz
/usr/share/cockpit/apps/po.ja.js.gz
/usr/share/cockpit/apps/po.js.gz
/usr/share/cockpit/apps/po.ko.js.gz
/usr/share/cockpit/apps/po.my.js.gz
/usr/share/cockpit/apps/po.nl.js.gz
/usr/share/cockpit/apps/po.pa.js.gz
/usr/share/cockpit/apps/po.pl.js.gz
/usr/share/cockpit/apps/po.pt.js.gz
/usr/share/cockpit/apps/po.pt_BR.js.gz
/usr/share/cockpit/apps/po.tr.js.gz
/usr/share/cockpit/apps/po.uk.js.gz
/usr/share/cockpit/apps/po.zh_CN.js.gz
/usr/share/cockpit/base1/bundle.min.js.gz
/usr/share/cockpit/base1/cockpit.min.css.gz
/usr/share/cockpit/base1/cockpit.min.js.gz
/usr/share/cockpit/base1/fonts/fontawesome.woff
/usr/share/cockpit/base1/fonts/glyphicons.woff
/usr/share/cockpit/base1/fonts/patternfly.woff
/usr/share/cockpit/base1/jquery.min.js.gz
/usr/share/cockpit/base1/manifest.json
/usr/share/cockpit/base1/mustache.min.js.gz
/usr/share/cockpit/base1/patternfly.min.css.gz
/usr/share/cockpit/base1/require.min.js.gz
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
/usr/share/cockpit/branding/ubuntu/branding.css
/usr/share/cockpit/branding/ubuntu/favicon.ico
/usr/share/cockpit/branding/ubuntu/logo.png
/usr/share/cockpit/dashboard/dashboard.min.js.gz
/usr/share/cockpit/dashboard/index.html.gz
/usr/share/cockpit/dashboard/manifest.json
/usr/share/cockpit/dashboard/po.ca.js.gz
/usr/share/cockpit/dashboard/po.cs.js.gz
/usr/share/cockpit/dashboard/po.da.js.gz
/usr/share/cockpit/dashboard/po.de.js.gz
/usr/share/cockpit/dashboard/po.es.js.gz
/usr/share/cockpit/dashboard/po.fi.js.gz
/usr/share/cockpit/dashboard/po.fr.js.gz
/usr/share/cockpit/dashboard/po.hr.js.gz
/usr/share/cockpit/dashboard/po.hu.js.gz
/usr/share/cockpit/dashboard/po.ja.js.gz
/usr/share/cockpit/dashboard/po.js.gz
/usr/share/cockpit/dashboard/po.ko.js.gz
/usr/share/cockpit/dashboard/po.my.js.gz
/usr/share/cockpit/dashboard/po.nl.js.gz
/usr/share/cockpit/dashboard/po.pa.js.gz
/usr/share/cockpit/dashboard/po.pl.js.gz
/usr/share/cockpit/dashboard/po.pt.js.gz
/usr/share/cockpit/dashboard/po.pt_BR.js.gz
/usr/share/cockpit/dashboard/po.tr.js.gz
/usr/share/cockpit/dashboard/po.uk.js.gz
/usr/share/cockpit/dashboard/po.zh_CN.js.gz
/usr/share/cockpit/docker/console.html.gz
/usr/share/cockpit/docker/console.min.js.gz
/usr/share/cockpit/docker/docker.css.gz
/usr/share/cockpit/docker/docker.min.js.gz
/usr/share/cockpit/docker/images/drive-harddisk-symbolic.svg.gz
/usr/share/cockpit/docker/index.html.gz
/usr/share/cockpit/docker/manifest.json
/usr/share/cockpit/docker/po.ca.js.gz
/usr/share/cockpit/docker/po.cs.js.gz
/usr/share/cockpit/docker/po.da.js.gz
/usr/share/cockpit/docker/po.de.js.gz
/usr/share/cockpit/docker/po.es.js.gz
/usr/share/cockpit/docker/po.fi.js.gz
/usr/share/cockpit/docker/po.fr.js.gz
/usr/share/cockpit/docker/po.hr.js.gz
/usr/share/cockpit/docker/po.hu.js.gz
/usr/share/cockpit/docker/po.ja.js.gz
/usr/share/cockpit/docker/po.js.gz
/usr/share/cockpit/docker/po.ko.js.gz
/usr/share/cockpit/docker/po.my.js.gz
/usr/share/cockpit/docker/po.nl.js.gz
/usr/share/cockpit/docker/po.pa.js.gz
/usr/share/cockpit/docker/po.pl.js.gz
/usr/share/cockpit/docker/po.pt.js.gz
/usr/share/cockpit/docker/po.pt_BR.js.gz
/usr/share/cockpit/docker/po.tr.js.gz
/usr/share/cockpit/docker/po.uk.js.gz
/usr/share/cockpit/docker/po.zh_CN.js.gz
/usr/share/cockpit/issue/active.issue
/usr/share/cockpit/issue/inactive.issue
/usr/share/cockpit/kdump/index.html.gz
/usr/share/cockpit/kdump/kdump.css.gz
/usr/share/cockpit/kdump/kdump.min.js.gz
/usr/share/cockpit/kdump/manifest.json
/usr/share/cockpit/kdump/po.ca.js.gz
/usr/share/cockpit/kdump/po.cs.js.gz
/usr/share/cockpit/kdump/po.da.js.gz
/usr/share/cockpit/kdump/po.de.js.gz
/usr/share/cockpit/kdump/po.es.js.gz
/usr/share/cockpit/kdump/po.fi.js.gz
/usr/share/cockpit/kdump/po.fr.js.gz
/usr/share/cockpit/kdump/po.hr.js.gz
/usr/share/cockpit/kdump/po.hu.js.gz
/usr/share/cockpit/kdump/po.ja.js.gz
/usr/share/cockpit/kdump/po.js.gz
/usr/share/cockpit/kdump/po.ko.js.gz
/usr/share/cockpit/kdump/po.my.js.gz
/usr/share/cockpit/kdump/po.nl.js.gz
/usr/share/cockpit/kdump/po.pa.js.gz
/usr/share/cockpit/kdump/po.pl.js.gz
/usr/share/cockpit/kdump/po.pt.js.gz
/usr/share/cockpit/kdump/po.pt_BR.js.gz
/usr/share/cockpit/kdump/po.tr.js.gz
/usr/share/cockpit/kdump/po.uk.js.gz
/usr/share/cockpit/kdump/po.zh_CN.js.gz
/usr/share/cockpit/kubernetes/index.html.gz
/usr/share/cockpit/kubernetes/kubernetes.css.gz
/usr/share/cockpit/kubernetes/kubernetes.min.js.gz
/usr/share/cockpit/kubernetes/manifest.json
/usr/share/cockpit/kubernetes/override.json
/usr/share/cockpit/kubernetes/po.ca.js.gz
/usr/share/cockpit/kubernetes/po.cs.js.gz
/usr/share/cockpit/kubernetes/po.da.js.gz
/usr/share/cockpit/kubernetes/po.de.js.gz
/usr/share/cockpit/kubernetes/po.es.js.gz
/usr/share/cockpit/kubernetes/po.fi.js.gz
/usr/share/cockpit/kubernetes/po.fr.js.gz
/usr/share/cockpit/kubernetes/po.hr.js.gz
/usr/share/cockpit/kubernetes/po.hu.js.gz
/usr/share/cockpit/kubernetes/po.ja.js.gz
/usr/share/cockpit/kubernetes/po.js.gz
/usr/share/cockpit/kubernetes/po.ko.js.gz
/usr/share/cockpit/kubernetes/po.my.js.gz
/usr/share/cockpit/kubernetes/po.nl.js.gz
/usr/share/cockpit/kubernetes/po.pa.js.gz
/usr/share/cockpit/kubernetes/po.pl.js.gz
/usr/share/cockpit/kubernetes/po.pt.js.gz
/usr/share/cockpit/kubernetes/po.pt_BR.js.gz
/usr/share/cockpit/kubernetes/po.tr.js.gz
/usr/share/cockpit/kubernetes/po.uk.js.gz
/usr/share/cockpit/kubernetes/po.zh_CN.js.gz
/usr/share/cockpit/kubernetes/registry.css.gz
/usr/share/cockpit/kubernetes/registry.html.gz
/usr/share/cockpit/kubernetes/registry.min.js.gz
/usr/share/cockpit/machines/base.css
/usr/share/cockpit/machines/index.html.gz
/usr/share/cockpit/machines/machines.css.gz
/usr/share/cockpit/machines/machines.min.js.gz
/usr/share/cockpit/machines/manifest.json
/usr/share/cockpit/machines/po.ca.js.gz
/usr/share/cockpit/machines/po.cs.js.gz
/usr/share/cockpit/machines/po.da.js.gz
/usr/share/cockpit/machines/po.de.js.gz
/usr/share/cockpit/machines/po.es.js.gz
/usr/share/cockpit/machines/po.fi.js.gz
/usr/share/cockpit/machines/po.fr.js.gz
/usr/share/cockpit/machines/po.hr.js.gz
/usr/share/cockpit/machines/po.hu.js.gz
/usr/share/cockpit/machines/po.ja.js.gz
/usr/share/cockpit/machines/po.js.gz
/usr/share/cockpit/machines/po.ko.js.gz
/usr/share/cockpit/machines/po.my.js.gz
/usr/share/cockpit/machines/po.nl.js.gz
/usr/share/cockpit/machines/po.pa.js.gz
/usr/share/cockpit/machines/po.pl.js.gz
/usr/share/cockpit/machines/po.pt.js.gz
/usr/share/cockpit/machines/po.pt_BR.js.gz
/usr/share/cockpit/machines/po.tr.js.gz
/usr/share/cockpit/machines/po.uk.js.gz
/usr/share/cockpit/machines/po.zh_CN.js.gz
/usr/share/cockpit/machines/vnc.css.gz
/usr/share/cockpit/machines/vnc.html.gz
/usr/share/cockpit/machines/vnc.min.js.gz
/usr/share/cockpit/networkmanager/index.html.gz
/usr/share/cockpit/networkmanager/manifest.json
/usr/share/cockpit/networkmanager/network.css.gz
/usr/share/cockpit/networkmanager/network.min.js.gz
/usr/share/cockpit/networkmanager/po.ca.js.gz
/usr/share/cockpit/networkmanager/po.cs.js.gz
/usr/share/cockpit/networkmanager/po.da.js.gz
/usr/share/cockpit/networkmanager/po.de.js.gz
/usr/share/cockpit/networkmanager/po.es.js.gz
/usr/share/cockpit/networkmanager/po.fi.js.gz
/usr/share/cockpit/networkmanager/po.fr.js.gz
/usr/share/cockpit/networkmanager/po.hr.js.gz
/usr/share/cockpit/networkmanager/po.hu.js.gz
/usr/share/cockpit/networkmanager/po.ja.js.gz
/usr/share/cockpit/networkmanager/po.js.gz
/usr/share/cockpit/networkmanager/po.ko.js.gz
/usr/share/cockpit/networkmanager/po.my.js.gz
/usr/share/cockpit/networkmanager/po.nl.js.gz
/usr/share/cockpit/networkmanager/po.pa.js.gz
/usr/share/cockpit/networkmanager/po.pl.js.gz
/usr/share/cockpit/networkmanager/po.pt.js.gz
/usr/share/cockpit/networkmanager/po.pt_BR.js.gz
/usr/share/cockpit/networkmanager/po.tr.js.gz
/usr/share/cockpit/networkmanager/po.uk.js.gz
/usr/share/cockpit/networkmanager/po.zh_CN.js.gz
/usr/share/cockpit/ostree/index.html.gz
/usr/share/cockpit/ostree/manifest.json
/usr/share/cockpit/ostree/ostree.css.gz
/usr/share/cockpit/ostree/ostree.min.js.gz
/usr/share/cockpit/ostree/po.ca.js.gz
/usr/share/cockpit/ostree/po.cs.js.gz
/usr/share/cockpit/ostree/po.da.js.gz
/usr/share/cockpit/ostree/po.de.js.gz
/usr/share/cockpit/ostree/po.es.js.gz
/usr/share/cockpit/ostree/po.fi.js.gz
/usr/share/cockpit/ostree/po.fr.js.gz
/usr/share/cockpit/ostree/po.hr.js.gz
/usr/share/cockpit/ostree/po.hu.js.gz
/usr/share/cockpit/ostree/po.ja.js.gz
/usr/share/cockpit/ostree/po.js.gz
/usr/share/cockpit/ostree/po.ko.js.gz
/usr/share/cockpit/ostree/po.my.js.gz
/usr/share/cockpit/ostree/po.nl.js.gz
/usr/share/cockpit/ostree/po.pa.js.gz
/usr/share/cockpit/ostree/po.pl.js.gz
/usr/share/cockpit/ostree/po.pt.js.gz
/usr/share/cockpit/ostree/po.pt_BR.js.gz
/usr/share/cockpit/ostree/po.tr.js.gz
/usr/share/cockpit/ostree/po.uk.js.gz
/usr/share/cockpit/ostree/po.zh_CN.js.gz
/usr/share/cockpit/ovirt/base.css
/usr/share/cockpit/ovirt/index.html.gz
/usr/share/cockpit/ovirt/install.sh
/usr/share/cockpit/ovirt/manifest.json
/usr/share/cockpit/ovirt/ovirt.css.gz
/usr/share/cockpit/ovirt/ovirt.min.js.gz
/usr/share/cockpit/ovirt/po.ca.js.gz
/usr/share/cockpit/ovirt/po.cs.js.gz
/usr/share/cockpit/ovirt/po.da.js.gz
/usr/share/cockpit/ovirt/po.de.js.gz
/usr/share/cockpit/ovirt/po.es.js.gz
/usr/share/cockpit/ovirt/po.fi.js.gz
/usr/share/cockpit/ovirt/po.fr.js.gz
/usr/share/cockpit/ovirt/po.hr.js.gz
/usr/share/cockpit/ovirt/po.hu.js.gz
/usr/share/cockpit/ovirt/po.ja.js.gz
/usr/share/cockpit/ovirt/po.js.gz
/usr/share/cockpit/ovirt/po.ko.js.gz
/usr/share/cockpit/ovirt/po.my.js.gz
/usr/share/cockpit/ovirt/po.nl.js.gz
/usr/share/cockpit/ovirt/po.pa.js.gz
/usr/share/cockpit/ovirt/po.pl.js.gz
/usr/share/cockpit/ovirt/po.pt.js.gz
/usr/share/cockpit/ovirt/po.pt_BR.js.gz
/usr/share/cockpit/ovirt/po.tr.js.gz
/usr/share/cockpit/ovirt/po.uk.js.gz
/usr/share/cockpit/ovirt/po.zh_CN.js.gz
/usr/share/cockpit/ovirt/vnc.css.gz
/usr/share/cockpit/ovirt/vnc.html.gz
/usr/share/cockpit/ovirt/vnc.min.js.gz
/usr/share/cockpit/packagekit/index.html.gz
/usr/share/cockpit/packagekit/manifest.json
/usr/share/cockpit/packagekit/po.ca.js.gz
/usr/share/cockpit/packagekit/po.cs.js.gz
/usr/share/cockpit/packagekit/po.da.js.gz
/usr/share/cockpit/packagekit/po.de.js.gz
/usr/share/cockpit/packagekit/po.es.js.gz
/usr/share/cockpit/packagekit/po.fi.js.gz
/usr/share/cockpit/packagekit/po.fr.js.gz
/usr/share/cockpit/packagekit/po.hr.js.gz
/usr/share/cockpit/packagekit/po.hu.js.gz
/usr/share/cockpit/packagekit/po.ja.js.gz
/usr/share/cockpit/packagekit/po.js.gz
/usr/share/cockpit/packagekit/po.ko.js.gz
/usr/share/cockpit/packagekit/po.my.js.gz
/usr/share/cockpit/packagekit/po.nl.js.gz
/usr/share/cockpit/packagekit/po.pa.js.gz
/usr/share/cockpit/packagekit/po.pl.js.gz
/usr/share/cockpit/packagekit/po.pt.js.gz
/usr/share/cockpit/packagekit/po.pt_BR.js.gz
/usr/share/cockpit/packagekit/po.tr.js.gz
/usr/share/cockpit/packagekit/po.uk.js.gz
/usr/share/cockpit/packagekit/po.zh_CN.js.gz
/usr/share/cockpit/packagekit/updates.css.gz
/usr/share/cockpit/packagekit/updates.min.js.gz
/usr/share/cockpit/pcp/manifest.json
/usr/share/cockpit/pcp/po.ca.js.gz
/usr/share/cockpit/pcp/po.cs.js.gz
/usr/share/cockpit/pcp/po.da.js.gz
/usr/share/cockpit/pcp/po.de.js.gz
/usr/share/cockpit/pcp/po.es.js.gz
/usr/share/cockpit/pcp/po.fi.js.gz
/usr/share/cockpit/pcp/po.fr.js.gz
/usr/share/cockpit/pcp/po.hr.js.gz
/usr/share/cockpit/pcp/po.hu.js.gz
/usr/share/cockpit/pcp/po.ja.js.gz
/usr/share/cockpit/pcp/po.js.gz
/usr/share/cockpit/pcp/po.ko.js.gz
/usr/share/cockpit/pcp/po.my.js.gz
/usr/share/cockpit/pcp/po.nl.js.gz
/usr/share/cockpit/pcp/po.pa.js.gz
/usr/share/cockpit/pcp/po.pl.js.gz
/usr/share/cockpit/pcp/po.pt.js.gz
/usr/share/cockpit/pcp/po.pt_BR.js.gz
/usr/share/cockpit/pcp/po.tr.js.gz
/usr/share/cockpit/pcp/po.uk.js.gz
/usr/share/cockpit/pcp/po.zh_CN.js.gz
/usr/share/cockpit/playground/hammer.gif
/usr/share/cockpit/playground/jquery-patterns.css.gz
/usr/share/cockpit/playground/jquery-patterns.html.gz
/usr/share/cockpit/playground/jquery-patterns.min.js.gz
/usr/share/cockpit/playground/manifest.json
/usr/share/cockpit/playground/metrics.css.gz
/usr/share/cockpit/playground/metrics.html.gz
/usr/share/cockpit/playground/metrics.min.js.gz
/usr/share/cockpit/playground/pkgs.html.gz
/usr/share/cockpit/playground/pkgs.min.js.gz
/usr/share/cockpit/playground/plot.css.gz
/usr/share/cockpit/playground/plot.html.gz
/usr/share/cockpit/playground/plot.min.js.gz
/usr/share/cockpit/playground/po.ca.js.gz
/usr/share/cockpit/playground/po.cs.js.gz
/usr/share/cockpit/playground/po.da.js.gz
/usr/share/cockpit/playground/po.de.js.gz
/usr/share/cockpit/playground/po.es.js.gz
/usr/share/cockpit/playground/po.extra.de.js
/usr/share/cockpit/playground/po.fi.js.gz
/usr/share/cockpit/playground/po.fr.js.gz
/usr/share/cockpit/playground/po.hr.js.gz
/usr/share/cockpit/playground/po.hu.js.gz
/usr/share/cockpit/playground/po.ja.js.gz
/usr/share/cockpit/playground/po.js.gz
/usr/share/cockpit/playground/po.ko.js.gz
/usr/share/cockpit/playground/po.my.js.gz
/usr/share/cockpit/playground/po.nl.js.gz
/usr/share/cockpit/playground/po.pa.js.gz
/usr/share/cockpit/playground/po.pl.js.gz
/usr/share/cockpit/playground/po.pt.js.gz
/usr/share/cockpit/playground/po.pt_BR.js.gz
/usr/share/cockpit/playground/po.tr.js.gz
/usr/share/cockpit/playground/po.uk.js.gz
/usr/share/cockpit/playground/po.zh_CN.js.gz
/usr/share/cockpit/playground/react-patterns.css.gz
/usr/share/cockpit/playground/react-patterns.html.gz
/usr/share/cockpit/playground/react-patterns.min.js.gz
/usr/share/cockpit/playground/service.html.gz
/usr/share/cockpit/playground/service.min.js.gz
/usr/share/cockpit/playground/speed.html.gz
/usr/share/cockpit/playground/speed.min.js.gz
/usr/share/cockpit/playground/test.html.gz
/usr/share/cockpit/playground/test.min.js.gz
/usr/share/cockpit/playground/translate.html.gz
/usr/share/cockpit/playground/translate.min.js.gz
/usr/share/cockpit/realmd/domain.min.js.gz
/usr/share/cockpit/realmd/manifest.json
/usr/share/cockpit/realmd/po.ca.js.gz
/usr/share/cockpit/realmd/po.cs.js.gz
/usr/share/cockpit/realmd/po.da.js.gz
/usr/share/cockpit/realmd/po.de.js.gz
/usr/share/cockpit/realmd/po.es.js.gz
/usr/share/cockpit/realmd/po.fi.js.gz
/usr/share/cockpit/realmd/po.fr.js.gz
/usr/share/cockpit/realmd/po.hr.js.gz
/usr/share/cockpit/realmd/po.hu.js.gz
/usr/share/cockpit/realmd/po.ja.js.gz
/usr/share/cockpit/realmd/po.js.gz
/usr/share/cockpit/realmd/po.ko.js.gz
/usr/share/cockpit/realmd/po.my.js.gz
/usr/share/cockpit/realmd/po.nl.js.gz
/usr/share/cockpit/realmd/po.pa.js.gz
/usr/share/cockpit/realmd/po.pl.js.gz
/usr/share/cockpit/realmd/po.pt.js.gz
/usr/share/cockpit/realmd/po.pt_BR.js.gz
/usr/share/cockpit/realmd/po.tr.js.gz
/usr/share/cockpit/realmd/po.uk.js.gz
/usr/share/cockpit/realmd/po.zh_CN.js.gz
/usr/share/cockpit/selinux/manifest.json
/usr/share/cockpit/selinux/po.ca.js.gz
/usr/share/cockpit/selinux/po.cs.js.gz
/usr/share/cockpit/selinux/po.da.js.gz
/usr/share/cockpit/selinux/po.de.js.gz
/usr/share/cockpit/selinux/po.es.js.gz
/usr/share/cockpit/selinux/po.fi.js.gz
/usr/share/cockpit/selinux/po.fr.js.gz
/usr/share/cockpit/selinux/po.hr.js.gz
/usr/share/cockpit/selinux/po.hu.js.gz
/usr/share/cockpit/selinux/po.ja.js.gz
/usr/share/cockpit/selinux/po.js.gz
/usr/share/cockpit/selinux/po.ko.js.gz
/usr/share/cockpit/selinux/po.my.js.gz
/usr/share/cockpit/selinux/po.nl.js.gz
/usr/share/cockpit/selinux/po.pa.js.gz
/usr/share/cockpit/selinux/po.pl.js.gz
/usr/share/cockpit/selinux/po.pt.js.gz
/usr/share/cockpit/selinux/po.pt_BR.js.gz
/usr/share/cockpit/selinux/po.tr.js.gz
/usr/share/cockpit/selinux/po.uk.js.gz
/usr/share/cockpit/selinux/po.zh_CN.js.gz
/usr/share/cockpit/selinux/selinux.css.gz
/usr/share/cockpit/selinux/selinux.min.js.gz
/usr/share/cockpit/selinux/setroubleshoot.html.gz
/usr/share/cockpit/shell/images/server-error.png
/usr/share/cockpit/shell/images/server-large.png
/usr/share/cockpit/shell/images/server-small.png
/usr/share/cockpit/shell/index-no-machines.css.gz
/usr/share/cockpit/shell/index-no-machines.min.js.gz
/usr/share/cockpit/shell/index-stub.css.gz
/usr/share/cockpit/shell/index-stub.min.js.gz
/usr/share/cockpit/shell/index.css.gz
/usr/share/cockpit/shell/index.html
/usr/share/cockpit/shell/index.min.js.gz
/usr/share/cockpit/shell/manifest.json
/usr/share/cockpit/shell/po.ca.js.gz
/usr/share/cockpit/shell/po.cs.js.gz
/usr/share/cockpit/shell/po.da.js.gz
/usr/share/cockpit/shell/po.de.js.gz
/usr/share/cockpit/shell/po.es.js.gz
/usr/share/cockpit/shell/po.fi.js.gz
/usr/share/cockpit/shell/po.fr.js.gz
/usr/share/cockpit/shell/po.hr.js.gz
/usr/share/cockpit/shell/po.hu.js.gz
/usr/share/cockpit/shell/po.ja.js.gz
/usr/share/cockpit/shell/po.js.gz
/usr/share/cockpit/shell/po.ko.js.gz
/usr/share/cockpit/shell/po.my.js.gz
/usr/share/cockpit/shell/po.nl.js.gz
/usr/share/cockpit/shell/po.pa.js.gz
/usr/share/cockpit/shell/po.pl.js.gz
/usr/share/cockpit/shell/po.pt.js.gz
/usr/share/cockpit/shell/po.pt_BR.js.gz
/usr/share/cockpit/shell/po.tr.js.gz
/usr/share/cockpit/shell/po.uk.js.gz
/usr/share/cockpit/shell/po.zh_CN.js.gz
/usr/share/cockpit/shell/shell.html.gz
/usr/share/cockpit/shell/simple.html
/usr/share/cockpit/shell/stub.html
/usr/share/cockpit/sosreport/index.html.gz
/usr/share/cockpit/sosreport/manifest.json
/usr/share/cockpit/sosreport/po.ca.js.gz
/usr/share/cockpit/sosreport/po.cs.js.gz
/usr/share/cockpit/sosreport/po.da.js.gz
/usr/share/cockpit/sosreport/po.de.js.gz
/usr/share/cockpit/sosreport/po.es.js.gz
/usr/share/cockpit/sosreport/po.fi.js.gz
/usr/share/cockpit/sosreport/po.fr.js.gz
/usr/share/cockpit/sosreport/po.hr.js.gz
/usr/share/cockpit/sosreport/po.hu.js.gz
/usr/share/cockpit/sosreport/po.ja.js.gz
/usr/share/cockpit/sosreport/po.js.gz
/usr/share/cockpit/sosreport/po.ko.js.gz
/usr/share/cockpit/sosreport/po.my.js.gz
/usr/share/cockpit/sosreport/po.nl.js.gz
/usr/share/cockpit/sosreport/po.pa.js.gz
/usr/share/cockpit/sosreport/po.pl.js.gz
/usr/share/cockpit/sosreport/po.pt.js.gz
/usr/share/cockpit/sosreport/po.pt_BR.js.gz
/usr/share/cockpit/sosreport/po.tr.js.gz
/usr/share/cockpit/sosreport/po.uk.js.gz
/usr/share/cockpit/sosreport/po.zh_CN.js.gz
/usr/share/cockpit/sosreport/sosreport.css.gz
/usr/share/cockpit/sosreport/sosreport.min.js.gz
/usr/share/cockpit/sosreport/sosreport.png
/usr/share/cockpit/ssh/manifest.json
/usr/share/cockpit/ssh/po.ca.js.gz
/usr/share/cockpit/ssh/po.cs.js.gz
/usr/share/cockpit/ssh/po.da.js.gz
/usr/share/cockpit/ssh/po.de.js.gz
/usr/share/cockpit/ssh/po.es.js.gz
/usr/share/cockpit/ssh/po.fi.js.gz
/usr/share/cockpit/ssh/po.fr.js.gz
/usr/share/cockpit/ssh/po.hr.js.gz
/usr/share/cockpit/ssh/po.hu.js.gz
/usr/share/cockpit/ssh/po.ja.js.gz
/usr/share/cockpit/ssh/po.js.gz
/usr/share/cockpit/ssh/po.ko.js.gz
/usr/share/cockpit/ssh/po.my.js.gz
/usr/share/cockpit/ssh/po.nl.js.gz
/usr/share/cockpit/ssh/po.pa.js.gz
/usr/share/cockpit/ssh/po.pl.js.gz
/usr/share/cockpit/ssh/po.pt.js.gz
/usr/share/cockpit/ssh/po.pt_BR.js.gz
/usr/share/cockpit/ssh/po.tr.js.gz
/usr/share/cockpit/ssh/po.uk.js.gz
/usr/share/cockpit/ssh/po.zh_CN.js.gz
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
/usr/share/cockpit/static/login.min.html
/usr/share/cockpit/static/login.po.ca.html
/usr/share/cockpit/static/login.po.cs.html
/usr/share/cockpit/static/login.po.da.html
/usr/share/cockpit/static/login.po.de.html
/usr/share/cockpit/static/login.po.es.html
/usr/share/cockpit/static/login.po.fi.html
/usr/share/cockpit/static/login.po.fr.html
/usr/share/cockpit/static/login.po.hr.html
/usr/share/cockpit/static/login.po.html
/usr/share/cockpit/static/login.po.hu.html
/usr/share/cockpit/static/login.po.ja.html
/usr/share/cockpit/static/login.po.ko.html
/usr/share/cockpit/static/login.po.my.html
/usr/share/cockpit/static/login.po.nl.html
/usr/share/cockpit/static/login.po.pa.html
/usr/share/cockpit/static/login.po.pl.html
/usr/share/cockpit/static/login.po.pt.html
/usr/share/cockpit/static/login.po.pt_BR.html
/usr/share/cockpit/static/login.po.tr.html
/usr/share/cockpit/static/login.po.uk.html
/usr/share/cockpit/static/login.po.zh_CN.html
/usr/share/cockpit/storaged/images/storage-array.png
/usr/share/cockpit/storaged/images/storage-disk.png
/usr/share/cockpit/storaged/index.html.gz
/usr/share/cockpit/storaged/manifest.json
/usr/share/cockpit/storaged/po.ca.js.gz
/usr/share/cockpit/storaged/po.cs.js.gz
/usr/share/cockpit/storaged/po.da.js.gz
/usr/share/cockpit/storaged/po.de.js.gz
/usr/share/cockpit/storaged/po.es.js.gz
/usr/share/cockpit/storaged/po.fi.js.gz
/usr/share/cockpit/storaged/po.fr.js.gz
/usr/share/cockpit/storaged/po.hr.js.gz
/usr/share/cockpit/storaged/po.hu.js.gz
/usr/share/cockpit/storaged/po.ja.js.gz
/usr/share/cockpit/storaged/po.js.gz
/usr/share/cockpit/storaged/po.ko.js.gz
/usr/share/cockpit/storaged/po.my.js.gz
/usr/share/cockpit/storaged/po.nl.js.gz
/usr/share/cockpit/storaged/po.pa.js.gz
/usr/share/cockpit/storaged/po.pl.js.gz
/usr/share/cockpit/storaged/po.pt.js.gz
/usr/share/cockpit/storaged/po.pt_BR.js.gz
/usr/share/cockpit/storaged/po.tr.js.gz
/usr/share/cockpit/storaged/po.uk.js.gz
/usr/share/cockpit/storaged/po.zh_CN.js.gz
/usr/share/cockpit/storaged/storage.css.gz
/usr/share/cockpit/storaged/storage.min.js.gz
/usr/share/cockpit/subscriptions/index.html.gz
/usr/share/cockpit/subscriptions/manifest.json
/usr/share/cockpit/subscriptions/po.ca.js.gz
/usr/share/cockpit/subscriptions/po.cs.js.gz
/usr/share/cockpit/subscriptions/po.da.js.gz
/usr/share/cockpit/subscriptions/po.de.js.gz
/usr/share/cockpit/subscriptions/po.es.js.gz
/usr/share/cockpit/subscriptions/po.fi.js.gz
/usr/share/cockpit/subscriptions/po.fr.js.gz
/usr/share/cockpit/subscriptions/po.hr.js.gz
/usr/share/cockpit/subscriptions/po.hu.js.gz
/usr/share/cockpit/subscriptions/po.ja.js.gz
/usr/share/cockpit/subscriptions/po.js.gz
/usr/share/cockpit/subscriptions/po.ko.js.gz
/usr/share/cockpit/subscriptions/po.my.js.gz
/usr/share/cockpit/subscriptions/po.nl.js.gz
/usr/share/cockpit/subscriptions/po.pa.js.gz
/usr/share/cockpit/subscriptions/po.pl.js.gz
/usr/share/cockpit/subscriptions/po.pt.js.gz
/usr/share/cockpit/subscriptions/po.pt_BR.js.gz
/usr/share/cockpit/subscriptions/po.tr.js.gz
/usr/share/cockpit/subscriptions/po.uk.js.gz
/usr/share/cockpit/subscriptions/po.zh_CN.js.gz
/usr/share/cockpit/subscriptions/subscriptions.css.gz
/usr/share/cockpit/subscriptions/subscriptions.min.js.gz
/usr/share/cockpit/systemd/index.html.gz
/usr/share/cockpit/systemd/logs.html.gz
/usr/share/cockpit/systemd/logs.min.js.gz
/usr/share/cockpit/systemd/manifest.json
/usr/share/cockpit/systemd/po.ca.js.gz
/usr/share/cockpit/systemd/po.cs.js.gz
/usr/share/cockpit/systemd/po.da.js.gz
/usr/share/cockpit/systemd/po.de.js.gz
/usr/share/cockpit/systemd/po.es.js.gz
/usr/share/cockpit/systemd/po.fi.js.gz
/usr/share/cockpit/systemd/po.fr.js.gz
/usr/share/cockpit/systemd/po.hr.js.gz
/usr/share/cockpit/systemd/po.hu.js.gz
/usr/share/cockpit/systemd/po.ja.js.gz
/usr/share/cockpit/systemd/po.js.gz
/usr/share/cockpit/systemd/po.ko.js.gz
/usr/share/cockpit/systemd/po.my.js.gz
/usr/share/cockpit/systemd/po.nl.js.gz
/usr/share/cockpit/systemd/po.pa.js.gz
/usr/share/cockpit/systemd/po.pl.js.gz
/usr/share/cockpit/systemd/po.pt.js.gz
/usr/share/cockpit/systemd/po.pt_BR.js.gz
/usr/share/cockpit/systemd/po.tr.js.gz
/usr/share/cockpit/systemd/po.uk.js.gz
/usr/share/cockpit/systemd/po.zh_CN.js.gz
/usr/share/cockpit/systemd/services.html.gz
/usr/share/cockpit/systemd/services.min.js.gz
/usr/share/cockpit/systemd/system.css.gz
/usr/share/cockpit/systemd/system.min.js.gz
/usr/share/cockpit/systemd/terminal.css.gz
/usr/share/cockpit/systemd/terminal.html.gz
/usr/share/cockpit/systemd/terminal.min.js.gz
/usr/share/cockpit/tuned/manifest.json
/usr/share/cockpit/tuned/performance.css.gz
/usr/share/cockpit/tuned/performance.min.js.gz
/usr/share/cockpit/tuned/po.ca.js.gz
/usr/share/cockpit/tuned/po.cs.js.gz
/usr/share/cockpit/tuned/po.da.js.gz
/usr/share/cockpit/tuned/po.de.js.gz
/usr/share/cockpit/tuned/po.es.js.gz
/usr/share/cockpit/tuned/po.fi.js.gz
/usr/share/cockpit/tuned/po.fr.js.gz
/usr/share/cockpit/tuned/po.hr.js.gz
/usr/share/cockpit/tuned/po.hu.js.gz
/usr/share/cockpit/tuned/po.ja.js.gz
/usr/share/cockpit/tuned/po.js.gz
/usr/share/cockpit/tuned/po.ko.js.gz
/usr/share/cockpit/tuned/po.my.js.gz
/usr/share/cockpit/tuned/po.nl.js.gz
/usr/share/cockpit/tuned/po.pa.js.gz
/usr/share/cockpit/tuned/po.pl.js.gz
/usr/share/cockpit/tuned/po.pt.js.gz
/usr/share/cockpit/tuned/po.pt_BR.js.gz
/usr/share/cockpit/tuned/po.tr.js.gz
/usr/share/cockpit/tuned/po.uk.js.gz
/usr/share/cockpit/tuned/po.zh_CN.js.gz
/usr/share/cockpit/users/index.html.gz
/usr/share/cockpit/users/manifest.json
/usr/share/cockpit/users/po.ca.js.gz
/usr/share/cockpit/users/po.cs.js.gz
/usr/share/cockpit/users/po.da.js.gz
/usr/share/cockpit/users/po.de.js.gz
/usr/share/cockpit/users/po.es.js.gz
/usr/share/cockpit/users/po.fi.js.gz
/usr/share/cockpit/users/po.fr.js.gz
/usr/share/cockpit/users/po.hr.js.gz
/usr/share/cockpit/users/po.hu.js.gz
/usr/share/cockpit/users/po.ja.js.gz
/usr/share/cockpit/users/po.js.gz
/usr/share/cockpit/users/po.ko.js.gz
/usr/share/cockpit/users/po.my.js.gz
/usr/share/cockpit/users/po.nl.js.gz
/usr/share/cockpit/users/po.pa.js.gz
/usr/share/cockpit/users/po.pl.js.gz
/usr/share/cockpit/users/po.pt.js.gz
/usr/share/cockpit/users/po.pt_BR.js.gz
/usr/share/cockpit/users/po.tr.js.gz
/usr/share/cockpit/users/po.uk.js.gz
/usr/share/cockpit/users/po.zh_CN.js.gz
/usr/share/cockpit/users/users.css.gz
/usr/share/cockpit/users/users.min.js.gz
/usr/share/metainfo/cockpit.appdata.xml
/usr/share/pixmaps/cockpit.png

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/cockpit/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/security/pam_ssh_add.so

%files locales -f cockpit.lang
%defattr(-,root,root,-)

