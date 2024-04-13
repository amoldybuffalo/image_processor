import json
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

def get_settings_path():
     return "./settings.json"

def read_setting(key):
    path = get_settings_path()
    with open(path, "r") as fp:
        settings = json.load(fp)
        return settings[key]

def write_setting(key, value):
    path = get_settings_path()
    with open(path, "rw") as fp:
        settings = json.load(fp)
        settings[key] = value
        json.dump(fp, path)

class SettingWidget:
    def __init__(self, name, setting, _type):
        self.name = label
        self.type = _type
        self.setting = setting
        self.widget = None

    def choose_path(self):
        dialog = Gtk.FileChooserDialog(title='Open Image', parent=self.parent, action=Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.add_buttons(
        ("_Cancel"), Gtk.ResponseType.CANCEL,
        ("_Open"), Gtk.ResponseType.ACCEPT)
        dialog.connect("response", self.on_file_choice)
        dialog.show()

    def get_value():

    def retrieve_setting(self):
        seting = read_setting()

    def apply(self):
        write_setting(self.setting_name, self.value)

    def display(self):
        name = Gtk.label()
        if self.type == "path":
            self.widget = Gtk.Entry()
        label.set_markup(self.name)
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        apply_button = Gtk.Button()


