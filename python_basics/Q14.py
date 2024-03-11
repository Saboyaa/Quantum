def mobius_transform(z, a, b, c, d):
    numerator = a * z + b
    denominator = c * z + d
    result = numerator / denominator
    return result

# Exemplo de uso
a = 0
b = 1
c = 0
d = 1
a1 = eval(input("digite a parte real de c1\n"))
b1 = eval(input("digite a parte imaginaria de c1\n"))
z = complex(a1,b1)

result = mobius_transform(z, a, b, c, d)
print("Resultado da Transformação de Möbius:", result)