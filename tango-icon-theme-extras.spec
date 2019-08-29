#
# TODO:
# - better summary and descriptions
# - add license
#
Summary:	Additional freedesktop.org standard compliant icons
Summary(pl.UTF-8):	Dodatkowe ikony implementujące standard freedesktop.org
Name:		tango-icon-theme-extras
Version:	0.1.0
Release:	3
License:	Creative Commons License (see COPYING)
Group:		Themes
Source0:	http://tango-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	caaceaec7b61f1cbda0db9842f9db281
URL:		http://tango-project.org/Tango_Desktop_Project
BuildRequires:	ImageMagick-coder-png
BuildRequires:	ImageMagick-devel
BuildRequires:	icon-naming-utils >= 0.7.2
BuildRequires:	librsvg
BuildRequires:	pkgconfig
Requires:	tango-icon-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional freedesktop.org standard compliant icons.

%description -l pl.UTF-8
Dodatkowe ikony implementujące standard freedesktop.org.

%prep
%setup -q

%build
%configure \
	--enable-png-creation
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Tango

%postun
%update_icon_cache Tango

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%{_iconsdir}/Tango
