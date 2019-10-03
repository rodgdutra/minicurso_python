# Primeiro exercicio resolução
import numpy as np
from pprint import pprint

# declarando um vetor de x
x = np.arange(0,10)

# declarando um vetor y de valores randomicos
y = np.random.rand(10)

# Alocando um array de 0
z = np.zeros(20)
z = z.reshape(10,2)

# Colocar a primeira coluna como x
z[:,0] = x

# Colocar a segunda coluna como y
z[:,1] = y

# Mostrando na tela a matriz
print("Matrix xy : ")
pprint(z)

# Adicionando valores para a coluna y
z[:,1] = z[:,1] + 4

# Mostrando na tela a matriz
print("Matrix xy : ")
pprint(z)