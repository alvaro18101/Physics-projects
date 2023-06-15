import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, axes = plt.subplots()

x_datos, y_datos = [], []

graficar, = plt.plot([],[])

def lim():
    axes.set_xlim(0,2*np.pi)
    axes.set_ylim(-1,1)
    return graficar,

def funcion(x):
    x_datos.append(x)
    y_datos.append(np.cos(3*x))
    graficar.set_data(x_datos, y_datos)
    return graficar,

ani = FuncAnimation(fig, funcion,frames=np.linspace(0,5,50), init_func=lim, blit=True)

plt.show()

FuncAnimation.save(self=FuncAnimation, filename='fig.mp4')
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# fig, axes = plt.subplots()

# x_datos, y_datos = [], []

# X = [-2,-1,0,1,2,3]
# Y = [4,1,0,1,4,9]

# graficar, = plt.plot([],[])

# def lim():
#     axes.set_xlim(-2,10)
#     axes.set_ylim(0,50)
#     return graficar,

# def funcion(x):
#     x_datos.append(X[x])
#     y_datos.append(Y[x])
#     graficar.set_data(x_datos, y_datos)
#     return graficar,

# ani = FuncAnimation(fig, funcion, frames=6, init_func=lim, blit=True)

# plt.show()