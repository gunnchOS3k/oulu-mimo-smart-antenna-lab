import numpy as np

def array_factor(theta, d_lambda=0.5, n=8):
    k = 2 * np.pi * d_lambda
    theta = np.atleast_1d(theta)
    n_arr = np.arange(n)[:, None]
    af = np.sum(np.exp(1j * k * n_arr * np.sin(theta)), axis=0)
    return np.abs(af)
