import numpy as np

def steering_ula(theta, n=8, d=0.5):
    return np.exp(1j*2*np.pi*d*np.arange(n)*np.sin(theta))
