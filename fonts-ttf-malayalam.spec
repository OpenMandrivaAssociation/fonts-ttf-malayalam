Summary:	Malayalam TrueType fonts
Name:		fonts-ttf-malayalam
Version:	1.0
Release:	9
License:	GPLv2+
Url:		http://malayalamlinux.sourceforge.net/downloads/downloads.html
Group:		System/Fonts/True type
Source0:	http://malayalamlinux.sourceforge.net/downloads/fonts/MalOtf.ttf
Source1:	http://malayalamlinux.sourceforge.net/downloads/COPYING
BuildArch:	noarch
BuildRequires:	fontconfig

%description
This Package provides Free Malayalam TrueType fonts.

%prep

%build

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/TTF/malayalam
install -m 644 %SOURCE0 %{buildroot}/%{_datadir}/fonts/TTF/malayalam

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/malayalam \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-malayalam:pri=50

%files
%dir %{_datadir}/fonts/TTF/malayalam/
%{_datadir}/fonts/TTF/malayalam/*.ttf
%{_sysconfdir}/X11/fontpath.d/ttf-malayalam:pri=50

