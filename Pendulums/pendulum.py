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
y, z, h, t, tf = 0.1, 0, 0.1, 0, 6
m = 1

# Energies
kinetic_energy = lambda m, z: 1/2*m*l**2*z**2
potential_energy = lambda m, y: -m*g*l*np.cos(y)

# Solved the ODEs of the simple pendulum (aproximation and exactly)
T, Y, Z, E_k, E_p, E = met_rk4_2(y, z, h, t, tf, g1, m, kinetic_energy, potential_energy)
T1, Y1, Z1, E_k1, E_p1, E1 = met_rk4_2(y, z, h, t, tf, g2, m, kinetic_energy, potential_energy)


# Plot of trajectory
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

# Plot of phases space
plt.plot(Y, Z, label=label_1)
plt.plot(Y1, Z1, '--', label=label_2)
plt.legend(loc='lower right', fontsize='small')
plt.title(r'$\theta$ vs $\dot{\theta}$')
plt.xlabel(r'Angle ($\theta$)')
plt.ylabel(r'Velocity ($\dot{\theta}$)')
plt.grid()
plt.show()

# Plot of kinetic energy
plt.plot(T,E_k, label=label_1)
plt.plot(T1,E_k1, '--', label=label_2)
plt.legend(loc='lower right', fontsize='small')
plt.title(r'$T$ vs Kinetic energy')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Kinetic energy')
plt.grid()
plt.show()

# Plot of potential energy
plt.plot(T,E_p, label=label_1)
plt.plot(T1,E_p1, '--', label=label_2)
plt.legend(loc='lower right', fontsize='small')
plt.title(r'$T$ vs Potential energy')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Potential energy')
plt.grid()
plt.show()

# Plot of energy
plt.plot(T,E, label=label_1)
plt.plot(T1,E1, '--', label=label_2)
plt.plot(T,E_p, label='Potential energy')
plt.legend(loc='lower right', fontsize='small')
plt.title(r'$T$ vs Total energy')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Total energy')
plt.grid()
plt.show()


# Animation
# alto = a/a*6
# ancho = b/a*6
a = max(0, max(-l*np.cos(Y))) + l + 1
fig = plt.figure(figsize=((2*l+2)*6/a,6))
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
# ani.save('pendulum.gif')
plt.show()

# OPCIONAL: Ver como se dejaría de trabar la animación