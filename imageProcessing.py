import glob
import os
import cv2
import numpy as np
from PIL import Image
from shutil import copyfile

"""
If some images just have 1 channel(grayscale), this fuction will turn them into 3 channels images
convert_imgs_in_dir = list of directories, 
suffix=new directory sufix, 
image_type=image file type
"""
def convertGrayTo3Channel(convert_imgs_in_dir=['train','test'], suffix="_3channel", image_type="jpg"): 
    for d in convert_imgs_in_dir:
        os.mkdir(d+suffix) #create parallal directory
        for filename in glob.glob(d+'/*.'+image_type):
            if os.path.isfile(filename):
                img = Image.open(filename)
                if len(np.array(img).shape) != 3:
                    img = Image.fromarray(cv2.cvtColor(np.array(img), cv2.COLOR_GRAY2RGB))
                    img.save(d+'_RGB/'+filename.split("/")[-1])
                else:
                    copyfile(filename, d+suffix+'/'+filename.split("/")[-1])
