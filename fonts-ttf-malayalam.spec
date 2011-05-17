Summary:	Malayalam TrueType fonts
Name:		fonts-ttf-malayalam
Version:	1.0
Release:	%mkrel 7
License:	GPLv2+
URL:		http://malayalamlinux.sourceforge.net/downloads/downloads.html
Group:		System/Fonts/True type
Source0:	http://malayalamlinux.sourceforge.net/downloads/fonts/MalOtf.ttf
Source1:	http://malayalamlinux.sourceforge.net/downloads/COPYING
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This Package provides Free Malayalam TrueType fonts.

%prep

%build

%install
rm -fr %buildroot
mkdir -p %buildroot/%{_datadir}/fonts/TTF/malayalam
install -m 644 %SOURCE0 %buildroot/%{_datadir}/fonts/TTF/malayalam

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/malayalam \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-malayalam:pri=50

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,0755)
%dir %_datadir/fonts/TTF/malayalam/
%_datadir/fonts/TTF/malayalam/*.ttf
%_sysconfdir/X11/fontpath.d/ttf-malayalam:pri=50
