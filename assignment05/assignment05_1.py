import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #kg*m/s^2
c_d = 0.25 #kg/m
gt = 36.0 #velocity, m/s

def v_at_t4(m):
    return np.sqrt(g*m/c_d) * np.tanh(np.sqrt(g*c_d/m) * 4)

m_i = 50
m_f = 250
step_size = 200
step = np.array([_ for _ in range(step_size+1)])

m = m_i + (m_f - m_i) / step_size * step
vel = v_at_t4(m)
err = vel - gt
print(m)
print(vel-gt)

plt.figure()
plt.plot(m, err, label='mass vs err')
plt.xlabel('mass [kg]')
plt.ylabel('error [m/s]')
plt.title('mass vs error graph')
plt.legend()
plt.grid(True)
plt.savefig(f"fig_5.1.png", dpi=1200)
#sol m is 143