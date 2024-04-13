import json
import platform
from pathlib import Path
import os

def get_settings_path():
    operating_system = platform.system()
    if operating_system == "Linux":
        path = Path.home() / Path(".config/image_processor")
        path.mkdir(parents=True, exist_ok=True)
        path = path / "settings.json"
        if not path.exists():
            open(path, 'a').close()
        return str(path)
    elif operating_system == "Windows":
        path = Path.home() / Path("AppData/Local/image_processor")
        path.mkdir(parents=True, exist_ok=True)
        path = path / "settings.json"
        if not path.exists():
            open(path, 'a').close()
        return str(path)


def read_setting(key):
    path = get_settings_path()
    with open(path, "r") as fp:
        try:
            settings = json.load(fp)
            return settings[key]
        except:
            return None

def write_setting(key, value):
    path = get_settings_path()
    with open(path, "r") as fp:
        try:
            settings = json.load(fp)
        except:
            settings = {}
    with open(path, "w") as fp:
        settings[key] = value
        json.dump(settings, fp)



