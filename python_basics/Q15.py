import numpy as np

def obter_matriz_complexa():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    matriz_complexa = np.zeros((linhas, colunas), dtype=complex)
    for i in range(linhas):
        for j in range(colunas):
            parte_real = float(input(f"Digite a parte real do elemento ({i+1},{j+1}): "))
            parte_imaginaria = float(input(f"Digite a parte imaginária do elemento ({i+1},{j+1}): "))
            matriz_complexa[i, j] = parte_real + parte_imaginaria * 1j
    return matriz_complexa
def add(matriz1, matriz2):
    resultado = matriz1 + matriz2
    return resultado
def inversa(matriz1, matriz2):
    resultado = np.linalg.inv(matriz1)
    return resultado
print("Digite a primeira matriz complexa:")
matriz_complexa1 = obter_matriz_complexa()
print("\nDigite a segunda matriz complexa (com as mesmas dimensões da primeira):")
matriz_complexa2 = obter_matriz_complexa()
print(add(matriz_complexa1,matriz_complexa2))
print(inversa(matriz_complexa1,matriz_complexa2))