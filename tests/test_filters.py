from gunnchos_mimo.array_factor import array_factor
import numpy as np

def test_af():
    assert array_factor(0.0) > 0
