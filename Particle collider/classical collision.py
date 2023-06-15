import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Particle:
    def __init__(self, r, v, a):
        self.r = r
        self.v = v
        self.a = a
        self.h = 0.1
    
    def __str__(self):
        return 'Particle: ' + str(self.r)

    def move(self):
        v0 = self.v
        self.r = v0 + (self.a*self.h**2)/2
        self.v = v0 + self.a


    def collision(self):
        return [self.r[0],self.r[1]]

r1 = np.array([1,3])
v1 = np.array([3,4])
a1 = np.array([-1,2])
particle1 = Particle(r1,v1,a1)

x, y = [], []

for i in range(20):
    x.append(particle1.r[0])
    y.append(particle1.r[1])
    particle1.move()
    # particle1.r = np.array([particle1.r[0],particle1.r[1]])

print(x)
print(y)

fig, axes = plt.subplots()
x_datos, y_datos = [], []

graficar, = plt.plot([],[],'ro')

def lim():
    axes.set_xlim(-15,3)
    axes.set_ylim(0,45)
    return graficar,

def funcion(i):
    x_datos.append(x[i])
    y_datos.append(y[i])
    graficar.set_data(x_datos, y_datos)
    return graficar,

ani = FuncAnimation(fig, funcion, frames=20, init_func=lim, blit=True)

plt.show()


