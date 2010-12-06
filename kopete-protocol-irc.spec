Name:           kopete-protocol-irc
License:        GPLv2+
Url:            http://kde-apps.org/content/show.php/kopete+irc+plugin?content=113720
Group:          Networking/Instant messaging
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        IRC Protocol support for Kopete
Version:        0.1.2
Release:        %mkrel 7
Source:         http://kde-apps.org/CONTENT/content-files/113720-irc.tar.gz
Requires:	    ircclient-qt
Requires:       kopete
BuildRequires:  kdenetwork4-devel
BuildRequires:  ircclient-qt-devel >= 0.3.2

%description
Irc Protocol Support for Kopete

%files
%defattr(-,root,root)
%_kde_libdir/kde4/kopete_irc.so
%_kde_appsdir/kopete/icons/*
%_kde_appsdir/kopete/ircnetworks.xml
%_kde_appsdir/kopete_irc
%_kde_datadir/kde4/services/kopete_irc.desktop

#--------------------------------------------------------------------

%prep
%setup -n irc

%build
%cmake_kde4 -DIRCCLIENT_INCLUDE_DIR=/usr/lib/qt4/include/ircclient-qt/

%install
%makeinstall_std -C build

%clean
rm -rf %buildroot
