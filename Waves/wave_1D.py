import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

f = lambda x: 0.05*x if 0<=x<=1 else -0.1*x + 0.15 # u(x,0)
g = lambda x: 0 # du/dt(x,0)

# f: CI t=0
# g: CI derivada
# t: tiempo final

def edp(dt, dx, v, x0, xl, t0, f, g, t):
    while (v*dt/dx)**2 > 1:
        print('Solución inestable c =',(v*dt/dx)**2)
        print('Digite valores para una solución estable')
        dt = float(input('dt = '))
        dx = float(input('dx = '))
    c = (v*dt/dx)**2
    nx = int((xl-x0)/dx + 1)
    nt = int((t-t0)/dt + 1)
    u = np.zeros((nt,nx))
    
    T, X = [], []
    for i in range(nx):
        X.append(i*dx)
    for i in range(nt):
        T.append(i*dt)
    
    # i: iteración en el tiempo
    # j: iteración en el espacio
    # Asignando las condiciones iniciales
    for j in range(nx):
        u[0][j] = f(j*dx)

    # Asignando las condiciones de frontera
    for i in range(nt):
        u[i][0] = u[i][-1] = 0
    # Se coloca las CF después porque tienen prioridad

    # Calculando el instante t1
    for j in range(1,nx-1):
        # u[1][j] = u[0][j] + c/2*(u[0][j+1] - 2*u[0][j] + u[0][j-1])
        u[1][j] = u[0][j] + dt*g(j*dx) + c/2*(u[0][j+1] - 2*u[0][j] + u[0][j-1])

    # Llenando la matriz
    for i in range(1,nt-1):
        for j in range(1,nx-1):
            u[i+1][j] = 2*u[i][j] - u[i-1][j] + c*(u[i][j-1] - 2*u[i][j] + u[i][j+1])
    return T, X, u

x0, xl, t0, t = 0, 1.5, 0, 0.1
# onda = edp(0.0005, 0.05, np.sqrt(9651), x0, xl, t0, f, g, t)
onda = edp(0.001, 0.1, np.sqrt(9651), x0, xl, t0, f, g, t)
T = onda[0]
X = onda[1]
Y = onda[2]

print('Solución de una onda 1D')
maximo = []
minimo = []
for i in range(len(Y)):
    maximo.append(max(Y[i]))
    minimo.append(min(Y[i]))

# Animación
fig = plt.figure()
ax = fig.gca()

def actualizar(i):
    ax.clear()
    plt.plot(X,Y[i],'-')
    plt.xlim(x0, xl)
    plt.ylim(min(minimo),max(maximo))
    plt.title('t=' + str(round(T[i],3)))
ani = animation.FuncAnimation(fig,actualizar,range(len(T)),interval=200)
ani.save('animation2.mp4')
plt.show()