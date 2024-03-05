from sympy import symbols, solve

# Definindo a variável simbólica
x = symbols('x')

# Definindo a equação
equacao = x**4 + 2*x**2 + 2

# Tentando resolver a equação
solucoes = solve(equacao, x)

# Verificando se há soluções reais
if not any(sol.is_real for sol in solucoes):
    print("A equação não possui soluções reais.")
else:
    print("A equação possui pelo menos uma solução real.")