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


def flip_image(img, HR=True, VER=True, HR_VER=True, ROT90=True, ROT90_HR=True):
    """
    This function create flip images
    :param img: np array
    :param HR: if true, flip the img horizontally
    :param VER: if true, flip the img vertically
    :param HR_VER: if true, flip the img horizontally then vertically
    :param ROT90: if true, rotate 90 degree anticlockwise
    :param ROT90_HR: if true, rotate 90 degree anticlockwise then horizontal flip
    :return: dict with params as key ig they were true
    """
    flip_dict = {}
    if HR:
        flip_dict["HR"] = np.fliplr(img)
    if VER:
        flip_dict["VER"] = np.flipud(img)
    if HR_VER:
        flip_dict["HR_VER"] = np.flipud(np.fliplr(img))
    if ROT90:
        flip_dict["ROT90"] = np.rot90(img)
    if ROT90_HR:
        flip_dict["ROT90_HR"] = np.fliplr(np.rot90(img))
    return flip_dict


def save_flip_arrays_as_image_files(path_to_save, basefile_name, filp_array_dict):
    """
    This function saves flipped arrays as image file.
    :param path_to_save: directory where the image will be saved
    :param basefile_name: original file name with extension. Not abs/relative path
    :param filp_array_dict: flip_image() return object
    :return:
    """
    if not os.path.isdir(path_to_save):
        print("There is not such dir: " + path_to_save)
        os.mkdir(path_to_save)
        print("Created dir: " + path_to_save)
    for header in filp_array_dict:
        img = Image.fromarray(filp_array_dict[header])
        img.save(path_to_save + "/" + header + "_" + basefile_name)


def save_torch_weights_from_model(torch_model, weight_filename):
    """
    Save torch model weights
    :param torch_model:
    :param weight_filename:
    :return: None
    """
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
