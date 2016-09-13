'''Module including useful functions for bootcamp'''

import numpy as np

def ecdf(data):
    '''Computes EDCF from data'''
    x = np.sort(data)
    y = (np.arange(0, len(x)) + 1) / len(x)
    return (x, y)
