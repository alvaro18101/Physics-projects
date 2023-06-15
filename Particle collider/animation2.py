import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []

ln, = plt.plot([],[],'--')

def init():
    ax.set_xlim(0,6*np.pi)
    ax.set_ylim(-1, 1.5)
    return ln,

def update(frame):
    ax.set_xlim(0,6*np.pi)
    ax.set_ylim(-1, 1.5)
    xdata.append(frame)
    ydata.append(np.cos(frame))
    ln.set_data(xdata, ydata)
    plt.title(str(frame))
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0,6*np.pi,50), interval=100, init_func=init, blit=True)
ani.save('animation.mp4')
plt.show()