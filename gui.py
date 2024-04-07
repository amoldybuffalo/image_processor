import sys
import gi
from actions import Action
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from photo_area import PhotoArea
from modules.scale import scale_action
from action_box import ActionBox

from action_predefs import action_predefs


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(640,480)


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.images = []
        self.action_box = ActionBox(list(action_predefs.values()))
        self.connect('activate', self.on_activate)
       

    def on_activate(self, app):
        self.build(app)
        self.win.present()

    def make_header(self):
        header = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        apply_button = Gtk.Button.new_with_label("Process photos")
        apply_button.connect("clicked", self.apply_actions)
        header.append(apply_button)
        return header

    def resize(self, widget):
        _, window_height = self.win.get_dimensions()
        widget_width, _ = widget.get_dimensions()
        widget.set_size_request(widget_width, window_height - 100)
        print(widget.type)

    def build(self, app, templates=None):
        self.win = MainWindow(application=app)
        self.photo_area = PhotoArea(self.win, 3)
        outer_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        outer_container.set_vexpand(True)
        header = self.make_header()
        split_view = Adw.OverlaySplitView()
        split_view.set_max_sidebar_width(100)
        split_view.set_hexpand(True)
        sidebar = Adw.NavigationPage()
        content = Adw.NavigationPage()
        sidebar.set_child(self.action_box.display())
        content.set_child(self.photo_area.display())
        split_view.set_sidebar(sidebar)
        split_view.set_content(content)
        outer_container.append(header)
        outer_container.append(split_view)
        self.win.set_child(outer_container)

    def apply_actions(self, widget):
        images = self.photo_area.get_images()
        for image in images:
            self.action_box.apply_actions(image)

    def on_window_resize(self, widget):
        (w, h) = self.win.get_size()
        self.image_window.set_size_request(w - 200, h - 100)

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)