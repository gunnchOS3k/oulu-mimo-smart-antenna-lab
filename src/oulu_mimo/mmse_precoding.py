import numpy as np

def mmse_precoder(H, snr=10):
    nt = H.shape[1]
    return np.linalg.inv(H.conj().T@H + nt/(10**(snr/10))*np.eye(nt)) @ H.conj().T
