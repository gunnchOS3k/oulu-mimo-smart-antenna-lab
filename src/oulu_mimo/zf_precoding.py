import numpy as np

def zf_precoder(H):
    return np.linalg.pinv(H)
