import numpy as np

class AddNoise:
    
    def __init__(self):
        pass
        
    def add_noise(self,data, mean = [0, 0], cov = [[100, 0], [0, 100]]):
        height = data.shape[0]
        x_axis = data.shape[1]
        y_axis = data.shape[2]
        z_axis = data.shape[3]
        mean = [0, 0]
        cov = [[100, 0], [0, 100]]  # diagonal covariance
        Z = np.random.multivariate_normal(mean, cov, (x_axis,y_axis,z_axis))
        img_noise =[Z[:,:,:,1]]
        for i in range (height-1):
            X = np.random.multivariate_normal(mean, cov, (x_axis,y_axis,z_axis))
            X = Z[:,:,:,1]
            img_noise = np.concatenate((img_noise,[X]), axis=0)


        return img_noise + data

    def random_output_label(self,Y_train, percentage=10):
        length_until = np.floor(len(Y_train)* percentage/100)
        index_1 =np.int(np.random.choice(np.arange(0,np.shape(Y_train)[0]-length_until)))
        index_2 =np.int(index_1 + length_until)
        print(type(index_1),type(index_2))
        Y_mod = Y_train[index_1:index_2]
        Y_mod = np.array(Y_mod)
        np.random.shuffle(Y_mod)
        #print('shape of mask', np.arange(index_1,index_2+1))
        #print('shape of data', np.array(Y_mod))
        #Y_train_new = np.place(np.array(Y_train),np.arange(index_1,index_2+1),np.array(Y_mod))
        Y_train[index_1:index_2] = Y_mod 
        return Y_train

        
        
    