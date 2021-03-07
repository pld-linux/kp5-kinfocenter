%define		kdeplasmaver	5.21.2
%define		qtver		5.9.0
%define		kpname		kinfocenter
Summary:	kinfocenter
Name:		kp5-%{kpname}
Version:	5.21.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	3ff86188bcb031a63a1f210741734658
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-khtml-devel
BuildRequires:	ninja
BuildRequires:	pciutils-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility that provides information about a computer system.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,sr@latin}

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kinfocenter
/etc/xdg/menus/kinfocenter.menu
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_about_distro.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_devinfo.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_info.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_memory.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_opengl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_pci.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_usb.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_view1394.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_energyinfo.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_fileindexermonitor.so
%{_desktopdir}/org.kde.kinfocenter.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%dir %{_datadir}/kcmusb
%{_datadir}/kcmusb/usb.ids
%dir %{_datadir}/kcmview1394
%{_datadir}/kcmview1394/oui.db
%dir %{_datadir}/kpackage/kcms/kcm_energyinfo
%dir %{_datadir}/kpackage/kcms/kcm_energyinfo/contents
%dir %{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui
%{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui/Graph.qml
%{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_energyinfo/metadata.desktop
%dir %{_datadir}/kpackage/kcms/kcm_fileindexermonitor
%dir %{_datadir}/kpackage/kcms/kcm_fileindexermonitor/contents
%dir %{_datadir}/kpackage/kcms/kcm_fileindexermonitor/contents/ui
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/contents/ui/constants.js
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/metadata.desktop
%{_datadir}/kservices5/about-distro.desktop
%{_datadir}/kservices5/deviceinfocategory.desktop
%{_datadir}/kservices5/devinfo.desktop
%{_datadir}/kservices5/dma.desktop
%{_datadir}/kservices5/graphicalinfocategory.desktop
%{_datadir}/kservices5/interrupts.desktop
%{_datadir}/kservices5/ioports.desktop
%{_datadir}/kservices5/kcm_energyinfo.desktop
%{_datadir}/kservices5/kcm_fileindexermonitor.desktop
%{_datadir}/kservices5/kcm_memory.desktop
%{_datadir}/kservices5/kcm_pci.desktop
%{_datadir}/kservices5/kcmusb.desktop
%{_datadir}/kservices5/kcmview1394.desktop
%{_datadir}/kservices5/lostfoundcategory.desktop
%{_datadir}/kservices5/networkinfocategory.desktop
%{_datadir}/kservices5/opengl.desktop
%{_datadir}/kservices5/smbstatus.desktop
%{_datadir}/kservices5/wayland.desktop
%{_datadir}/kservices5/xserver.desktop
%{_datadir}/kservicetypes5/kinfocentercategory.desktop
%{_datadir}/kpackage/kcms/kcm_energyinfo/metadata.json
%{_datadir}/kpackage/kcms/kcm_fileindexermonitor/metadata.json
%{_datadir}/metainfo/org.kde.kinfocenter.appdata.xml

%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_nic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_samba.so
%dir %{_datadir}/kpackage/kcms/kcm_nic
%dir %{_datadir}/kpackage/kcms/kcm_nic/contents
%dir %{_datadir}/kpackage/kcms/kcm_nic/contents/ui
%{_datadir}/kpackage/kcms/kcm_nic/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_nic/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_nic/metadata.json
%dir %{_datadir}/kpackage/kcms/kcmsamba
%dir %{_datadir}/kpackage/kcms/kcmsamba/contents
%{_datadir}/kpackage/kcms/kcmsamba/contents/ShareListItem.qml
%{_datadir}/kpackage/kcms/kcmsamba/contents/main.qml
%{_datadir}/kpackage/kcms/kcmsamba/metadata.desktop
%{_datadir}/kpackage/kcms/kcmsamba/metadata.json
%{_datadir}/kservices5/basicinformation.desktop
%{_datadir}/kservices5/detailedinformation.desktop
%{_datadir}/kservices5/kcm_nic.desktop
