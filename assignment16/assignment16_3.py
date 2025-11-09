import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

x_list = np.array([0.00, 0.12, 0.22, 0.32, 0.36, 0.40, 0.44, 0.54, 0.64, 0.70, 0.80])
# f_list = f(x_list)

I_gt = 1.640533

def Intergrate(f, interval):
    a, b = interval
    
    I = (b-a) * (f(a) + f(b))/2
    
    return I
    

def rel_err(approx, gt):
    return np.abs((gt - approx)/gt)


I = 0
n = len(x_list)-1
segments = [x_list[i:i+2] for i in range(0,n)]

for interval in segments:
    I += Intergrate(f, interval)
print(f"intergration results with {n} segments : {I}")
print(f"error = {rel_err(I,I_gt)}")
