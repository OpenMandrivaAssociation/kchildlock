Name:		kchildlock
Version:0.90.4.2
Release:	2
Summary:	Tool to monitor and restrict time spend on computer by a children
Source0:	http://ufpr.dl.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
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
%{_kde_libdir}/kde4/kcm_kchildlock.so
%{_kde_libdir}/kde4/kded_kchildlockdaemon.so
%{_kde_datadir}/config/kchildlockrc
%{_kde_services}/kcm_kchildlock.desktop
%{_kde_services}/kded/kchildlockdaemon.desktop
%{_var}/opt/kchildlock/dummy.txt
%{_kde_iconsdir}/hicolor/*/*/*
%doc %{_kde_docdir}/HTML/en/kcontrol/%{name}

#------------------------------------------------------------------------------

%prep
%setup -q


%build
%cmake_kde4
%make

%install

%makeinstall_std -C build

%find_lang %{name}

