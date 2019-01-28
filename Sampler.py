import numpy as np
class Sampler:
    def __init__(self):
        pass
    
    
#get samoles from each class    
def getSampleEachClass(X_train,Y_train, number_of_sample=20, number_of_class=10):
    itemindex = np.where(Y_train==number_of_class-1)
    X_train_new = X_train[itemindex][0:number_of_sample]
    Y_train_new = Y_train[itemindex][0:number_of_sample]
    for cls in range(number_of_class-1):
        itemindex = np.where(Y_train==cls)
        X_train_new = np.concatenate((X_train_new,
                                      X_train[itemindex][0:number_of_sample]),axis=0)
        Y_train_new = np.concatenate((Y_train_new,
                                       Y_train[itemindex][0:number_of_sample]),axis=0)
    return X_train_new, Y_train_new



        