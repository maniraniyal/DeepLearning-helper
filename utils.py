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
import random
import torch
import shutil


def save_torch_weights_from_model(torch_model, weight_filename):
    if os.path.exists(weight_filename):
        for i in range(10):
            tmp_file = weight_filename + '_' + str(random.randint(1, 1000))
            if not os.path.exists(tmp_file):
                break
        else:
            raise Exception("Could not generate unique random file")
        torch.save(torch_model.state_dict(), tmp_file)
        # os.remove(weight_file)
        # os.rename(tmp_file, weight_file)
        shutil.move(tmp_file, weight_filename)
    else:
        torch.save(torch_model.state_dict(), weight_filename)


def convert_gray_images_to_rgb(directories_list, out_dir_suffix="_RGB", image_reg="/*.jpg"):
    """
    convert_grayImages_to_RGB assumes that directory has only grayscale or RGB images, not RGBA.
    """
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
                               

def convert_rgb_to_gray_images(directories_list, out_dir_suffix="_GRAY", image_reg="/*.jpg"):
    """
    convert_RGB_to_grayImages assumes that directory has only grayscale or RGB images, not RGBA.
    """
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
                    

def save_array(rootdir, array):
    """
    saves the numpy array to the disk.
    """
    c=bcolz.carray(array, rootdir=rootdir, mode='w')
    c.flush()


def load_array(rootdir):
    """
    Loads numpy array from disk
    """
    return bcolz.open(rootdir)[:]


def plot_image_from_files(filenames, col=3, DPI=200):
    """
    plotImageFromFiles plot images in row and column, given filename with abs/relaive path
    """
    total_images = len(filenames)
    fig = plt.figure(dpi=DPI)
    for i,f in enumerate(filenames):
        plt.subplot(int(total_images/col)+1,col,i+1)
        plt.imshow(np.asarray(Image.open(filenames[i])))


def plot_image_from_list_of_arrays(arraylist, col=3, DPI=200):
    """
    plotImageFromListOfArrays plot images in row and column, given numpyarray(3,x,x) as list.
    """
    total_images = len(arraylist)
    fig = plt.figure(dpi=DPI)
    for i, arr in enumerate(arraylist):
        plt.subplot(int(total_images/col)+1,col,i+1)
        plt.imshow(arr)
