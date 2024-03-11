import matplotlib.pyplot as plt

a1 = eval(input("digite a parte real de c1\n"))
b1 = eval(input("digite a parte imaginaria de c1\n"))
a2 = eval(input("digite a parte real de c2\n"))
b2 = eval(input("digite a parte imaginaria de c2\n"))
c1 = complex(a1,b1)
c2 = complex(a2,b2) #fazer logo mutiplicacao de numero qualquer dae A e B ficam como casos particulares
plt.figure()
plt.quiver(0, 0, (c1*c2).real, (c1*c2).imag, angles='xy', scale_units='xy', scale=1, color='y')
plt.text((c1*c2).real, (c1*c2).imag, ' Vetor soma', fontsize=12, color='y', verticalalignment='bottom', horizontalalignment='right')

plt.xlim(0, 4)
plt.ylim(-2, 2)

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()