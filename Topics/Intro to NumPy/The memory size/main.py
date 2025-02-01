import numpy as np

def memory_size(arr):
    return np.array(arr).itemsize * len(arr)
