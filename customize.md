# Customize into your own application

This document contains instructions on how to change the template into your on app

## meson.build

- change project name **example** to **myapp**
- change the APPLICATION_ID to **org.yourdomain.MyApp**
- change the APPLICATION_ROOT to **/org/yourdomain/MyApp**

```meson
project('example',
          version: '1.0',
    meson_version: '>= 0.59.0',
)

APPLICATION_ID = 'org.mydomain.Example'
APPLICATION_ROOT = '/org/mydomain/Example'
```

## example/

rename the **example** directory
```bash
mv example/ myapp/
```
## example/example.in

rename the **example/example.in**
```
mv example/example.in example/myapp.in
```

## data/example.gresource.xml.in

rename **data/example.gresource.xml.in**

```
mv data/example.gresource.xml.in data/myapp.gresource.xml.in
```

## data/example.gschema.xml.in

rename **data/example.gschema.xml.in**

```
mv data/data/example.gschema.xml.in.in data/data/myapp.gschema.xml.in
```
## build-aux/flatpak/org.mydomain.Example.yml

rename **build-aux/flatpak/org.mydomain.Example.yml**

```
mv build-aux/flatpak/org.mydomain.Example.yml build-aux/flatpak/org.yourdomain.MyApp.yml
```

Edit **build-aux/flatpak/org.yourdomain.MyApp.yml**

Change the **app-id:** to **org.yourdomain.MyApp**

```yaml
app-id: org.mydomain.Example
runtime: org.gnome.Platform
runtime-version: "43"
```
