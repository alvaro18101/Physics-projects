# Code that uses the parabolic motion formulas
import numpy as np
g = 9.81
# Parameters to change
v0 = 20
angle = np.pi/4
n = 200
# Computing
v0x = v0*np.cos(angle)
v0y = v0*np.sin(angle)
t = 2*v0y/g
h_max = v0y**2/(2*g)
d = v0x*t

T = np.linspace(0,t,n)
X = np.linspace(0,t,n)
Y = np.linspace(0,t,n)

X = v0x*T
Y = v0y*T - g*T**2/2

print('---MRU formulas---')
print(f'Time of the motion: {round(t,3)} s')
print(f'Maximum height: {round(h_max,3)} m')
print(f'Distance traveled: {round(d,3)} m')
print()


# Code solving EDO
from rk4_2 import met_rk4_2
t0 = 0
h = 0.01
ax = lambda y,z,t: 0
ay = lambda y,z,t: -g

T2, Y2, ZY2 = met_rk4_2(0, v0y, h, 0, ay, True)
T2, X2, ZX2 = met_rk4_2(0, v0x, h, 0, ax, False, len_Y=len(Y2))

print('---Computational data---')
print(f'Maximum height: {round(max(Y2),3)} m')
print(f'Distance traveled: {round(max(X2),3)} m')
print()


# Code solving EDO with air resistance
k = 0.1
ax = lambda y,z,t: 0-k*z
ay = lambda y,z,t: -g - k*z

T3, Y3, ZY3 = met_rk4_2(0, v0y, h, 0, ay, True)
T3, X3, ZX3 = met_rk4_2(0, v0x, h, 0, ax, False, len_Y=len(Y3))

print('---Computational data: Air resistance---')
print(f'Maximum height: {round(max(Y3),3)} m')
print(f'Distance traveled: {round(max(X3),3)} m')
print()



# Ploting
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# ax.plot(X,Y)
ax.plot(X2,Y2)
ax.plot(X3,Y3)
ax.plot([-1,max(X)+1],[0,0], color='k', linewidth=0.7)
ax.set_title('Parabolic motion')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend(['No air resistance', f'Air resistance k={k}'])
plt.show()