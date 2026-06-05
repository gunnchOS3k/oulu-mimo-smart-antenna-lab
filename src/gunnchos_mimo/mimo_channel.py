import numpy as np

def rayleigh_mimo(nr, nt, rng=None):
    rng = rng or np.random.default_rng(0)
    return (rng.standard_normal((nr,nt)) + 1j*rng.standard_normal((nr,nt)))/np.sqrt(2)
