f = lambda x: 4/(1+x**2)
a,b, N = 0, 1, 1000000
h = (b-a)/N
sumatoria = 0
for i in range(1,N):
    sumatoria += f(a+i*h)
pi = h*(f(a) + 2*sumatoria + f(b))/2
print(pi)