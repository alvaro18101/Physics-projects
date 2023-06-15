n, pi = 10000000, 0
for i in range(n):
    pi += ((-1)**(i))/(2*i+1)
print(4*pi)