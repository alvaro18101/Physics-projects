# Resolviendo el problema mediante el algoritmo de Verlet
import numpy as np
import matplotlib.pyplot as plt
k = 4*np.pi**2
ax = lambda x,y: -k*x/(x**2 + y**2)**(3/2)
ay = lambda x,y: -k*y/(x**2 + y**2)**(3/2)

def verlet(t0, tf, x, y, vx, vy, h):
  T = [t0]
  X, Y = [x], [y]
  VX, VY = [vx], [vy]
  t = t0
  for i in range(int((tf-t0)/h)):
    x1 = x + h*vx + h**2*ax(x,y)/2
    y1 = y + h*vy + h**2*ay(x,y)/2
    vx = vx + h*(ax(x,y) + ax(x1,y1))/2
    vy = vy + h*(ay(x,y) + ay(x1,y1))/2

    x = x1
    y = y1

    t = t + h

    X.append(x1)
    Y.append(y1)
    VX.append(vx)
    VY.append(vy)
    T.append(t)

  return T,X,Y

T, X, Y = verlet(0,1,1,0,0,2*np.pi,0.01)
plt.figure(figsize=(5,5))
plt.plot(X,Y)
plt.plot(0,0,'oy')
plt.show()

import matplotlib.animation as animation
# Figura sobre la que se basa la animación
fig = plt.figure(figsize=(5,5))
ax=fig.gca()

def actualizar(i):
    ax.clear()
    plt.plot(0,0,'oy')
    plt.plot(X,Y,'--')
    plt.plot(X[i],Y[i],'o')
    # plt.plot(l1*np.sin(Y1[i])+l2*np.sin(Y2[i]),-l1*np.cos(Y1[i])-l2*np.cos(Y2[i]),'bo')
    plt.title(str(round(T[i],3)))
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
ani=animation.FuncAnimation(fig,actualizar,range(len(T)),interval=100)
ani.save('animacion.mp4')
plt.show()