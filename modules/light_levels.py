from wand.image import Image
from utils import add_file_suffix

def auto_light_levels(filename):
    new_filename = add_file_suffix(filename, "-level-adjusted")
    with Image(filename=filename) as img:
        img.auto_gamma()
        img.auto_level()
        img.level(gamma=2.4)
        img.save(filename=new_filename)
    return new_filename

auto_light_levels("image.jpg")