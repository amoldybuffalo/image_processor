from wand.image import Image
from utils import add_file_suffix

def light_levels(filename, path, gamma):
    new_filename = add_file_suffix(filename, path, "-levels")
    with Image(filename=filename) as img:
        img.auto_gamma()
        img.auto_level()
        img.level(gamma=2.4)
        img.save(filename=new_filename)
    return new_filename


def light_level_action(filename, path, args):
    gamma = args["gamma"]
    return light_levels(filename, path, gamma)