from scipy.ndimage.filters import gaussian_filter
import matplotlib.pyplot as plt
import numpy as np

class DataVizulaize:
    
    def __init__(self, model):
        self.model = model
        
    def rgb2gray(self,rgb):
        return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

    def vizualize(self,layer_num, num_kernel,gray=False, gaus_filter=True,sigma = 1,shapeofgrid=(16,8) ):
        if num_kernel%2>0:
            im_h = 8
            im_w = num_kernel+1/2
        else:
            im_h = 8
            im_w = num_kernel/2
            
        #for layer in model.layers:
        #weights = layer.get_weights() # list of numpy arrays
        kernals = self.model.layers[layer_num].get_weights()[0]
        #np.shape(kernals)
        fig, axs = plt.subplots(shapeofgrid[0],shapeofgrid[1], figsize=(15,10))
        fig.subplots_adjust(hspace = .01, wspace=.01)
        axs = axs.ravel()
        for i in range(np.shape(kernals)[3]):
            one_kernal = np.abs(kernals[:,:,:,i])
            one_kernal -= one_kernal.mean() # Post-processes the feature to make it visually palatable
            one_kernal /= one_kernal.std()
            one_kernal *= 64
            one_kernal += 128
            one_kernal= np.clip(one_kernal, 0, 255).astype('uint8')
            if(gray):
                one_kernal =self.rgb2gray(one_kernal)
                
            if gaus_filter:
                one_kernal = gaussian_filter(one_kernal, sigma)
                
            axs[i].imshow(one_kernal,cmap='gray')
            axs[i].axes.get_xaxis().set_ticks([])
            axs[i].axes.get_yaxis().set_ticks([])
            #axs[i].set_title(str(250+i))