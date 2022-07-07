#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kwalletmanager
Summary:	kwallet manager
Name:		ka5-%{kaname}
Version:	22.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	fcebc5681997a24906d6820835bc94af
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kauth-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KWalletManager is a tool to manage the passwords on your system. By
using the KDE wallet subsystem it not only allows you to keep your own
secrets but also to access and manage the passwords of every
application that integrates with the wallet.

%description -l pl.UTF-8
KWalletManager to narzędzie do zarządzania hasłami na Twoim
systemie. Używanie podsystemu portfela KDE, nie tylko pozwala Ci
trzymać Twoje sekretu, ale też zarządzać hasłami przez każdą
aplikację, która się z nim integruje.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwalletmanager5
%{_libdir}/qt5/plugins/kcm_kwallet5.so
%attr(755,root,root) %{_libexecdir}/kauth/kcm_kwallet_helper5
%{_desktopdir}/kwalletmanager5-kwalletd.desktop
%{_desktopdir}/org.kde.kwalletmanager5.desktop
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_iconsdir}/hicolor/128x128/apps/kwalletmanager.png
%{_iconsdir}/hicolor/128x128/apps/kwalletmanager2.png
%{_iconsdir}/hicolor/16x16/apps/kwalletmanager.png
%{_iconsdir}/hicolor/16x16/apps/kwalletmanager2.png
%{_iconsdir}/hicolor/22x22/actions/wallet-closed.png
%{_iconsdir}/hicolor/22x22/actions/wallet-open.png
%{_iconsdir}/hicolor/22x22/apps/kwalletmanager.png
%{_iconsdir}/hicolor/32x32/apps/kwalletmanager.png
%{_iconsdir}/hicolor/32x32/apps/kwalletmanager2.png
%{_iconsdir}/hicolor/48x48/apps/kwalletmanager.png
%{_iconsdir}/hicolor/48x48/apps/kwalletmanager2.png
%{_iconsdir}/hicolor/64x64/apps/kwalletmanager.png
%{_iconsdir}/hicolor/64x64/apps/kwalletmanager2.png
%{_datadir}/kservices5/kwalletconfig5.desktop
%{_datadir}/kservices5/kwalletmanager5_show.desktop
%{_datadir}/metainfo/org.kde.kwalletmanager5.appdata.xml
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet5.conf
%{_datadir}/qlogging-categories5/kwalletmanager.categories
%{_datadir}/dbus-1/services/org.kde.kwalletmanager5.service
