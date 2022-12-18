configure_file(
  input: meson.project_name() + '.in',
  output: 'local-'+meson.project_name(),
  configuration: local_conf
)

configure_file(
  input:  meson.project_name() + '.in',
  output: meson.project_name(),
  configuration: conf,
  install_dir: get_option('bindir')
)

configure_file(
  input: 'constants.py.in',
  output: 'constants.py',
  configuration: configuration_data({
    'APP_ID': APPLICATION_ID,
    'RELEASE_VER': meson.project_version(),
    'VERSION': meson.project_version() ,
    'BUILD_TYPE': get_option('buildtype'),
    'PKGDATA_DIR': PKGDATA_DIR,
    'LOCALE_DIR': conf.get('LOCALE_DIR'),
    'APP_ROOT':  APPLICATION_ROOT,
  }),
  install: true,
  install_dir: PY_INSTALLDIR.get_install_dir() / meson.project_name(),
)

launcher = join_paths(meson.project_build_root(), meson.project_name(), 'local-' + meson.project_name())

run_target('run',
  command: [launcher]
)

# Install sources
py_sources = [
  '__init__.py',
  'main.py',
]
PY_INSTALLDIR.install_sources(py_sources, subdir: meson.project_name() )


# Install ui Python modules
ui_modules = [
'ui/__init__.py',
'ui/window.py',
]
PY_INSTALLDIR.install_sources(ui_modules, subdir: meson.project_name() + '/ui')

