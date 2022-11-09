#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.26.3
%define		qtver		5.15.2
%define		kpname		kinfocenter
Summary:	kinfocenter
Name:		kp5-%{kpname}
Version:	5.26.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ad7a6e104e9e095460eeb6f7008a454e
URL:		http://www.kde.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-khtml-devel
BuildRequires:	libusb-devel
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
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%if %{with tests}
ctest
%endif

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
%{_desktopdir}/org.kde.kinfocenter.desktop
%{_datadir}/desktop-directories/kinfocenter.directory
%dir %{_datadir}/kpackage/kcms/kcm_energyinfo
%dir %{_datadir}/kpackage/kcms/kcm_energyinfo/contents
%dir %{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui
%{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui/Graph.qml
%{_datadir}/kpackage/kcms/kcm_energyinfo/contents/ui/main.qml
%{_datadir}/metainfo/org.kde.kinfocenter.appdata.xml

%dir %{_datadir}/kpackage/kcms/kcm_nic
%dir %{_datadir}/kpackage/kcms/kcm_nic/contents
%dir %{_datadir}/kpackage/kcms/kcm_nic/contents/ui
%{_datadir}/kpackage/kcms/kcm_nic/contents/ui/main.qml

%dir %{_libdir}/qt5/qml/org/kde/kinfocenter
%dir %{_libdir}/qt5/qml/org/kde/kinfocenter/private
%{_libdir}/qt5/qml/org/kde/kinfocenter/private/CommandOutputKCM.qml
%{_libdir}/qt5/qml/org/kde/kinfocenter/private/qmldir
%{_datadir}/kinfocenter
%dir %{_datadir}/kpackage/kcms/kcm_about-distro
%dir %{_datadir}/kpackage/kcms/kcm_about-distro/contents
%dir %{_datadir}/kpackage/kcms/kcm_about-distro/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_cpu
%dir %{_datadir}/kpackage/kcms/kcm_cpu/contents
%dir %{_datadir}/kpackage/kcms/kcm_cpu/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_egl
%dir %{_datadir}/kpackage/kcms/kcm_egl/contents
%dir %{_datadir}/kpackage/kcms/kcm_egl/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_glx
%dir %{_datadir}/kpackage/kcms/kcm_glx/contents
%dir %{_datadir}/kpackage/kcms/kcm_glx/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_interrupts
%dir %{_datadir}/kpackage/kcms/kcm_interrupts/contents
%dir %{_datadir}/kpackage/kcms/kcm_interrupts/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_pci
%dir %{_datadir}/kpackage/kcms/kcm_pci/contents
%dir %{_datadir}/kpackage/kcms/kcm_pci/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_vulkan
%dir %{_datadir}/kpackage/kcms/kcm_vulkan/contents
%dir %{_datadir}/kpackage/kcms/kcm_vulkan/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_wayland
%dir %{_datadir}/kpackage/kcms/kcm_wayland/contents
%dir %{_datadir}/kpackage/kcms/kcm_wayland/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_xserver
%dir %{_datadir}/kpackage/kcms/kcm_xserver/contents
%dir %{_datadir}/kpackage/kcms/kcm_xserver/contents/ui
%dir %{_datadir}/kpackage/kcms/kcmsamba
%dir %{_datadir}/kpackage/kcms/kcmsamba/contents
%dir %{_datadir}/kpackage/kcms/kcmsamba/contents/ui

%attr(755,root,root) %{_libdir}/libKInfoCenterInternal.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kcm_about-distro.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kcm_energyinfo.so
%dir %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_cpu.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_devinfo.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_egl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_glx.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_interrupts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_nic.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_pci.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_samba.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_usb.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_vulkan.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_wayland.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_xserver.so
%{_datadir}/kpackage/kcms/kcm_about-distro/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_cpu/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_egl/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_glx/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_interrupts/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_pci/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_vulkan/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_wayland/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_xserver/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcmsamba/contents/ui/ShareListItem.qml
%{_datadir}/kpackage/kcms/kcmsamba/contents/ui/main.qml

%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_firmware_security.so
%attr(755,root,root) %{_prefix}/libexec/kauth/kinfocenter-dmidecode-helper
%{_desktopdir}/kcm_about-distro.desktop
%{_datadir}/dbus-1/system-services/org.kde.kinfocenter.dmidecode.service
%{_datadir}/dbus-1/system.d/org.kde.kinfocenter.dmidecode.conf
%dir %{_datadir}/kpackage/kcms/kcm_firmware_security
%dir %{_datadir}/kpackage/kcms/kcm_firmware_security/contents
%dir %{_datadir}/kpackage/kcms/kcm_firmware_security/contents/code
%attr(755,root,root) %{_datadir}/kpackage/kcms/kcm_firmware_security/contents/code/fwupdmgr.sh
%dir %{_datadir}/kpackage/kcms/kcm_firmware_security/contents/ui
%{_datadir}/kpackage/kcms/kcm_firmware_security/contents/ui/main.qml
%{_datadir}/polkit-1/actions/org.kde.kinfocenter.dmidecode.policy

%{_libdir}/qt5/plugins/plasma/kcms/kinfocenter/kcm_kwinsupportinfo.so
%dir %{_datadir}/kpackage/kcms/kcm_kwinsupportinfo
%dir %{_datadir}/kpackage/kcms/kcm_kwinsupportinfo/contents
%dir %{_datadir}/kpackage/kcms/kcm_kwinsupportinfo/contents/ui
%{_datadir}/kpackage/kcms/kcm_kwinsupportinfo/contents/ui/main.qml
