import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class ProgressWindow:
    def __new__(cls, total_steps, parent):
        if total_steps >= 0:
            instance = super().__new__(cls)
            instance.__init__(total_steps, parent)
            return instance
        else:
            return None

    def __init__(self, total_steps, parent):
        self.total_steps = total_steps
        self.current_steps = 0
        self.parent = parent
        

    def display(self):
        self.dialog = Gtk.MessageDialog(title="Progress")
        #dialog.add_buttons(("_Okay"), Gtk.ResponseType.ACCEPT)
        self.dialog.set_size_request(300,200)
        self.dialog.set_transient_for(self.parent)
        self.dialog.set_modal(True)
        content_area = self.dialog.get_content_area()
        
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.label = Gtk.Label()
        self.progress_bar = Gtk.ProgressBar()

        container.append(self.label)
        container.append(self.progress_bar)
        
        content_area.append(container)

        self.dialog.show()

    def update(self, msg, update_type):
        self.label.set_markup(msg)
        if update_type == "finish":
            self.current_steps += 1
            self.progress_bar.set_fraction(self.current_steps/self.total_steps)
        

        if self.current_steps == self.total_steps:
            self.label.set_markup("<b>FINISHED!</b>")

        
