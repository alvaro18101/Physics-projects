import numpy as np
points, A = 10000, 0
for i in range(points):
    if np.sqrt((0.01*np.random.rand()-0.005)**2 + (0.01*np.random.rand()-0.005)**2)<=0.005:
        A += 1
    pi = 4*A/points
print(pi)