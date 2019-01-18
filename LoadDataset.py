import os
import matplotlib.image as misc
from sklearn.utils import shuffle
import numpy as np


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
        i = 0
        Xdata = []
        Ydata = []

        for dir in dir_list:
            current_dir = self.address + '/' + dir;
            all_image = os.listdir(current_dir)
            for image in all_image:
                image_add = current_dir + '/' + image
                image = misc.imread(image_add)[:,:,:3]
                Xdata.append(image)
                Ydata.append(i)
            i = i + 1
            print(str(dir), ' directory images are fetched!!! ')
#         print('Files in current directory: ', os.listdir(current_dir))
        return Xdata, Ydata
# Shuffeling the data
    def shuffle_data(self , X, y):
        return shuffle(X, y)



