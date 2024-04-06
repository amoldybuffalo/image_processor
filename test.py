import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class FileGridWindow(Gtk.Window):

    def __init__(self):
        super().__init__(title="File Grid")

        self.grid = Gtk.Grid()
        self.set_child(self.grid)

        self.button = Gtk.Button(label="Open File Dialog")
        self.button.connect("clicked", self.on_button_clicked)
        self.grid.attach(self.button, 0, 0, 1, 1)

        self.file_list = Gtk.FlowBox()
        self.file_list.set_selection_mode(Gtk.SelectionMode.NONE)
        self.grid.attach_next_to(self.file_list, self.button, Gtk.PositionType.BOTTOM, 1, 1)

    def on_button_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.set_select_multiple(True)

        dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
        dialog.add_button("Open", Gtk.ResponseType.OK)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            files = dialog.get_files()
            self.display_files(files)
        elif response == Gtk.ResponseType.CANCEL:
            print("File selection canceled")

        dialog.destroy()

    def display_files(self, files):
        for file in files:
            image = Gtk.Image.new_from_file(file.get_path())
            self.file_list.add(image)
            self.show_all()

win = FileGridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()