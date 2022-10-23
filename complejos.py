import math
import matplotlib.pyplot as plt
import numpy as np


z = complex(2, 3)
z2 = complex(2, -3)
z3 = (z + z2) / 2
z4 = (z - z2) / 2

print(z, '\n', z2, '\n', z3, '\n', z4)

fig, ax = plt.subplots()

theta = np.linspace(0, 2*np.pi, 130)

radius = 1

a = radius*np.cos(theta)
b = radius*np.sin(theta)
x = [.9, 0, 0]
y = [.7, 1, 0]

ax.plot(a, b, x, y, 'ro', linewidth=1.5, color='red')
ax.set_aspect(1)

plt.show()