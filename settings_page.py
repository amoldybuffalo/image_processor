import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
import settings

class Setting:
    def __init__(self, name, setting, _type):
        self.name = name
        self.type = _type
        self.setting = setting
        self.widget = None

    def on_folder_choice(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            folders = dialog.get_files()
            path = folders[0].get_path()
            self.widget.set_text(path)
        elif response == Gtk.ResponseType.CANCEL:
            print("File selection canceled")
        dialog.destroy()

    def choose_path(self, widget):
        dialog = Gtk.FileChooserDialog(title='Find Folder', action=Gtk.FileChooserAction.SELECT_FOLDER)
        dialog.add_buttons(
        ("_Cancel"), Gtk.ResponseType.CANCEL,
        ("_Choose"), Gtk.ResponseType.ACCEPT)
        dialog.connect("response", self.on_folder_choice)
        dialog.show()

    def get_value(self):
        if self.type == "path":
            value = self.widget.get_text()
        return value

    def retrieve_setting(self):
        setting = settings.read_setting(self.setting)
        if setting != None:
            if self.type == "path":
                self.widget.set_text(setting)

    def apply(self):
        value = self.get_value()
        settings.write_setting(self.setting, value)

    def display(self):
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        container.set_spacing(5)
        label = Gtk.Label()
        label.set_markup(self.name)
        container.append(label)
        
        if self.type == "path":
            self.widget = Gtk.Entry()
            open_path_dialog = Gtk.Button.new_with_label("Choose Folder")
            open_path_dialog.connect("clicked", self.choose_path)
            container.append(self.widget)
            container.append(open_path_dialog)
        self.retrieve_setting()
        return container

class SettingsPage:
    def __init__(self, settings):
        self.settings = settings

    def on_apply_button_click(self, widget):
        for setting in self.settings:
            setting.apply()

    def display(self):
        container = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        container.set_spacing(10)
        container.set_halign(Gtk.Align.CENTER)

        for setting in self.settings:
            container.append(setting.display())
        
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        separator.set_margin_top(10)
        separator.set_margin_bottom(3)

        apply_button = Gtk.Button.new_with_label("Apply")
        apply_button.connect("clicked", self.on_apply_button_click)
        container.append(separator)
        container.append(apply_button)
        return container
        