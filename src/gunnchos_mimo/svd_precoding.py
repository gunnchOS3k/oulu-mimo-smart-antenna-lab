import numpy as np

def svd_precoder(H):
    U,S,Vh = np.linalg.svd(H)
    return Vh.conj().T, S
