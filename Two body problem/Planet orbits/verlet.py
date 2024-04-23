# import numpy as np
# import matplotlib.pyplot as plt

G = 1
gravitational_force = lambda m1, m2, r: G*m1*m2/r**2



def verlet(dt, t, tf, r1, r2, v1, v2, f(r1, r2, v1, v2)):
    N = int(tf - t)/h
    X1 = [r1[0]]
    Y1 = [r1[1]]
    X2 = [r2[0]]
    Y2 = [r2[1]]
    for i in range(N):
        r1[0] = r[0] + dt*v(t + dt/2)
        r1[i+1] = r1[i] +v1[i]*dt + f()*dt**2/2
        v1[i+1] = v[i] + dt*(f() + f())/2
        r2[i+1] = r2[i] + v2[i]*dt + f()*dt**2/2
        
        t = t + dt
        X1.append(r1[0])
        Y1.append(r1[1])
        X21.append(r2[0])
        Y2.append(r2[1])
    return X1, Y1, X2, Y2

x = [[1,2], [3,1], [4, 8]]
# print(x[:,0])   esto necesita numpy