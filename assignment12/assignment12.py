import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return 5 + np.cos(2*np.pi*12.5*t) + np.sin(2*np.pi*18.75*t)

dt = 0.02
n = 8 #num sample

x_axis = [i*dt for i in range(n)]
y_list = [f(x_val) for x_val in x_axis]

equation_str = f"y = f(t)"

plt.figure(figsize=(10, 5))
plt.plot(x_axis, y_list, color="red", label=equation_str)
plt.xlabel("t")
plt.ylabel("f(t)")
plt.title("result versus time(t)")
plt.grid(True)
plt.legend()
plt.savefig(f"fig_12.1_1.png", dpi=600)

ft_vals = np.array(y_list)
Ft = np.fft.rfft(ft_vals)[:]
freqs = np.fft.rfftfreq(n, dt)

tn = n*dt
fs = 1/dt

df = fs/n
fmax = 0.5*fs
fmin = 1/tn

freqs = [df * i for i in range(1, n//2+1)]
coeffCos = Ft.real[1:n//2+1] / n
coeffSin = Ft.imag[1:n//2+1] / n

plt.figure(figsize=(10, 5))
plt.bar(freqs, coeffCos, width=0.1, color="red")
plt.scatter(freqs, coeffCos, color="red")
plt.xlabel("frequence [Hz]")
plt.ylabel("Amptitude")
plt.title("result versus frequency(Hz) : Cos component")
plt.grid(True)
plt.axhline(y=0, color="red")
plt.legend()
plt.ylim(np.min(coeffCos)-0.1, np.max(coeffCos)+0.1)
plt.savefig(f"fig_12.1_2.png", dpi=600)

plt.figure(figsize=(10, 5))
plt.bar(freqs, coeffSin, width=0.1, color="red")
plt.scatter(freqs, coeffSin, color="red")
plt.xlabel("frequence [Hz]")
plt.ylabel("Amptitude")
plt.title("result versus frequency(Hz) : Sin component")
plt.grid(True)
plt.axhline(y=0, color="red")
plt.legend()
plt.ylim(np.min(coeffSin)-0.1, np.max(coeffSin)+0.1)
plt.savefig(f"fig_12.1_3.png", dpi=600)


Pk = coeffCos**2 + coeffSin**2


plt.figure(figsize=(10, 5))
plt.bar(freqs, Pk, width=0.1, color="red")
plt.scatter(freqs, Pk, color="red")
plt.xlabel("frequence [Hz]")
plt.ylabel("Power")
plt.title("Power spectrum versus frequency(Hz)")
plt.grid(True)
plt.axhline(y=0, color="red")
plt.legend()
plt.ylim(np.min(Pk)-0.1, np.max(Pk)+0.1)
plt.savefig(f"fig_12.2_1.png", dpi=600)