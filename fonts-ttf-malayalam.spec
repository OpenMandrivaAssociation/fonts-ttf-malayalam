Summary:	Malayalam TrueType fonts
Name:		fonts-ttf-malayalam
Version:	1.0
Release:	%mkrel 9
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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-7mdv2011.0
+ Revision: 675423
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0-6
+ Revision: 675187
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0-5
+ Revision: 664336
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2011.0
+ Revision: 605202
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-3mdv2010.1
+ Revision: 494154
- fc-cache is now called by an rpm filetrigger

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0-2mdv2009.1
+ Revision: 351131
- rebuild

* Thu Jun 26 2008 Funda Wang <fwang@mandriva.org> 1.0-1mdv2009.0
+ Revision: 229200
- import fonts-ttf-malayalam


