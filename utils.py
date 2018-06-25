import bcolz
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import glob
import os
import cv2
import numpy as np
from PIL import Image
from shutil import copyfile

"""
convert_grayImages_to_RGB assumes that directory has only grayscale or RGB images, not RGBA.
"""
def convert_grayImages_to_RGB(directories_list, out_dir_suffix="_RGB", image_reg="/*.jpg"):
    for d in directories_list:
        os.mkdir(d+out_dir_suffix)
        for filename in glob.glob(d+image_reg):
            if os.path.isfile(filename):
                img = Image.open(filename)
                if len(np.array(img).shape) != 3:
                    img = Image.fromarray(cv2.cvtColor(np.array(img), cv2.COLOR_GRAY2RGB))
                    img.save(d+out_dir_suffix+filename.split("/")[-1])
                else:
                    copyfile(filename, d+out_dir_suffix+filename.split("/")[-1])
                               

"""
convert_RGB_to_grayImages assumes that directory has only grayscale or RGB images, not RGBA.
"""
def convert_RGB_to_grayImages(directories_list, out_dir_suffix="_GRAY", image_reg="/*.jpg"):
    for d in directories_list:
        os.mkdir(d+out_dir_suffix)
        for filename in glob.glob(d+image_reg):
            if os.path.isfile(filename):
                img = Image.open(filename)
                if len(np.array(img).shape) == 3:
                    img = Image.fromarray(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY))
                    img.save(d+out_dir_suffix+filename.split("/")[-1])
                else:
                    copyfile(filename, d+out_dir_suffix+filename.split("/")[-1])
                    
"""
saves the numpy array to the disk.
"""
def save_array(rootdir, array):
    c=bcolz.carray(array, rootdir=rootdir, mode='w')
    c.flush()

"""
Loads numpy array from disk
"""
def load_array(rootdir):
    return bcolz.open(rootdir)[:]

"""
plotImageFromFiles plot images in row and column, given filename with abs/relaive path
"""
def plotImageFromFiles(filenames,col=3,DPI=200):
    total_images = len(filenames)
    fig = plt.figure(dpi=DPI)
    for i,f in enumerate(filenames):
        plt.subplot(int(total_images/col)+1,col,i+1)
        plt.imshow(np.asarray(Image.open(filenames[i])))

"""
plotImageFromListOfArrays plot images in row and column, given numpyarray(3,x,x) as list.
"""
def plotImageFromListOfArrays(arraylist,col=3,DPI=200):
    total_images = len(arraylist)
    fig = plt.figure(dpi=DPI)
    for i,arr in enumerate(arraylist):
        plt.subplot(int(total_images/col)+1,col,i+1)
        plt.imshow(arr)
