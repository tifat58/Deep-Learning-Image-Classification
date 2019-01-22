import os
import matplotlib.image as misc
from sklearn.utils import shuffle
import numpy as np
import scipy
from skimage.transform import rescale, resize, downscale_local_mean


class LoadData:
    # give the relative path of data set in constructor.

    def __init__(self, address):
        if os.listdir(address):
            print('Dataset directory added')
            print(os.listdir(address))
            self.address = address
        else:
            print('Give proper directory name')

    def generate_data(self):
        dir_list = os.listdir(self.address)
        Xdata = []
        Ydata = []
        i = 0
        for dir in dir_list:
            cls_lbl = int(dir[1])
            current_dir = self.address + '/' + dir;
            all_image = os.listdir(current_dir)
            for image in all_image:
                image_add = current_dir + '/' + image
                image = misc.imread(image_add)[:,:,:3]
                image_r = resize(image, (227,227,3))
                Xdata.append(image_r)

#                 print(image_r.shape)

                Ydata.append(cls_lbl)
            i = i + 1

            print(str(dir), ' directory images are fetched!!! ')
#         print('Files in current directory: ', os.listdir(current_dir))


        #print('Files in current directory: ', os.listdir(current_dir))
        return Xdata, Ydata
# Shuffeling the data
    def shuffle_data(self , X, y):
        return shuffle(X, y)

    def generate_data_2cls(self, dir_list=['c0','c1','c2','c3','c4','c5','c6','c7','c8','c9']):
        Xdata = []
        Ydata = []
        i = 0
        for dir in dir_list:
            cls_lbl = int(dir[1])
            current_dir = self.address + '/' + dir;
            all_image = os.listdir(current_dir)
            for image in all_image:
                image_add = current_dir + '/' + image
                image = misc.imread(image_add)[:,:,:3]
                image_r = scipy.misc.imresize(image, (227,227,3))
                Xdata.append(image_r)
                #print(image_r.shape)
                Ydata.append(cls_lbl)
            i = i + 1

            print(str(dir), ' directory images are fetched!!! ')
#         print('Files in current directory: ', os.listdir(current_dir))
        return Xdata, Ydata

