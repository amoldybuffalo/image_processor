import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class ErrorHandler:
    def __init__(self, parent):
        self.parent = parent
    def destroy(self, widget, data):
        widget.destroy()
    def error(self,msg):
        dialog = Gtk.MessageDialog(title="Error!")
        dialog.add_buttons(("_Okay"), Gtk.ResponseType.ACCEPT)
        dialog.set_size_request(300,200)
        dialog.set_transient_for(self.parent)
        dialog.set_modal(True) 
        label = Gtk.Label()
        label.set_markup(f"{msg}")
        content_area = dialog.get_content_area()
        content_area.append(label)
        dialog.connect("response", self.destroy)
        dialog.show()
