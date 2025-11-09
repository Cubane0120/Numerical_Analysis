import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

a = 0
b = 0.8

I_gt = 1.640533

def Intergrate(f, interval):
    if len(interval)==3:
        x0, x1, x2 = interval
        
        I = (x2-x0) * (f(x0) + 4*f(x1) + f(x2)) / 6
        return I
    elif len(interval)==4:
        x0, x1, x2, x3 = interval
        
        I = (x3-x0) * (f(x0) + 3*f(x1) + 3*f(x2) + f(x3)) / 8
        return I
    else:
        raise 0
    
    
def segment(n, interval):
    a, b = interval
    h = (b - a) / n
    segments = [a+h*i for i in range(0,n+1)]
    
    if n%2==0 and n >= 2:
        return [segments[2*i:2*i+3] for i in range(0,n//2)]
    if n%2!=0 and n >= 3:
        return [segments[2*i:2*i+3] for i in range(0,(n-3)//2)] + [segments[-4:]]
    

def rel_err(approx, gt):
    return np.abs((gt - approx)/gt)

def Ea(interval, n, ddf=-2400):
    a, b = interval[0], interval[-1]
    return -(b-a)**5 / (180*(n**4)) * ddf


#Ex 16.2-1
n = 2
I = 0

for interval in segment(n, [a,b]):
    I += Intergrate(f, interval)
print(f"intergration results with {n} segments : {I}")
print(f"error = {rel_err(I,I_gt)}")

#Ex 16.2-2
n = 4
I = 0

for interval in segment(n, [a,b]):
    I += Intergrate(f, interval)
print(f"intergration results with {n} segments : {I}")
print(f"error = {rel_err(I,I_gt)}")
print(f"Ea = {Ea([a,b], n)}")

#Ex 16.2-3
n = 3
I = 0

for interval in segment(n, [a,b]):
    I += Intergrate(f, interval)
print(f"intergration results with {n} segments : {I}")
print(f"error = {rel_err(I,I_gt)}")
#Ex 16.2-4
n = 5
I = 0

for interval in segment(n, [a,b]):
    I += Intergrate(f, interval)
print(f"intergration results with {n} segments : {I}")
print(f"error = {rel_err(I,I_gt)}")