import numpy as np
import matplotlib.pyplot as plt
from rk4_2 import met_rk4_2
import matplotlib.animation as animation

# Parameters
l, g = 10, 9.91
w2 = g/l

# ODEs
g1 = lambda y, z, t: -w2*y
g2 = lambda y, z, t: -w2*np.sin(y)

# CI
y, z, h, t, tf = 0.5, 0, 0.1, 0, 6

# Solved the ODEs of the simple pendulum (aproximation and exactly)
T, Y, Z = met_rk4_2(y, z, h, t, tf, g1)
T1, Y1, Z1 = met_rk4_2(y, z, h, t, tf, g2)

# Plots
label_1 = r"$\ddot{\theta}=-\omega^2 \theta$"
label_2 = r"$\ddot{\theta}=-\omega^2 \sin{\theta}$"
plt.plot(T, Y, label=label_1)
plt.plot(T1, Y1, '--', label=label_2)
plt.legend(loc='lower right', fontsize='small')
plt.title(r'$\theta$ vs $t$')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Angle ($\theta$)')
plt.grid()
plt.show()

# Animation
fig = plt.figure(figsize=(12,6))
ax=fig.gca()
ax.set_facecolor('#131310')
fig.set_facecolor('#131310')
ax.spines[['top', 'bottom', 'right', 'left']].set_color('#e8e6df')
ax.tick_params(axis='both', colors='#e8e6df')

def actualizar(i):
    ax.clear()
    plt.grid(color='#e8e6df')
    plt.plot([0,l*np.sin(Y[i])],[0,-l*np.cos(Y[i])], ls='--', lw=3, color='#FA2807')
    plt.plot(l*np.sin(Y[i]),-l*np.cos(Y[i]), marker='o', markersize=8, color='#FA2807')
    plt.title('t = '+str(round(T[i],3))+'s', color='#e8e6df')
    plt.xlim(-l-1,l+1)
    plt.ylim(-l-1,max(0, max(-l*np.cos(Y))))
ani=animation.FuncAnimation(fig,actualizar,range(len(T)),repeat=True, interval=100)
ani.save('pendulum.gif')
plt.show()

# OPCIONAL: Ver como se dejaría de trabar la animación