import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #kg*m/s^2
c_d = 0.25 #kg/m
gt = 36.0 #velocity, m/s

def v_at_t4(m):
    return np.sqrt(g*m/c_d) * np.tanh(np.sqrt(g*c_d/m) * 4)

def target(m):
    return v_at_t4(m) - gt

m_i = 50
m_f = 250

if target(m_i) * target(m_f) < 0:
    pass
else:
    raise ValueError("Inital searching region is not correct")

for _ in range(5):
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
    
    print(target(m_middle), m_i, m_f)

print(v_at_t4(m_middle), m_middle)