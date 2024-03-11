import matplotlib.pyplot as plt

a1 = eval(input("digite a parte real de c1\n"))
b1 = eval(input("digite a parte imaginaria de c1\n"))
c1 = complex(a1,b1)
plt.figure()
for i in range(1,11):
    plt.quiver(0, 0, (c1+i*complex(0,1)).real, (c1+i*complex(0,1)).imag, angles='xy', scale_units='xy', scale=1, color='y')

plt.ylim((-c1-10*complex(0,1)).imag, (c1+10*complex(0,1)).imag)
plt.xlim(-c1.real, c1.real)

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True)

plt.show()