'''
Created on 2017-08-24

@author: mani
'''
import pickle
_image_oneSide = 32
_image_channels = 3
_image_flat_size = _image_oneSide * _image_oneSide *  _image_channels
_base_dir = None

def _unpickle(file_name):
    with open(file_name, 'rb') as fd:
        _dict = pickle.load(fd)
    return _dict

def load_train_data():
    train_data = [[],[]]
    for i in range(5):
        _data = _unpickle(_base_dir+"/data_batch_"+str(i+1))
        train_data[0].extend(_data["data"])
        train_data[1].extend(_data["labels"])
    return train_data
def load_test_data():
    test_data = [[],[]]
    _data = _unpickle(_base_dir+"/test_batch")
    test_data[0].extend(_data["data"])
    test_data[1].extend(_data["labels"])
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
    