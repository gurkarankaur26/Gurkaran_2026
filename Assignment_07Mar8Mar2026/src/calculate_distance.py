import numpy as np

def calculate_distance(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.sum((a-b)**2)