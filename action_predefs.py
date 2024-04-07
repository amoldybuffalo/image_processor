from actions import Action
from modules.scale import scale_action
from modules.crop import crop_action, crop_square_action
action_predefs = {
    "scale": Action("Scale", [{"type":"input", "name":"width"}, {"type":"input", "name":"height"}], scale_action),
    "crop": Action("Smart Crop", [{"type":"input", "name":"width_buffer"}, {"type":"input", "name":"height_buffer"}], crop_action),
    "crop_square": Action("Smart Crop Square", [{"type":"input", "name":"buffer"}], crop_square_action)
}