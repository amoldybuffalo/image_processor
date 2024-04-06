import sys
import gi
from actions import Action
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from photo_area import PhotoArea
def sample(args):
    pass

sample_options = [{"type":"input", "name":"width"}, {"type":"input", "name":"height"}]

a = Action("Crop", sample_options, sample)

actions = [a]

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(640,480)


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.images = []
        self.actions = actions
        self.connect('activate', self.on_activate)
       

    def on_activate(self, app):
        self.build(app)
        self.win.present()
        
    def build(self, app, templates=None):
        self.win = MainWindow(application=app)
        self.photo_area = PhotoArea(self.win, 3)
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        separator.set_margin_start(30)
        separator.set_margin_end(30)
        for a in self.actions:
            container.append(a.display())
        container.append(separator)
        container.append(self.photo_area.display())     
        self.win.set_child(container)

    def apply_actions(self, widget):
        images = self.photo_area.get_images()
        for image in images:
            for action in self.actions:
                image = action.run_on(image) #operates recursively

    def on_window_resize(self, widget):
        (w, h) = self.win.get_size()
        self.image_window.set_size_request(w - 200, h - 100)

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)