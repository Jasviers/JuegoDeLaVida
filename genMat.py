import numpy as np
import random

def genMat(dim):
    array = np.ones((dim*dim), dtype = bool)
    array2 = np.array(list(map(rand, array))).reshape(dim, dim)
    return list(array2)

def rand(elem):
    if random.randint(0,1) > 0:
        return True
    else:
        return False
