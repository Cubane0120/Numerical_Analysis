import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #kg*m/s^2
m = 68.1 #kg
c_d = 0.25 #kg/m
t_total = 12

def v_gt(t):
    return np.sqrt(g*m/c_d) * np.tanh(np.sqrt(g*c_d/m) * t)

dt = 4
print(f"dt : {dt}")
t = np.arange(0, t_total + dt, dt)

v_numerical = [0]
for _ in t[1:]: #without t=0, v(0) = 0
    delta_v = (g - c_d/m * np.power(v_numerical[-1],2))*dt
    v_numerical.append(v_numerical[-1] + delta_v)


v_analytic = v_gt(t)
v_terminal = np.sqrt(g * m / c_d)

v_analytic_ = v_gt(t_total)
v_numerical_ = v_numerical[-1]

plt.figure()
plt.plot(t, v_numerical, label='Numerical')
plt.plot(t, v_analytic, label='Analytic')
plt.axhline(v_terminal, linestyle='--')
plt.xlabel('Time t (s)')
plt.ylabel('Velocity v (m/s)')
plt.title('Free fall with quadratic drag: Analytic vs Euler')
plt.legend()
plt.grid(True)
plt.savefig(f"result_{dt:.2f}.png", dpi=1200)

print(f'Terminal velocity: {v_terminal:.6f} m/s')
print(f'Analytic v({t_total}s): {v_analytic_:.6f} m/s')
print(f'Numerical v({t_total}s): {v_numerical_:.6f} m/s')

print(f'absolute err : {abs(v_analytic_-v_numerical_)}')
print(f'relative err : {abs(v_analytic_-v_numerical_)/v_analytic_}')