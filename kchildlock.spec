%define name	kchildlock
%define version	 0.75.4
%define release	%mkrel 1
%define Summary	 Tool to monitor and restrict time spend on computer by a children

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://ufpr.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}_%{version}.orig.tar.gz
# Patch 0 fix the hardcoded path for installing libs
Patch0:		kchildlock-0.75.4-mdv-fix-cmake-install-path.patch
# Patch 1 fix a wrong path in the desktop file for kcm
Patch1:		kchildlock-0.75.3-mdv-fix-icon-path.patch
Patch2:		kchildlock-0.75.3-drop-kworkspace.patch
License:	GPLv2
Group:		Graphical desktop/KDE 
URL:		http://kde-apps.org/content/show.php/KChildlock?content=88124
BuildRequires:	kdelibs4-devel	

%description

kchildlock is a tool to monitor and restrict the time a children spends on the
computer. The limits can be specified per day of the week, by lower and upper
hour limits, maximum daily usage time, and maximum weekly usage time. The same
restriction limits can be applied to applications based on the user login. It
requires the KDE4 Desktop.

%files  -f %{name}.lang
%defattr(-,root,root)
%_kde_libdir/kde4/kcm_kchildlock.so
%_kde_libdir/kde4/kded_kchildlockdaemon.so
%_kde_datadir/apps/%{name}/
%_kde_datadir/config/kchildlockrc
%_kde_services/kcm_kchildlock.desktop
%_kde_services/kded/kchildlockdaemon.desktop
%doc %_kde_docdir/HTML/en/kcontrol/%{name}

#------------------------------------------------------------------------------

%prep
%setup -q 
%patch0 -p0
%patch1	-p0
%patch2 -p0

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build


%find_lang %{name} 

%clean
%__rm -rf %buildroot
