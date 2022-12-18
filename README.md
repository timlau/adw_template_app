# Pyhton Libadwaita & Gtk4 Template application
A template for building a [libadwaita](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/main/index.html) and [Gtk4](https://docs.gtk.org/gtk4/index.html) application in python

- A flexible app using 
  - Adw.Application
  - Adw.ApplicationWindow
  - Adw.Leaflet
  - Adw.Stack and friends
- ui is build using [blueprint](https://jwestman.pages.gitlab.gnome.org/blueprint-compiler/)
- use Gtk.Template to connect the ui with the python class
- resources stored in GRessouce (.ui & style.css)
- settings stored in GSettings (win dimentions is saved at close)
- using meson to build/install
- easy to transform into a new project check [customize.md](customize.md) for details
  


## build and run

run this script to build and run the application

```
./local.sh
```

## flatpak build & run

Build as flatpak
```
flatpak-builder --force-clean .flatpak/repo build-aux/flatpak/org.mydomain.Example.yml
```

Run the flatpak
```
flatpak-builder --run .flatpak/repo build-aux/flatpak/org.mydomain.Example.yml
```


## Requirements

- gtk4-devel >= 4.5
- libadwaita-devel >= 1.2
- blueprint-compiler
- python3-gobject
- python3 >= 3.10
- meson

### Fedora 37

```
sudo dnf install gtk4-devel libadwaita-devel blueprint-compiler meson
```
