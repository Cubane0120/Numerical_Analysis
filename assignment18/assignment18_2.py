import numpy as np
import matplotlib.pyplot as plt

h1 = 0.5
h2 = 0.25
x0 = 0.5
df_gt = -0.9125

def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

def D(h, x):
    return (f(x+h) - f(x-h)) / (2*h)

def rel_err(approx, gt=df_gt):
    return np.abs((gt - approx)/gt*100)

D_h1 = D(h1, x0)
D_h2 = D(h2, x0)
D_extra = (4*D_h2 - D_h1)/3

print(f"D_h1 value = {D_h1}\t error : {rel_err(D_h1)}%\t h1 = {h1}")
print(f"D_h2 value = {D_h2}\t error : {rel_err(D_h2)}%\t h2 = {h2}")
print(f"Richardson Extrapolation value = {D_extra}\t error : {rel_err(D_extra)}%")