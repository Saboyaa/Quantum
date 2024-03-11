import cmath

a1 = eval(input("digite a parte real de c1\n"))
b1 = eval(input("digite a parte imaginaria de c1\n"))
c1 = complex(a1,b1)

print(cmath.polar(c1))