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

def RombergIntergration(f, interval, j, k):
    a, b = interval
    
    def I_rombg(f,j,k):
        if k==1:
            n = 2**(j-1)
            I =0
            for interval in segment(n, [a,b]):
                I += Intergrate(f, interval)
            
            return I
        
        I1 = I_rombg(f, j+1, k-1)
        I2 = I_rombg(f, j, k-1)
        C = 4**(k-1)
        
        return (C*I1 - I2)/(C-1)

    return I_rombg(f, j, k)

def rel_err(approx, gt):
    return np.abs((gt - approx)/gt*100)


#Ex 17.1-1
j, k = 1, 2
I = RombergIntergration(f, [a,b], j, k)
print(f"intergration results with j={j}, k={k} romberg intergration : {I}")
print(f"error = {rel_err(I,I_gt)}%")
j, k = 2, 2
I = RombergIntergration(f, [a,b], j, k)
print(f"intergration results with j={j}, k={k} romberg intergration : {I}")
print(f"error = {rel_err(I,I_gt)}%")


#Ex 17.1-2
j, k = 1, 3
I = RombergIntergration(f, [a,b], j, k)
print(f"intergration results with j={j}, k={k} romberg intergration : {I}")
print(f"error = {rel_err(I,I_gt)}%")