import numpy as np
import matplotlib.pyplot as plt


x_target = 2
y_gt = 0.6931472

def LinearInterpolatgion(x_t, Interval, InvervalVal):
    x_l, x_r = Interval
    y_l, y_r = InvervalVal
    
    return (y_r - y_l) / (x_r - x_l) * (x_t - x_l)

def error(pred, gt):
    return np.abs((pred-gt)/gt)
    
#cond 1
interval = (1, 6)
intervalVal = (0, 1.791759)
y_pred1 = LinearInterpolatgion(x_target, interval, intervalVal)
err1 = error(y_pred1, y_gt)

#cond 2
interval = (1, 4)
intervalVal = (0, 1.386294)
y_pred2 = LinearInterpolatgion(x_target, interval, intervalVal)
err2 = error(y_pred2, y_gt)

print(y_pred1, y_pred2)
print(err1, err2)