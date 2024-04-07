from utils import add_file_suffix
from wand.image import Image

def scale_image(filename, width, height):
    new_filename = add_file_suffix(filename, "-resized")
    with Image(filename=filename) as img:
        w = img.width
        h = img.height
        img.resize(width, height)
        img.save(filename= new_filename)
    return new_filename

def scale_action(filename, args):
    width = int(args[0])
    height = int(args[1])
    return scale_image(filename, width, height)
