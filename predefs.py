from actions import Action
from modules.scale import scale_action
from modules.crop import crop_action, crop_square_action
from modules.light_levels import light_level_action
from settings_page import Setting

action_predefs = {
    "scale": Action("Scale", [{"type":"number", "name":"Width", "id":"width"}, {"type":"number", "name":"Height", "id":"height"}], scale_action),
    "crop": Action("Smart Crop", [{"type":"number", "name":"Horizontal Buffer", "id":"horizontal_buffer"}, {"type":"number", "name":"Vertical Buffer", "id":"vertical_buffer"}], crop_action),
    "crop_square": Action("Smart Crop (square)", [{"type":"number", "name":"Buffer", "id":"buffer"}], crop_square_action),
    "light_levels": Action("Fix Light Levels", [{"type":"number", "name":"Gamma", "id":"gamma"}], light_level_action)
}

settings_predefs = [Setting("Save Path", "save_path", "path"), Setting("Intermediate Image Path", "intermediate_path", "path")]