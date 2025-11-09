import numpy as np
import matplotlib.pyplot as plt

def T(x,y):
    return 2*x*y + 2*x - x**2 - 2*y**2 + 72


def Intergrate(f, interval):
    a, b = interval
    
    I = (b-a) * (f(a) + f(b))/2
    
    return I

def I_x(T, y_val):
    def F(x):
        return T(x, y_val)
    return F

def I_y(T, interval_x, n):
    segments_x = [interval_x[i:i+2] for i in range(0,n)]
        
    def F(y):
        I = 0
        for int_x in segments_x:
            # print(int_x)
            I += Intergrate(I_x(T, y), int_x)
        
        return I
    return F
    
def Intergrate_2dim(T, interval_x, interval_y, n):
    segments_y = [interval_y[i:i+2] for i in range(0,n)]
    
    I = 0
    for int_y in segments_y:
        # print(int_y)
        I += Intergrate(I_y(T, interval_x, n), int_y)
    return I

def rel_err(approx, gt):
    return np.abs((gt - approx)/gt)


n = 2#500
X, Y = 8, 6
interval_x = [X*i/n for i in range(0,n+1)]
interval_y = [Y*i/n for i in range(0,n+1)]

I = Intergrate_2dim(T, interval_x, interval_y, n)

print(f"multi-dimensional intergration results with {n} segments : {I}")
print(f"average temperature : {I/(X*Y)}")