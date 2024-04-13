import sys
import gi
from settings import read_setting
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib

class Action:
    def __init__(self, name, parameters, callback):
        self.name = name
        self.parameters = parameters
        self.callback = callback
        self.settings = []
    
    def on_entry_changed(self, entry):
        # Use GLib.idle_add to delay the action until the main loop is idle
        GLib.idle_add(self.filter_entry_text, entry)

    def filter_entry_text(self, entry):
        text = entry.get_text()
        new_text = ''.join([char for char in text if char.isdigit()])
        if new_text != text:
            entry.set_text(new_text)
            entry.set_position(-1)
        return False 

    def get_settings(self):
        data = {}
        for setting in self.settings:
            id, widget = setting.values()
            if widget.__class__.__name__ == "CheckButton":
                data[id] = widget.get_active()
            elif widget.__class__.__name__ == "Entry":
                text = widget.get_text()
                if text == "":
                    return None
                else:
                    data[id] = text
        return data
        


    def display(self):
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, )
        main_box.set_size_request(200, 100)
        main_box.set_spacing(5)
        name = Gtk.Label()
        name.set_markup(f"<b>{self.name}</b>")
        main_box.set_margin_start(10)
        main_box.set_margin_end(10)
        main_box.set_margin_bottom(10)
        main_box.append(name)

        for option in self.parameters:
            if option["type"] == "check":
                check_box = Gtk.CheckButton(label=option["name"])
                self.settings.append({"id":option["id"], "widget": check_box})
                main_box.append(check_box)
            elif option["type"] == "number":
                lbl = Gtk.Label(label=option["name"])
                entry = Gtk.Entry()
                entry.connect("changed", self.on_entry_changed)
                self.settings.append({"id":option["id"], "widget":entry})
                main_box.append(lbl)
                main_box.append(entry)
        return main_box

    def run_on(self, filename, path):
        settings = self.get_settings()
        return self.callback(filename, path, settings)
        





