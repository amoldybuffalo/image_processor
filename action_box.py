import sys
import gi
from actions import Action
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class ActionBox:
    def __init__(self, actions):
        self.actions = actions

    def make_dropdown(self):
        strings = [action["name"] for action in self.actions]
        dropdown = Gtk.Dropdown.new_from_strings(strings)
        return dropdown

    def get_box(self):


