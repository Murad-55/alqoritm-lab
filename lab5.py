import numpy as np
from scipy.optimize import brentq

# Tənliyin funksiyası
def f(x):
    return x**2 - np.cos(x)

# İnterval daxilində kök tapılır
root = brentq(f, 0.0, 1.0)

print(f"Kök: {root}")
