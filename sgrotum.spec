%define name    sgrotum
%define version 2.0.0
%define release %mkrel 2

%define section Networking/Mail
%define title   Sgrotum
%define Summary Email/news SiGnature ROTUMbulator

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          %section
URL:            http://homepages.ihug.co.nz/~trmusson/programs.html
Source0:        %name-%version.tar.bz2
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

