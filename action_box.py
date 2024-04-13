import sys
import gi
from actions import Action
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
from settings import read_setting
class ActionBox:
    def __init__(self, actions, error_handler):
        self.actions = actions
        self.current_actions = []
        self.error_handler = error_handler
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
        self.main_container.set_margin_end(5)
        self.main_container.set_margin_start(5)
        return self.main_container

    def on_down_button_click(self, widget):
        for i in range(len(self.current_actions)):
            curr_widget = widget.get_parent().get_parent().get_parent()
            if self.current_actions[i]["widget"] == curr_widget:
                if i < len(self.current_actions) - 1:
                    self.main_container.reorder_child_after(self.current_actions[i]["widget"], self.current_actions[i+1]["widget"])
                    self.current_actions[i], self.current_actions[i+1] = self.current_actions[i+1], self.current_actions[i]
                    print([a["id"] for a in self.current_actions])

    def on_up_button_click(self, widget):
        for i in range(len(self.current_actions)):
            curr_widget = widget.get_parent().get_parent().get_parent()
            if self.current_actions[i]["widget"] == curr_widget:
                if i != 0:
                    if i == 1: 
                        self.main_container.reorder_child_after(self.current_actions[i]["widget"], None) 
                    else:
                        self.main_container.reorder_child_after(self.current_actions[i]["widget"], self.current_actions[i-2]["widget"])
                    self.current_actions[i], self.current_actions[i-1] = self.current_actions[i-1], self.current_actions[i]
                    print([a["id"] for a in self.current_actions])

    def on_delete_button_click(self, widget):
        for i in range(len(self.current_actions)):
            curr_widget = widget.get_parent().get_parent().get_parent()
            if self.current_actions[i]["widget"] == curr_widget:
                self.main_container.remove(self.current_actions[i]["widget"])
                self.current_actions.remove(self.current_actions[i])

    def create_widget_from_action(self, action):
        frame = Gtk.Frame()
        frame.set_margin_top(5)
        frame.set_margin_bottom(5)
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        header.set_hexpand(True)
        up_btn = Gtk.Button()
        up_btn.set_icon_name("go-up")
        up_btn.connect("clicked", self.on_up_button_click)
        down_btn = Gtk.Button()
        down_btn.set_icon_name("go-down")
        down_btn.connect("clicked", self.on_down_button_click)
        remove_btn = Gtk.Button()
        remove_btn.set_icon_name("delete")
        remove_btn.set_valign(Gtk.Align.END)
        remove_btn.connect("clicked", self.on_delete_button_click)
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
        output_path = read_setting("settings.json", "save_path")
        intermediate_path = read_setting("settings.json", "intermediate_path")
        actions = [self.actions[i] for i in [a["id"] for a in self.current_actions]]
        for action in actions:
                if action.get_settings() == None:
                    self.error_handler.error("Some settings not set!")
                    return
        for i, action in enumerate(actions):
            if (i - 1) < len(actions):            
                image = action.run_on(image, intermediate_path) #operates recursively
            else:
                image = action.run_on(image, output_path)



