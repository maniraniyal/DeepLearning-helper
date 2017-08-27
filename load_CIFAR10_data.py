'''
Created on 2017-08-24
Call load_data() function with directory where the CIFAR10 data-set is extracted.
Return:
    training data [images(nd.array), labels(nd.array)](list)
    test data    [images(nd.array), labels(nd.array)](list)
    mapping_of_classes [name of classes](list)
@author: mani
'''
import pickle
import numpy as np
from scipy import sparse
_base_dir = None

def _unpickle(file_name):
    with open(file_name, 'rb') as fd:
        _dict = pickle.load(fd)
    return _dict

def load_train_data():
    train_data = [None,None]
    for i in range(5):
        _data = _unpickle(_base_dir+"/data_batch_"+str(i+1))
        if type(train_data[0]) == type(None):
            train_data[0] = _data["data"]
        else:
            print(train_data[0].shape)
            train_data[0] = np.concatenate((train_data[0],_data["data"]),axis=0)
        if type(train_data[1]) == type(None):
            train_data[1] = np.array(_data["labels"])
        else:
            train_data[1] = np.concatenate((train_data[1],np.array(_data["labels"])),axis=0)

    return train_data
def load_test_data():
    test_data = [None,None]
    _data = _unpickle(_base_dir+"/test_batch")
    test_data[0] = _data["data"]
    test_data[1] = np.array(_data["labels"])
    return test_data
def load_label_map():
    label_names = _unpickle(_base_dir+"/batches.meta")["label_names"]
    return label_names
def load_data(base_dir):
    global _base_dir
    _base_dir = base_dir
    train = load_train_data()
    test = load_test_data()
    label_map = load_label_map()
    return train,test,label_map
    
if __name__ == "__main__":
    train,test,classes = load_data("../../Downloads/cifar-10-batches-py")
    print ("training set shape: ", train[0].shape)
    print ("test set shape: ", test[0].shape)
    print ("classes set shape: ", len(classes))
