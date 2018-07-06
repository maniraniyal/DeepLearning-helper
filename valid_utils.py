from collections import defaultdict
import random
import numpy as np


def dict_from_filename_and_class_mapping(imgs_data, img_col=0, class_col=1):
    """
    It create image class to image file mapping
    :param imgs_data: data
    :param img_col: image col index
    :param class_col: image class index
    :return: defaultdict(list)
    """
    class_default_dict = defaultdict(list)
    for idx, row in enumerate(imgs_data):
        if img_col == 0 and class_col == 1:
            img, img_class = row
        elif img_col == 1 and class_col == 0:
            img_class, img = row
        else:
            raise Exception("can't handle input params!")
        class_default_dict[img_class] += [(idx, img)]
    return class_default_dict


def get_img_validation_idx_based_on_class_percent(imgs_data, per=20, img_col=0, class_col=1):
    """
    Get Validation Indexs for image csv data with class wise percentage.
    :param imgs_data: numpy array
    :param per: validation data percentage for each class
    :param img_col: array index for images
    :param class_col: array index for classes
    :return: list of [validation-index, img]
    """
    if per >= 100:
        raise Exception("Please select validation percentage less than 100!")
    val_idxs = []
    class_dict = dict_from_filename_and_class_mapping(imgs_data, img_col=img_col, class_col=class_col)
    for img_class, idx_n_img_list in class_dict.items():
        val_idxs.extend(random.sample(idx_n_img_list, len(idx_n_img_list) * per // 100))
    return val_idxs


def get_train_valid_data(map_data_np):
    """
    Divide training and validation data
    :param map_data_np: numpy array
    :return: training data, validation data
    """
    val_idxs = get_img_validation_idx_based_on_class_percent(imgs_data=map_data_np)
    val_idxs = [idx for idx, img in val_idxs]
    mask = np.zeros(len(map_data_np), dtype=bool)
    mask[val_idxs] = True
    return map_data_np[~mask], map_data_np[mask]
