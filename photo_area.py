import sys
import gi
from actions import Action
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from utils import get_gtk_image


class PhotoArea:
    def __init__(self, win, row_width):
        self.images = []
        self.row_width = row_width
        self.win = win

    def add_to_images(self, filename):
        self.images.append(filename)
        print(self.images)
        ROW_SIZE = self.row_width
        IMAGE_SIZE = 50
        image_count = len(self.images)
        print(image_count)
        frame = Gtk.Frame()
        image = get_gtk_image(filename, 1000, 1000)
        image.set_size_request(200,200)
        frame.set_child(image)
        frame.set_margin_start(5)
        frame.set_margin_end(5)
        frame.set_margin_top(5)
        frame.set_margin_bottom(5)
        self.image_grid.attach(frame, ((image_count-1) % ROW_SIZE) * IMAGE_SIZE, ((image_count-1) // ROW_SIZE) * IMAGE_SIZE, IMAGE_SIZE, IMAGE_SIZE)

    def display(self):
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box.set_vexpand(True)
        title = Gtk.Label()
        title.set_markup("<b><span size=\"large\">Photos:</span></b>")
        main_box.append(title)
        self.image_window = Gtk.ScrolledWindow()
        self.image_window.set_size_request(400, 300)
        self.image_grid = Gtk.Grid()
        self.image_grid.set_row_spacing(5)
        self.image_window.set_child(self.image_grid)
        self.image_window.set_vexpand(True)
        main_box.append(self.image_window)
        button = Gtk.Button(label="Import Photos...")
        button.connect("clicked", self.file_dialog)
        main_box.append(button)
        return main_box

    def display_files(self, files):
        for file in files:
            self.add_to_images(file.get_path())
            self.image_grid.show()

    def on_file_choice(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            files = dialog.get_files()
            self.display_files(files)
        elif response == Gtk.ResponseType.CANCEL:
            print("File selection canceled")
        dialog.destroy()

    def file_dialog(self, widget):
        dialog = Gtk.FileChooserDialog(title='Foo', action=Gtk.FileChooserAction.OPEN)
        dialog.add_buttons(
        ("_Cancel"), Gtk.ResponseType.CANCEL,
        ("_Open"), Gtk.ResponseType.ACCEPT)
        dialog.connect("response", self.on_file_choice)
        dialog.show()
    
    def get_images(self):
        return list(set(self.images))
        