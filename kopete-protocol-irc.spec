Summary:	IRC Protocol support for Kopete
Name:		kopete-protocol-irc
Version:	0.1.2
Release:	11
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://kde-apps.org/content/show.php/kopete+irc+plugin?content=113720
Source0:	http://kde-apps.org/CONTENT/content-files/113720-irc.tar.gz
BuildRequires:	kopete-devel
BuildRequires:	ircclient-qt-devel >= 0.3.2
Requires:	ircclient-qt
Requires:	kopete

%description
IRC Protocol Support for Kopete.

%files
%{_kde_libdir}/kde4/kopete_irc.so
%{_kde_appsdir}/kopete/icons/*
%{_kde_appsdir}/kopete/ircnetworks.xml
%{_kde_appsdir}/kopete_irc
%{_kde_datadir}/kde4/services/kopete_irc.desktop

#----------------------------------------------------------------------------

%prep
%setup -qn irc

%build
%cmake_kde4 -DIRCCLIENT_INCLUDE_DIR=%{_qt_includedir}/ircclient-qt/

%install
%makeinstall_std -C build

