import numpy as np
from pprint import pprint
# Nota :  a biblioteca pprint serve para mostrar na tela de
# forma mais agradável matrizes e outras estruturas

# Declarando uma matriz e visualizando-a
A = np.array([[2, 4], [5, -6]])
print("A:")
pprint(A)

# Visualizando somente a primeira linha
print("A[0]:")
pprint(A[0])

# Visualizando somente a primeira coluna
print("A j1:")
pprint(A[:,0])

# Operações basicas com matrizes
B = np.array([[3,4],[6,9]])
print("B :")
pprint(B)

# Soma
print("A + B :")
pprint(A + B)

# Multiplicação
print("A * B :")
pprint( A * B)

# Transposição
print("A_t:")
pprint(np.transpose(A))

# Transformando matriz em vetor unidimensional
tran_a = A.flatten()
print("A unidimensional :")
pprint(tran_a)

# Manipulando as dimensões de um array
C = np.arange(0,4)
C = C.reshape(2,2)
print("C :")
pprint(C)