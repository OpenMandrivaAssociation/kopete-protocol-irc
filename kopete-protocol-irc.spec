#
# spec file for package kopete-protocol-facebook
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

%define gitrev 3376a46

Name:           kopete-protocol-irc
License:        GPLv2+
Url:            http://kde-apps.org/content/show.php/kopete+irc+plugin?content=113720
Group:          Networking/Instant messaging
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        IRC Protocol support for Kopete
Version:        0.1.2
Release:        %mkrel 2
Source:         http://kde-apps.org/CONTENT/content-files/113720-irc.tar.gz
Requires:	ircclient-qt
BuildRequires:  kdenetwork4-devel
BuildRequires:  ircclient-qt-devel >= 0.3.2

%description
Facebook Protocol Support for Kopete

%prep
%setup -n irc

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr -DIRCCLIENT_INCLUDE_DIR=/usr/lib/qt4/include/ircclient-qt/ ..

%install
cd build
%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%doc AUTHORS COPYING
/usr/%_lib/kde4/kopete_irc.so
/usr/share/apps/kopete/icons/*
/usr/share/apps/kopete/ircnetworks.xml
#/usr/share/apps/kopete/icons/oxygen/16x16/actions/*
#/usr/share/apps/kopete/icons/oxygen/32x32/*
/usr/share/apps/kopete_irc/ircchatui.rc
/usr/share/kde4/services/kopete_irc.desktop

