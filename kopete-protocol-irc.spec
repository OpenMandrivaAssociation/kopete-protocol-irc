Name:           kopete-protocol-irc
License:        GPLv2+
Url:            http://kde-apps.org/content/show.php/kopete+irc+plugin?content=113720
Group:          Networking/Instant messaging
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        IRC Protocol support for Kopete
Version:        0.1.2
Release:        %mkrel 8
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


%changelog
* Sun Mar 20 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.1.2-8mdv2011.0
+ Revision: 647082
- Rebuild

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-7mdv2011.0
+ Revision: 612659
- the mass rebuild of 2010.1 packages

* Fri Mar 19 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.1.2-6mdv2010.1
+ Revision: 525166
- Rebuild

* Fri Nov 27 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.1.2-5mdv2010.1
+ Revision: 470615
- Lets upse makeinstall_std
- Lets upse makeinstall_std
- Add -D to let install in rootjail
- Add -D to find ircclient-qt includes
- BR fixed
- import kopete-protocol-irc

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean spec file to use mandriva rules and policies
        - Use kde rpm macros
        - Use rpm macros and do not hardcode prefix
        - do not tell to report bugs on opensuse bugzilla
        - Do not use copyrighted suse spec file


* Thu Nov 23 2009 Daniel Lucio <dlucio@mandriva.org> - 0.1.2-1mdv2010.0
- Bump release

