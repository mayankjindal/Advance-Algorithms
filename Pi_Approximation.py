# Approximating the values of Pi
# Author @Mayank_Jindal

from random import uniform
import math
import matplotlib.pyplot as plt


def generate():
    n = 0
    for i in range(0, Ntotal):
        point = [round(uniform(-1, 1), 4) for j in range(0, 2)]  # Generating random coordinates
        # point = [(-1 + 2 * p) for p in xy]  # Scaling the coordinates
        eu_dist = (point[0] ** 2 + point[1] ** 2) ** 0.5  # Euclidean Distance from the center
        if eu_dist <= 1:  # If the point lies inside the circle
            n += 1
    return n


Ninside = 0
Ntotal = 10**4
scale = 1000
x = []
y = []

for i in range(0, scale):
    temp = generate()
    Ninside += temp
    try:
        current_val = (Ninside/Ntotal)*4/i
    except:
        current_val = (Ninside/Ntotal)*4
    print(current_val)
    y.append((current_val - math.pi)*100/math.pi)
    x.append(Ntotal*i)

print(Ninside)
print(Ntotal)
print("Approximated Value of pi = ", (Ninside/Ntotal)*(4/scale))
print("Actual Value of pi = ", math.pi)
#print(x)
#print(y)

plt.scatter(x, y)
#plt.loglog(x, y, basex=10, basey=10)
plt.show()
