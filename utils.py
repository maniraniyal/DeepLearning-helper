import bcolz
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def save_array(rootdir, array):
    c=bcolz.carray(array, rootdir=rootdir, mode='w')
    c.flush()
    
def load_array(rootdir):
    return bcolz.open(rootdir)[:]

def plotImageFromFiles(filenames,col=3,DPI=200):
    total_images = len(filenames)
    fig = plt.figure(dpi=DPI)
    for i,f in enumerate(filenames):
        plt.subplot(int(total_images/col)+1,col,i+1)
        plt.imshow(np.asarray(Image.open(filenames[i])))

def plotImageFromListOfArrays(arraylist,col=3,DPI=200):
    total_images = len(arraylist)
    fig = plt.figure(dpi=DPI)
    for i,arr in enumerate(arraylist):
        plt.subplot(int(total_images/col)+1,col,i+1)
        plt.imshow(arr)
