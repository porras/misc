Name: bemoji
Version: 0.4.0
Release: %autorelease
Summary: Emoji picker with support for bemenu/wofi/rofi/dmenu and wayland/X11
License: MIT
URL: https://github.com/marty-oehme/bemoji
Source: https://github.com/marty-oehme/bemoji/releases/download/v/bemoji-%{version}.tar.gz
BuildArch: noarch

Requires: (bemenu or wofi or rofi or rofi-wayland or dmenu or ilia or fuzzel)
Requires: (wl-clipboard or (xclip and xsel))
Requires: (wtype or xdotool)
Requires: sed grep /usr/bin/cut /usr/bin/sort /usr/bin/uniq /usr/bin/tr curl

%description
Emoji picker with support for bemenu/wofi/rofi/dmenu and wayland/X11.

Will remember your favorite emojis and give you quick access.

%prep
%setup -cq

%build
# nothing to build

%install
install -D -m 0755 -t %{buildroot}%{_bindir} %{name}
install -D -m 0644 -t %{buildroot}%{_mandir}/man1 doc/%{name}.1.*

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%license doc/LICENSE
%doc doc/README.md

%changelog
%autochangelog
