import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

a = 0
b = 0.8

I_gt = 1.640533

def Intergrate(f, interval):
    a, b = interval
    
    I = (b-a) * (f(a) + f(b))/2
    
    return I
    
    
def segment(n, interval):
    a, b = interval
    h = (b - a) / n
    
    return [[a+h*i, a+h*(i+1)] for i in range(0,n)]

def rel_err(approx, gt):
    return (gt - approx)/gt

def Ea(interval, n, ddf=-60):
    a, b = interval
    return -(b-a)**3 / (12*(n**2)) * ddf


#Ex 16.1-1
n = 1
I = 0
for interval in segment(n, [a,b]):
    I += Intergrate(f, interval)
print(f"intergration results with {n} segments : {I}")
print(f"error = {rel_err(I,I_gt)}")

#Ex 16.1-2
print("================")
n = 2
I = 0
for interval in segment(n, [a,b]):
    I += Intergrate(f, interval)
print(f"intergration results with {n} segments : {I}")
print(f"error = {rel_err(I,I_gt)}")
print(f"Ea = {Ea([a,b], n)}")