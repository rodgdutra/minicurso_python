# Importando o numpy
import numpy as np

# Alocando um vetor de 0 até 45 com intervalos de 5 em 5
x1 = np.arange(0,50,5)
print("x1            : {0}".format(x1))

# Criando um array com valores randomicos
x2 = np.random.rand(10)
print("x2            : {0}".format(x2))

#Criando um array só com valores 0
x0 = np.zeros(10)
print("x3            : {0}".format(x0))

# Note que o ultimo valor é o final - intervalo
# Realizando operações com o vetor
# Somando 2 a todos os campos do vetor
soma = x1 + 2
print("soma          : {0}".format(soma))

# Multiplicando cada campo por 0.5
mult = x1 * 0.5
print("multiplicação : {0}".format(mult))

# Somando um array com outro array
x2   = np.arange(0,10)
soma = x1 + x2
print("x1 + x2       : {0}".format(soma))

# Divindo um array por outro
mult = x2 * x1
print("x2 * x1       : {0}".format(mult))

# Acessando valores individuais de vetores
print("x1[0] : {0}".format(x1[0]))

# Nota-se que pode-se alocar valores para os valores acessados
x1[0] = 10
print("x1[0] : {0}".format(x1[0]))