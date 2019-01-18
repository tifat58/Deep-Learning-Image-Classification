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
                Xdata.append(image)
                Ydata.append(cls_lbl)
            i = i + 1
<<<<<<< HEAD
            print(str(dir), ' directory images are fetched!!! ')
#         print('Files in current directory: ', os.listdir(current_dir))
=======

        #print('Files in current directory: ', os.listdir(current_dir))
>>>>>>> f7c9c129387a9915fda9aa7a17ba97e8d6634912
        return Xdata, Ydata
# Shuffeling the data
    def shuffle_data(self , X, y):
        return shuffle(X, y)



