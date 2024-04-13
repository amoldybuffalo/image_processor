from utils import add_file_suffix
from wand.image import Image

def scale_image(filename, path, width, height):
    scaled_filename = add_file_suffix(filename, path, "-resized")
    print(scaled_filename)
    with Image(filename=filename) as img:
        w = img.width
        h = img.height
        img.resize(width, height)
        img.save(filename=scaled_filename)
    return scaled_filename

def scale_action(filename, path, args):
    width = int(args["width"])
    height = int(args["height"])
    return scale_image(filename, path, width, height)
