# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

import sys
import os

from gi.repository import Gio, Adw

from example.ui.window import ExampleMainWindow
from example.constants import rootdir, app_id


class ExampleApplication(Adw.Application):
    """The main application class."""

    __gtype_name__ = "ExampleApplication"

    def __init__(self):
        super().__init__(application_id=app_id, flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.set_resource_base_path(rootdir)
        self.style_manager = Adw.StyleManager.get_default()
        self.settings = Gio.Settings.new(app_id)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """

        self.win = self.props.active_window
        if not self.win:
            self.win = ExampleMainWindow(
                application=self,
                default_height=self.settings.get_int("window-height"),
                default_width=self.settings.get_int("window-width"),
            )
            # create app actions
            self.create_action("about", self.on_about)
            self.create_action("preferences", self.on_preferences)
        self.win.present()

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
            activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

    def on_about(self, *_args):
        toast = Adw.Toast.new("About was pressed")
        toast.set_timeout(1)
        self.win.toast_overlay.add_toast(toast)

    def on_preferences(self, *_args):
        toast = Adw.Toast.new("Preferences was pressed")
        toast.set_timeout(1)
        self.win.toast_overlay.add_toast(toast)


def main():
    """The application's entry point."""
    app = ExampleApplication()
    return app.run(sys.argv)
