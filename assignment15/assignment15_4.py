import numpy as np
import matplotlib.pyplot as plt


x_list = np.array([0, 2, 9])
y_list = np.array([0, 1, 6])

f_list = np.array([[0,0,0],[0, 60, 55],[0, 57.5, 70]])
xi, yi = 5.25, 4.8

f_xi_y1 = (xi-x_list[2])/(x_list[1]-x_list[2]) * f_list[1, 1] + (xi-x_list[1])/(x_list[2]-x_list[1]) * f_list[2, 1]
f_xi_y2 = (xi-x_list[2])/(x_list[1]-x_list[2]) * f_list[1, 2] + (xi-x_list[1])/(x_list[2]-x_list[1]) * f_list[2, 2]

f_xi_yi = (yi-y_list[2])/(y_list[1]-y_list[2]) * f_xi_y1 + (yi-y_list[1])/(y_list[2]-y_list[1]) * f_xi_y2


print(f_xi_yi)