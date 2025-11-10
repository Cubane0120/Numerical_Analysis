import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

a = 0
b = 0.8

I_gt = 1.640533


def GaussQuadrature(f, c, x, interval):
    a, b = interval
    
    def f_norm(x_norm):
        x_orin = (b-a)/2*x_norm + (a+b)/2
        return f(x_orin) * (b-a)/2
    
    I = np.sum(c * f_norm(x))
    # print(c * f_norm(x))
    return I

def rel_err(approx, gt):
    return np.abs((gt - approx)/gt*100)


#Ex 17.2-1
#c, x for 2 points
n = 2
c = np.array([1, 1])
x = np.array([-1/np.sqrt(3), 1/np.sqrt(3)])

I = GaussQuadrature(f, c, x, [a,b])
print(f"intergration results with {n} points Gauss quadrature : {I}")
print(f"error = {rel_err(I,I_gt)}%")

#Ex 17.2-2
#c, x for 3 points
n = 3
c = np.array([5/9, 8/9, 5/9])
x = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])

I = GaussQuadrature(f, c, x, [a,b])
print(f"intergration results with {n} points Gauss quadrature : {I}")
print(f"error = {rel_err(I,I_gt)}%")
