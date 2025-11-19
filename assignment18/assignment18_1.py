import numpy as np
import matplotlib.pyplot as plt

h = 0.25
x0 = 0.5
df_gt = -0.9125

def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

def rel_err(approx, gt=df_gt):
    return (gt - approx)/gt*100

#Backward
f_b = (f(x0) - f(x0-h)) / h
f_b_h = (3*f(x0) - 4*f(x0-h) + f(x0-2*h)) / (2*h)

#Centered
f_c = (f(x0+h) - f(x0-h)) / (2*h)
f_c_h = (-f(x0+2*h) + 8*f(x0+h) - 8*f(x0-h) + f(x0-2*h)) / (12*h)

#Forward
f_f = (f(x0+h) - f(x0)) / h
f_f_h = (-f(x0+2*h) + 4*f(x0+h) - 3*f(x0)) / (2*h)

print(f"Forward value = {f_f}\t error : {rel_err(f_f)}%")
print(f"Backward value = {f_b}\t error : {rel_err(f_b)}%")
print(f"Centered value = {f_c}\t error : {rel_err(f_c)}%")

print(f"(high-accuracy) Forward value = {f_f_h}\t error : {rel_err(f_f_h)}%")
print(f"(high-accuracy) Backward value = {f_b_h}\t error : {rel_err(f_b_h)}%")
print(f"(high-accuracy) Centered value = {f_c_h}\t error : {rel_err(f_c_h)}%")