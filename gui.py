import sys
import gi
from actions import Action
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from photo_area import PhotoArea
from modules.scale import scale_action
from action_box import ActionBox
from error import ErrorHandler
from settings_page import SettingsPage
from progress import ProgressWindow
from predefs import action_predefs, settings_predefs


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(640,480)

    
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.error_handler = ErrorHandler(self.win)
        self.action_box = ActionBox(list(action_predefs.values()), self.error_handler)
        self.photo_area = PhotoArea(self.win, self.action_box, 3)
        self.build(app)
        self.win.present()

    def build(self, app, templates=None):

        #test 
        p_window = ProgressWindow(10, self.win)
        p_window.display()
        p_window.update("Did something", "finish")

        switcher = Adw.ViewSwitcher()
        switcher.set_vexpand(False)
        stack = Adw.ViewStack()
        
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        container.set_vexpand(True)
        split_view = Adw.OverlaySplitView()
        split_view.set_max_sidebar_width(100)
        split_view.set_hexpand(True)
        sidebar = Adw.NavigationPage()
        content = Adw.NavigationPage()
        sidebar.set_child(self.action_box.display())
        content.set_child(self.photo_area.display())
        split_view.set_sidebar(sidebar)
        split_view.set_content(content)
        split_view.set_margin_top(5)

        settings_page = SettingsPage(settings_predefs)

        stack.add_titled_with_icon(split_view, "Program", "Program", "applications-accessories")
        stack.add_titled_with_icon(settings_page.display(), "Settings", "Settings", "preferences-other")

        switcher.set_stack(stack)
        switcher.set_policy(Adw.ViewSwitcherPolicy.WIDE)
        separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)

        container.append(switcher)
        container.append(separator)
        container.append(stack)

        self.win.set_child(container)

app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)