a1 = eval(input("digite a parte real de c1\n"))
b1 = eval(input("digite a parte imaginaria de c1\n"))
a2 = eval(input("digite a parte real de c2\n"))
b2 = eval(input("digite a parte imaginaria de c2\n"))
c1 = complex(a1,b1)
c2 = complex(a2,b2)
print(f"{c1.conjugate()}+{c2.conjugate()} = {(c1+c2).conjugate()}")
print(f"{c1.conjugate()}*{c2.conjugate()} = {(c1*c2).conjugate()}")