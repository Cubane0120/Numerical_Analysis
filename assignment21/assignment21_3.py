import numpy as np
import matplotlib.pyplot as plt


x_0 = np.array([1.5, 3.5])

def f(x):
    x1, x2 = x
    f1 = x1**2 + x1*x2 - 10
    f2 = x2 + 3*x1*(x2**2) - 57

    return np.array([f1, f2])

def g1(x):
    x1, x2 = x
    return np.sqrt(10 - x1*x2)

def g2(x):
    x1, x2 = x
    return np.sqrt((57 - x2)/(3*x1))

def Succesive_Substitution(x_0, num_iter):
    x_prev = x_0
    x_appx = x_prev
    print(f"initial\t x : \n{x_0}")
    for _ in range(num_iter):        
        x_appx[0] = g1(x_appx)
        x_appx[1] = g2(x_appx)
        
        x_prev = x_appx
        print(f"iter {_+1}\t x : \n{x_appx}")
    return x_appx
    

x_appx = Succesive_Substitution(x_0, 10)
print(x_appx)