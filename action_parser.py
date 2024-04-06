import json
import os
from actions import Action
import crop
functions = {"crop":crop.crop_action}

def read_json_action(filename):
    with open(filename, "r") as f:
        dict = json.loads(f.read())
        settings = settings 

def read_dir(dir):
    files = []
    contents = os.listdir(dir)
    for item in contents:
        files.append(dir + "/" + str(item))


read_dir("./actions")
read_json_action("./actions/crop.json")
