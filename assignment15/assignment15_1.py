import numpy as np
import matplotlib.pyplot as plt


x_list = [3.0, 4.5, 7.0, 9.0]
y_list = [2.5, 1.0, 2.5, 0.5]

x_target = 5

def find_adjacent(x0, x_list=x_list):
    min_i, max_i = 0, len(x_list)-1
    if x0 < x_list[min_i] or x0 > x_list[max_i]:
        raise "extrapolation"
    
    while (max_i - min_i) > 0:
        i = (min_i+max_i)//2
        if x0 < x_list[i]:
            max_i = i
        elif x0 > x_list[i+1]:
            min_i = i
        else:
            return i, i+1


def calculate_y(x0):
    i, j = find_adjacent(x0)
    x1, x2, f1, f2 = x_list[i], x_list[j], y_list[i], y_list[j]
    return f1 + (f2-f1)/(x2-x1) * (x0 - x1)

print(calculate_y(x_target))

num_step = 60
x_axis = [np.min(x_list) + (np.max(x_list) - np.min(x_list)) * i / num_step for i in range(num_step+1)]
y_spline = [calculate_y(x_val) for x_val in x_axis]


plt.figure()
plt.plot(x_axis, y_spline, label="first-order splines")
plt.scatter(x_list, y_list, color="blue", label="given data")
plt.scatter(x_target, calculate_y(x_target), color="red", label="x=5")

plt.xlabel("x")
plt.ylabel("f")
plt.title("first-order splines")
plt.grid(True)
plt.legend()

plt.savefig(f"fig_15.1.png", dpi=1200)