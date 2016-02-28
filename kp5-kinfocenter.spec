%define		kdeplasmaver	5.5.4
%define		qtver		5.4.0
%define		kpname		kinfocenter
Summary:	kinfocenter
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	4eddff6767cf1a2d47b6ddf711a4655e
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
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kinfocenter

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_nic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_opengl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_pci.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_samba.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_usb.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_view1394.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_energyinfo.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_fileindexermonitor.so
%{_desktopdir}/org.kde.kinfocenter.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%{_datadir}/kcmusb/usb.ids
%{_datadir}/kcmview1394/oui.db
%{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui/Graph.qml
%{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_energyinfo/metadata.desktop
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
%{_datadir}/kservices5/nic.desktop
%{_datadir}/kservices5/opengl.desktop
%{_datadir}/kservices5/scsi.desktop
%{_datadir}/kservices5/smbstatus.desktop
%{_datadir}/kservices5/wayland.desktop
%{_datadir}/kservices5/xserver.desktop
%{_datadir}/kservicetypes5/kinfocentercategory.desktop
%{_datadir}/kxmlgui5/kinfocenter/kinfocenterui.rc
