import matplotlib.pyplot as plt
import cmath

z1 = 2 - 1j
z2 = 1 + 1j

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6, 6))

ax.plot(cmath.phase(z1+z2), abs(z1+z2), marker='o', markersize=15, color='red')
ax.plot(cmath.phase(z1-z2), abs(z1-z2), marker='o', markersize=15, color='red')
plt.show()