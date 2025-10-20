import numpy as np
import matplotlib.pyplot as plt


b_list = []
x_vals = []
DP = []

def add_data(x,y, b_list=b_list, x_vals=x_vals, DP=DP):
    N = len(DP)
    x_vals.append(x)
    DP.append(y)
    # print(N)
    def combine(x1,x2,y1,y2):
        return (y2 - y1)/(x2 - x1)
    
    for i in range(N-1,-1,-1):
        DP[i] = combine(x_vals[i],x_vals[-1],DP[i],DP[i+1])
    
    b_list.append(DP[0])
    # print("==================")
    # print(x_vals)
    # print(DP)
    # print(b_list)
# breakpoint()

def interpolate(x0, b_list=b_list, x_vals=x_vals):
    N = len(b_list)
    
    return_val = 0
    x_term = 1
    for i in range(N):
        return_val += b_list[i] * x_term
        x_term = x_term * (x0 - x_vals[i])
    # print(b_list)
    return return_val   
    
x0 = 2
gt = np.log(2)
def error(pred, gt=gt):
    return np.abs((pred-gt)/gt)

x_ = [1, 4, 6]
y_ = [0, 1.386294, 1.791759]

for i in range(len(x_)):
    add_data(x_[i],y_[i])

pred = interpolate(x0)
err = error(pred)
print(pred, err)

print("==========")
add_data(5, 1.609438)
pred = interpolate(x0)
err = error(pred)
print(pred, err)