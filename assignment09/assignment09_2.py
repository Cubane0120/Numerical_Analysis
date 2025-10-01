import numpy as np
import matplotlib.pyplot as plt

num_step = 50
v = np.array([10, 20, 30, 40, 50, 60, 70, 80])
F = np.array([25, 75, 380, 550, 610, 1220, 830, 1450])

x = v
y = F
log_x=np.log10(v)
log_y=np.log10(F)

n = len(log_x)
x_m = np.mean(log_x)
y_m = np.mean(log_y)

beta2 = (n * np.sum(log_x*log_y) - np.sum(log_x)*np.sum(log_y)) / (n * np.sum(log_x**2) - np.sum(log_x)**2 )
log_alpha2 = np.mean(log_y) - beta2 * np.mean(log_x)
alpha2 = np.power(10, log_alpha2)

def y_reg(x):
    return alpha2*(x ** beta2)    
def y_reg_log(logx):
    return log_alpha2 + beta2 * logx  

x_axis = [np.min(x) + (np.max(x) - np.min(x)) * i / num_step for i in range(num_step)]
y_approx = [y_reg(x_) for x_ in x_axis]

equation_str = f"y = {alpha2:.3f} x^{beta2:.3f}"

plt.figure()
plt.scatter(x, y)
plt.plot(x_axis, y_approx, color="red", label=equation_str)

plt.xlabel("v (m/s)")
plt.ylabel("F (N)")
plt.title("Curve Fitting (power equation)")
plt.grid(True)
plt.legend()

plt.savefig(f"fig_09.2_1.png", dpi=1200)

x_axis_log = [np.min(log_x) + (np.max(log_x) - np.min(log_x)) * i / num_step for i in range(num_step)]
y_approx_log = [y_reg_log(x_) for x_ in x_axis_log]

equation_str_log = f"log(y) = {log_alpha2:.3f} + {beta2:.3f}log(x)"

plt.figure()
plt.scatter(log_x, log_y)
plt.plot(x_axis_log, y_approx_log, color="red", label=equation_str_log)

plt.xlabel("log(v)")
plt.ylabel("log(F)")
plt.title("Curve Fitting (logx vs logy of power equation)")
plt.grid(True)
plt.legend()

plt.savefig(f"fig_09.2_2.png", dpi=1200)