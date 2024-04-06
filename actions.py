import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, GLib



class Action:
    def __init__(self, name, parameters, callback):
        self.name = name
        self.parameters = parameters
        self.callback = callback
        self.data = []
        self.settings_widgets = []

    
    def on_entry_changed(self, entry):
        # Use GLib.idle_add to delay the action until the main loop is idle
        GLib.idle_add(filter_entry_text, entry)

    def filter_entry_text(entry):
        text = entry.get_text()
        new_text = ''.join([char for char in text if char.isdigit()])
        if new_text != text:
            entry.set_text(new_text)
            entry.set_position(-1)
        return False 

    def on_apply(self, widget, callback_data=None):
        for widget in self.settings_widgets:
            print(widget.__class__.__name__)
            if widget.__class__.__name__ == "CheckButton":
                self.data.append(widget.get_active())
            elif widget.__class__.__name__ == "Entry":
                self.data.append(widget.get_text())


    def display(self):
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, )
        main_box.set_size_request(200, 100)
        main_box.set_spacing(10)
        name = Gtk.Label()
        name.set_markup(self.name)
        main_box.set_margin_start(10)
        main_box.append(name)

        for option in self.parameters:
            if option["type"] == "check":
                check_box = Gtk.CheckButton(label=option["name"])
                self.settings_widgets.append(check_box)
                main_box.append(check_box)
            elif option["type"] == "input":
                lbl = Gtk.Label(label=option["name"])
                entry = Gtk.Entry()
                entry.connect("changed", self.on_entry_changed)
                main_box.append(lbl)
                main_box.append(entry)
                self.settings_widgets.append(entry)
        apply = Gtk.Button(label="Apply")
        apply.connect("clicked", self.on_apply, None)
        main_box.append(apply)
        return main_box

        def run_on(filename):
            return self.callback([filename, *self.parameters])





