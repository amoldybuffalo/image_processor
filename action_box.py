import sys
import gi
from actions import Action
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class ActionBox:
    def __init__(self, actions):
        self.actions = actions
        self.current_actions = []
    def make_dropdown(self):
        container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        strings = ["None"] + [action.name for action in self.actions]
        self.dropdown = Gtk.DropDown.new_from_strings(strings)
        add_button = Gtk.Button.new_with_label("Add action")
        add_button.connect("clicked", self.on_action_select)
        container.append(self.dropdown)
        container.append(add_button)
        return container

    def display(self):
        self.main_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        dropdown = self.make_dropdown()
        self.main_container.append(dropdown)
        self.main_container.set_vexpand(True)
        return self.main_container

    def on_down_button_click(self, widget):
        for i in range(len(self.current_actions)):
            curr_widget = widget.get_parent().get_parent().get_parent()
            print(curr_widget)
            if self.current_actions[i]["widget"] == curr_widget:
                if i != len(self.current_actions):
                    self.main_container.reorder_child_after(self.current_actions[i]["widget"], self.current_actions[i+1]["widget"])
                    self.current_actions[i], self.current_actions[i+1] = self.current_actions[i+1], self.current_actions[i]

    def on_up_button_click(self, widget):
        pass
    def create_widget_from_action(self, action):
        frame = Gtk.Frame()
        frame.set_margin_top(5)
        frame.set_margin_bottom(5)
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        header.set_hexpand(True)
        up_btn = Gtk.Button()
        up_btn.set_icon_name("go-up")
        down_btn = Gtk.Button()
        down_btn.set_icon_name("go-down")
        down_btn.connect("clicked", self.on_down_button_click)
        remove_btn = Gtk.Button()
        remove_btn.set_icon_name("delete")
        remove_btn.set_valign(Gtk.Align.END)
        header.append(up_btn)
        header.append(down_btn)
        header.append(remove_btn)

        container.append(header)
        container.append(action.display())
        frame.set_child(container)

        return frame
        

    def on_action_select(self, widget):
        dropdown_position = self.dropdown.get_selected()
        if dropdown_position !=  0:
            action_number = dropdown_position - 1
            if not action_number in [a["id"] for a in self.current_actions]:
                action = {"id":action_number, "widget":self.create_widget_from_action(self.actions[action_number])}
                self.current_actions.append(action)
                self.main_container.append(action["widget"])
    def apply_actions(self, image):
        actions = [self.actions[i] for i in [a["id"] for a in self.current_actions]]
        for action in actions:
                image = action.run_on(image) #operates recursively



