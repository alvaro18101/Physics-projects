import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# CI
y1, z1, y2, z2 = np.pi/3, 0, -np.pi/6, 0

# Parameters
g = 9.81
m1, m2, l1, l2 = 1.0, 1.0, 1.0, 2.0
h = 0.01
t, tf = 0, 5
N = int((tf-t)/h)

Y1, Z1, Y2, Z2, T = [y1], [z1], [y2], [z2], [t]

# Functions
def g1(y1,z1,y2,z2):
    return (-g*(2*m1+m2)*np.sin(y1)-m2*g*np.sin(y1-2*y2)-2*np.sin(y1-y2)*m2*((z2**2)*l2+(z1**2)*l1*np.cos(y1-y2)))/(l1*(2*m1+m2-m2*np.cos(2*y1-2*y2)))
def g2(y1,z1,y2,z2):
    return (2*np.sin(y1-y2)*(z1**2*l1*(m1+m2)+g*(m1+m2)*np.cos(y1)+z2**2*l2*m2*np.cos(y1-y2)))/(l2*(2*m1+m2-m2*np.cos(2*y1-2*y2)))

def energy_0(y1, z1, y2, z2):
    return -(m1+m2)*g*l1*np.cos(y1) - m2*g*l2*np.cos(y2)

def kinetic_energy(y1, z1, y2, z2):
    return 1/2*m1*l1**2*z1**2 + 1/2*m2*( l1**2*z1**2 + l2**2*z2**2 + 2*l1*l2*z1*z2*np.cos(y1-y2) )

def potential_energy(y1, z1, y2, z2):
    return -(m1 + m2)*g*l1*np.cos(y1) - m2*g*l2*np.cos(y2)

K = [kinetic_energy(y1, z1, y2, z2)]
V = [potential_energy(y1, z1, y2, z2)]
Energy = [kinetic_energy(y1, z1, y2, z2) + potential_energy(y1, z1, y2, z2)]

# RK4
for i in range(N):
    k1_1 = h*z1
    p1_1 = h*g1(y1,z1,y2,z2)
    k1_2 = h*z2
    p1_2 = h*g2(y1,z1,y2,z2)

    k2_1 = h*(z1 + p1_1/2)
    p2_1 = h*g1(y1 + k1_1/2, z1 + p1_1/2, y2 + k1_2/2, z2 + p1_2/2)
    k2_2 = h*(z2 + p1_2/2)
    p2_2 = h*g2(y1 + k1_1/2, z1 + p1_1/2, y2 + k1_2/2, z2 + p1_2/2)

    k3_1 = h*(z1 + p2_1/2)
    p3_1 = h*g1(y1 + k2_1/2, z1 + p2_1/2, y2 + k2_2/2, z2 + p2_1/2)
    k3_2 = h*(z2 + p2_2/2)
    p3_2 = h*g2(y1 + k2_1/2, z1 + p2_1/2, y2 + k2_2/2, z2 + p2_2/2)

    k4_1 = h*(z1 + p3_1)
    p4_1 = h*g1(y1 + k3_1, z1 + p3_1, y2 + k3_2, z2 + p3_2)
    k4_2 = h*(z2 + p3_2)
    p4_2 = h*g2(y1 + k3_1, z1 + p3_1, y2 + k3_2, z2 + p3_2)

    y1 = y1 + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6
    y2 = y2 + (k1_2 + 2*k2_2 + 2*k3_2 + k4_2)/6
    z1 = z1 + (p1_1 + 2*p2_1 + 2*p3_1 + p4_1)/6    
    z2 = z2 + (p1_2 + 2*p2_2 + 2*p3_2 + p4_2)/6
    t = t + h

    Y1.append(y1)
    Z1.append(z1)
    Y2.append(y2)
    Z2.append(z2)
    T.append(t)
    K.append(kinetic_energy(y1, z1, y2, z2))
    V.append(potential_energy(y1, z1, y2, z2))
    Energy.append(kinetic_energy(y1, z1, y2, z2) + potential_energy(y1, z1, y2, z2))


# PLOTS
label_1 = r"$m_1$"
label_2 = r"$m_2$"
# Plot of trajectory
plt.plot(T,Y1, label=label_1)
plt.plot(T,Y2, label=label_2)
plt.legend(loc='upper right', fontsize='small')
plt.title(r'$\theta$ vs $t$')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Angle ($\theta$)')
plt.grid()
plt.show()

# Plot of phases space
plt.plot(Y1, Z1, label=label_1)
plt.plot(Y2, Z2, label=label_2)
plt.legend(loc='lower right', fontsize='small')
plt.title(r'$\theta$ vs $\dot{\theta}$')
plt.xlabel(r'Angle ($\theta$)')
plt.ylabel(r'Velocity ($\dot{\theta}$)')
plt.grid()
plt.show()

# Plot of energies
plt.plot(T,K, label='Kinetic energy')
plt.plot(T,V, label='Potential energy')
plt.plot(T, Energy, label='Total energy')
plt.legend(loc='lower right', fontsize='small')
plt.title(r'$T$ vs Mechanical energy')
plt.xlabel(r'Time ($t$)')
plt.ylabel(r'Energy')
plt.grid()
plt.show()

# Animación
fig = plt.figure()
ax=fig.gca()
ax.set_facecolor('#131310')
fig.set_facecolor('#131310')
ax.spines[['top', 'bottom', 'right', 'left']].set_color('#e8e6df')
ax.tick_params(axis='both', colors='#e8e6df')


def actualizar(i):
    ax.clear()
    plt.grid(color='#e8e6df')
    plt.plot([0,l1*np.sin(Y1[i])],[0,-l1*np.cos(Y1[i])], ls='--', lw=3, color='#FA2807')
    plt.plot([l1*np.sin(Y1[i]),l1*np.sin(Y1[i])+l2*np.sin(Y2[i])],[-l1*np.cos(Y1[i]),-l1*np.cos(Y1[i])-l2*np.cos(Y2[i])], ls='--', lw=3, color='#FA2807')
    plt.plot(l1*np.sin(Y1[i]),-l1*np.cos(Y1[i]), marker='o', markersize=8, color='#FA2807')
    plt.plot(l1*np.sin(Y1[i])+l2*np.sin(Y2[i]),-l1*np.cos(Y1[i])-l2*np.cos(Y2[i]), marker='o', markersize=8, color='#FA2807')
    plt.title('t = '+str(round(T[i],3))+'s', color='#e8e6df')
    plt.xlim(-l1-l2,l1+l2)
    plt.ylim(-l1-l2,0)
ani=animation.FuncAnimation(fig,actualizar,range(len(T)),interval=100)
# ani.save('double_pendulum.gif')
# plt.show()