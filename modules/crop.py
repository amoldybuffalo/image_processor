from bounds import get_foreground_bounds
from pathlib import Path
from wand.image import Image
from wand.display import display
from pathlib import Path
import math

def crop(filename, width_buffer, height_buffer):
    bounds = get_foreground_bounds(filename)
    x1 = bounds[0][0] 
    y1 = bounds[0][1]
    x2 = bounds[1][0]
    y2 = bounds[1][1]
    p = Path(filename)
    cropped_filename = str(p.parent / Path(p.stem + "-cropped" + p.suffix))
    with Image(filename=filename) as img:
        w = img.width 
        h = img.height
        left = x1 - width_buffer if x1 - width_buffer > 0 else 0
        right = x2 + width_buffer if x2 + width_buffer < w else w
        top = y1 - height_buffer if y1 - height_buffer > 0 else 0
        bottom = y2 + height_buffer if y2 + height_buffer < h else h
        img.crop(left, top, right, bottom)
        img.save(filename=cropped_filename)
    return cropped_filename

def crop_square(filename, min_buffer):
    bounds = get_foreground_bounds(filename)
    x1 = bounds[0][0] 
    y1 = bounds[0][1]
    x2 = bounds[1][0]
    y2 = bounds[1][1]
    bounded_width = x2 - x1
    bounded_height = y2 - y1
    max_length = max([bounded_width, bounded_height])

    p = Path(filename)
    cropped_filename = str(p.parent / Path(p.stem + "-cropped" + p.suffix))
    with Image(filename=filename) as img:
        w = img.width 
        h = img.height
        if max_length == bounded_width:
            left = x1 - min_buffer if x1 - min_buffer > 0 else 0
            right = x2 + min_buffer if x2 + min_buffer < w else w

            top_buffer_expression = math.floor(y1 - (2*min_buffer + bounded_width - bounded_height) / 2) 
            top = top_buffer_expression if top_buffer_expression > 0 else 0

            bottom_buffer_expression = math.floor(y2 + (2*min_buffer + bounded_width - bounded_height) / 2) 
            bottom = bottom_buffer_expression if bottom_buffer_expression < h else h

        elif max_length == bounded_height:
            top = y1 - min_buffer if y1 - min_buffer > 0 else 0
            bottom = y2 + min_buffer if y2 + min_buffer < h else h 

            left_buffer_expression = math.floor(x1 - (2 * min_buffer + bounded_height - bounded_width) / 2 ) 
            left = left_buffer_expression if left_buffer_expression > 0 else 0

            right_buffer_expression = math.floor(x2 + (2*min_buffer + bounded_height - bounded_width) / 2) 
            right = right_buffer_expression if right_buffer_expression < w else w

        print(f"Top: {top}\n Bottom: {bottom}\n Right: {right}\n Left: {left}\n")
        img.crop(left, top, right, bottom)
        img.save(filename=cropped_filename)
    return cropped_filename

def crop_action(filename, args):
    width_buffer = int(args[0])
    height_buffer = int(args[1])
    return crop(filename, width_buffer, height_buffer)

def crop_square_action(filename, args):
    buffer = int(args[0])
    return crop_square(filename, buffer)

