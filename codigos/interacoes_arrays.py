import numpy as np
# Alocando um vetor de 0 até 50 com passo de 1 em 1
x = np.arange(0,50)
print("x  : {0}".format(x))

# Partindo o Array
# A notação do python para o particionamento de arrays é [inicio:final:passo]
# Nota-se que não necessáriamente é necessário utilizar todos os ':'

# partindo o array em 2 metades
x1 = x[:25]
x2 = x[25:50]
print("x1  : {0}".format(x1))
print("x2  : {0}".format(x2))

# Realizando o 'Downsampling' do array
x3 = x[::2]
print("x3  : {0}".format(x3))

# Juntando 2 arrays
x4 = np.concatenate((x1,x2))
print("x4  : {0}".format(x4))

# Comparando 2 arrays
comp = (x4 == x)
print("comp: {0}".format(comp))

# Transformando um array do tipo numpy para lista do python
x1_list = x1.tolist()
print("classe antes: ",type(x1))
print("classe depois: ",type(x1_list))

# Adicionando termos em uma lista python
x1_list.append(255)
print("x1_list: {0}".format(x1_list))

# Acessando informações do array
len_x1 = len(x1)
dim_x1 = x1.shape
print("tamanho x1: {0}, dimensões x1: {1}".format(len_x1,dim_x1))