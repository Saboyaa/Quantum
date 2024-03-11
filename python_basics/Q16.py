import numpy as np

# Exemplo de uso
matriz = np.array([[1+2j, 3-1j],
                            [4+5j, 6-2j]])


transposta = np.transpose(matriz)
conjugada = np.conjugate(matriz)
dagger = np.transpose(conjugada)

print("\nTransposta:\n", transposta)
print("\nConjugada:\n", conjugada)
print("\nDagger:\n", dagger)