%define name    sgrotum
%define version 2.0.0
%define release 7

%define section Networking/Mail
%define title   Sgrotum
%define Summary Email/news SiGnature ROTUMbulator

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          %section
URL:            https://homepages.ihug.co.nz/~trmusson/programs.html
Source0:        %name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot
Buildrequires:  glib2-devel

%description
An email/news SiGnature ROTUMbulator. As well as the rotation and
randomization of signatures, it'll optionally insert random
quotations, taking care of length, word-wrap and justification.
Like this:

# Han
-- 
                 __   Men often believe -- or pretend -- that the Law
      .,-;-;-,. /'_\  is something sacred, or at least a science -- an
    _/_/_/_|_\_\) /       unfounded assumption very convenient to
  '-<_><_><_><_>=/\                     governments.
jgs `/_/====/_/-'\_\
     ""     ""    ""


%prep
%setup -q

%build
%configure --enable-glib2
%make


%install
rm -rf %buildroot
%makeinstall


%clean
rm -rf %buildroot


%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING README ChangeLog examples
%_mandir/man1/%name.1.*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0.0-6mdv2010.0
+ Revision: 433731
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0.0-5mdv2009.0
+ Revision: 260647
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0.0-4mdv2009.0
+ Revision: 252367
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.0.0-2mdv2008.1
+ Revision: 127214
- kill re-definition of %%buildroot on Pixel's request
- import sgrotum


* Mon Jan 02 2006 Lenny Cartier <lenny@mandriva.com> 2.0.0-2mdk
- rebuild

* Fri Oct 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.0-1mdk
- 2.0.0

* Fri Sep 12 2003 Han Boetes <han@linux-mandrake.com> 1.2.6-1mdk
- Initial release for mandrake. Perhaps it will even make it in 9.2
  cooker? :)


