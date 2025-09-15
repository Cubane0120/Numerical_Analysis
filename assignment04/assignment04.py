import numpy as np
import matplotlib.pyplot as plt

x_0 = 0.5
gt = -0.9125
s = 4

def f(x):
    return -0.1*np.power(x,4) -0.15*np.power(x,3) -0.5*np.power(x,2) -0.25*x + 1.2

def f_derived(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

step = [_ for _ in range(0,10)]

err_abss = []
err_rels = []

for exp_h in step:
    h = 10 ** (-exp_h)
    target = f_derived(x_0, h)
    err_abs = np.abs(target - gt)
    err_rel = np.abs( (target - gt) / gt )
    print(target)
    
    err_abss.append(err_abs)
    err_rels.append(err_rel)

plt.figure()
plt.plot(step, err_abss, label='absolute error')
plt.xlabel('-exponent of h')
plt.ylabel('err')
plt.title('Absolute eror')
plt.legend()
plt.grid(True)
plt.savefig(f"err_abs.png", dpi=1200)

plt.figure()
plt.plot(step, err_rels, label='relative error')
plt.xlabel('-exponent of h')
plt.ylabel('err')
plt.title('Relative eror')
plt.legend()
plt.grid(True)
plt.savefig(f"err_rel.png", dpi=1200)

plt.figure()
plt.plot(step[s:], err_abss[s:], label=f'absolute error [{s}:]')
plt.xlabel('-exponent of h')
plt.ylabel('err')
plt.title('Absolute eror skip ')
plt.legend()
plt.grid(True)
plt.savefig(f"err_abs_skip.png", dpi=1200)

plt.figure()
plt.plot(step[s:], err_rels[s:], label=f'relative error [{s}:]')
plt.xlabel('-exponent of h')
plt.ylabel('err')
plt.title('Relative eror')
plt.legend()
plt.grid(True)
plt.savefig(f"err_rel_skip.png", dpi=1200)