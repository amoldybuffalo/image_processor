from pathlib import Path
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import GdkPixbuf
from wand.image import Image

def add_file_suffix(filename, suffix):
     p = Path(filename)
     return str(p.parent / Path(p.stem + suffix + p.suffix))
     
def get_midpoint(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    midpoint = (int((x1+x2)/2), int((y1+y2)/2))
    return midpoint

def get_dimensions(filename):
     with Image(filename=filename) as img:
          w = img.width
          h = img.height
          return (w,h)

def get_gtk_image(filename, w, h):
     pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(filename, w, h)
     image = Gtk.Image.new_from_pixbuf(pixbuf)
     return image