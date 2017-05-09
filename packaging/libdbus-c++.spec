Summary:	C++ Interface for DBus
Name:		libdbus-c++
Version:	1.1
Release:	70001
URL:		http://dev.openwengo.org/trac/openwengo/trac.fcgi/browser/wengophone-ng/branches/wengophone-dbus-api/libs/dbus/src
Source0:	%{name}-%{version}.tar.gz
License:	LGPL
Group:		Libraries
BuildRoot:	%{_tmppath}/%{name}-root
Prefix:		/usr

%description

Ability to reflect dbus methods and signals into a more natural C++ object system.

%package devel
Requires:	libdbus-c++ = %{version}
Group:		Development/Libraries
Summary:	Header files for libdbus-c++

%description devel
Header files for libdbus-c++


%prep
%setup -q 

%build
./bootstrap
./configure --prefix=/usr --disable-ecore 
make -j 4

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(755,root,root)
%{prefix}/lib/libdbus-c++*.so*



%files devel
%defattr(-,root,root)
%{prefix}/bin/dbusxx-xml2cpp
%{prefix}/bin/dbusxx-introspect
%{prefix}/lib/libdbus-c*.a
%{prefix}/lib/libdbus-c*.la
%{prefix}/include/dbus-c++-1
%{prefix}/lib/pkgconfig/*.pc

%changelog
* Thu Feb 8 2007 Ben Martin
- initial spec file
