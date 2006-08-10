#
# TODO:
# - better summary and descriptions
# - check why 24x24 and scalable icon sets don't build correctly
# - add license
#
Summary:	Additional freedesktop.org standard compliant icons
Summary(pl):	Dodatkowe ikony implementuj±ce standard freedesktop.org
Name:		tango-icon-theme-extras
Version:	0.1.0
Release:	0.1
License:	Creative Commons License (see COPYING)
Group:		Themes
Source0:	http://tango-project.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	caaceaec7b61f1cbda0db9842f9db281
URL:		http://tango-project.org/Tango_Desktop_Project
BuildRequires:	ImageMagick-coder-png
BuildRequires:	ImageMagick-devel
BuildRequires:	icon-naming-utils >= 0.7.2
BuildRequires:	pkgconfig
Requires:	tango-icon-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional freedesktop.org standard compliant icons.

%description -l pl
Dodatkowe ikony implementuj±ce standard freedesktop.org.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%{_iconsdir}/Tango
