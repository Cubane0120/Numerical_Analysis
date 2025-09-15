import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #kg*m/s^2
c_d = 0.25 #kg/m
gt = 36.0 #velocity, m/s
err_thd = 0.5 #%

def v_at_t4(m):
    return np.sqrt(g*m/c_d) * np.tanh(np.sqrt(g*c_d/m) * 4)

def target(m):
    return v_at_t4(m) - gt

def error_function(x_new, x_old):
    return np.abs((x_new - x_old) / x_new) *100 #%

m_i = 50
m_f = 250

if target(m_i) * target(m_f) < 0:
    pass
else:
    raise ValueError("Inital searching region is not correct")


err_list = []
root_list = []
vel_list = []

m_middle_prev = m_i
while True:
    symbol_i = target(m_i) < 0
    symbol_f = target(m_f) < 0
    m_middle = (m_i + m_f)/2

    if symbol_i == symbol_f:
        raise Exception()
    
    symbol_m = target(m_middle) < 0
    if symbol_i == symbol_m:
        m_i = m_middle
    else:
        m_f = m_middle
    
    err = error_function(m_middle, m_middle_prev)
    
    err_list.append(err)
    root_list.append(m_middle)
    
    m_middle_prev = m_middle
    
    if err < err_thd:
        break

x_axis = [_+1 for _ in range(len(err_list))]

print(m_middle, v_at_t4(m_middle))
print("num iteration : ",len(err_list)+1)

plt.figure()
plt.plot(x_axis, err_list, label='iteration_step vs error')
plt.xlabel('step')
plt.ylabel('error [%]')
plt.title('iteration_step vs error graph')
plt.legend()
plt.grid(True)
plt.savefig(f"fig_5.3_err.png", dpi=1200)
plt.figure()


plt.figure()
plt.plot(x_axis, root_list, label='iteration_step vs pseudo root')
plt.xlabel('step')
plt.ylabel('pseudo root [kg]')
plt.title('iteration_step vs pseudo root graph')
plt.legend()
plt.grid(True)
plt.savefig(f"fig_5.3_root.png", dpi=1200)
plt.figure()