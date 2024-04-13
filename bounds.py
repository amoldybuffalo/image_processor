# import required libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
import wand
from wand.image import Image
from wand.display import display
from utils import add_file_suffix
from utils import get_dimensions
from modules.scale import scale_image


# from matplotlib import pyplot as plt
def get_foreground_bounds(filename):
    w1, h1 = get_dimensions(filename)
    scaled_filename = scale_image(filename, 500, int(h1/w1 * 500))
    w2, h2 = get_dimensions(scaled_filename)
    scale_factor_x = w2/w1 
    scale_factor_y = h2/h1
    # read input image
    img = cv2.imread(scaled_filename)
    print(f"Image dimensions: {img.shape}" )
    # define mask
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    print(f"H2 is {h2}")
    # define rectangle
    rect = (80, int(h2/5), 400, int(h2 - (h2/3.5)))
    print(rect)
    # apply grabCut method to extract the foreground
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,120,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    # display the extracted foreground image

    h = img.shape[0]
    w = img.shape[1]

    x_values = []
    y_min = -1
    x_min = -1
    y_max = -1
    x_max = -1
    print("Got to here")
    line_started = False
    for y in range(0, h):
        for x in range(0, w):
            if np.any(img[y,x] > 0):
                line_started = True
                if y_min == -1:
                    y_min = y
                else:
                    y_max = y
                x_values.append(x)
                #img[y,x] = [255,255,255]
            else:
                if line_started:
                    x_values.append(x)
                    line_started = False
    print("Got here")

    x_min = min(x_values)
    x_max = max(x_values)
    img[y_min, x_min] = [255,0,0]
    img[y_max, x_max] = [255,0,0]  

    plt.imshow(img),plt.show()
    return [(int(x_min/scale_factor_x),int(y_min/scale_factor_y)), (int(x_max/scale_factor_x), int(y_max/scale_factor_y))]
