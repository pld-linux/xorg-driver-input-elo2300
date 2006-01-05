Summary:	X.org input driver for ELOGraphics 2300 touch screens
Summary(pl):	Sterownik wej�ciowy X.org dla ekran�w dotykowych ELOGraphics 2300
Name:		xorg-driver-input-elo2300
Version:	1.0.0.5
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/driver/xf86-input-elo2300-%{version}.tar.bz2
# Source0-md5:	664af07018e07207358a73b4e93e7a91
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for ELOGraphics 2300 touch screens.

%description -l pl
Sterownik wej�ciowy X.org dla ekran�w dotykowych ELOGraphics 2300.

%prep
%setup -q -n xf86-input-elo2300-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/elo2300_drv.so
#%{_mandir}/man4/elo2300.4*
