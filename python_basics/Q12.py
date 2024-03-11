import matplotlib.pyplot as plt

a1 = eval(input("digite a parte real de c1\n"))
b1 = eval(input("digite a parte imaginaria de c1\n"))
c1 = complex(a1,b1)
plt.figure()
for i in range(1,11):
    plt.quiver(0, 0, (c1**i).real, (c1**i).imag, angles='xy', scale_units='xy', scale=1, color='y')

plt.xlim(-abs(c1)**10, abs(c1)**10)
plt.ylim(-abs(c1)**10, abs(c1)**10)

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()