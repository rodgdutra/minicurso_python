import numpy as np
# Declarando uma lista vazia
x = list() # também poderia ser x = []

# Utilizando o for para adicionar valores em x
for i in range(0,10):
    x.append(i)

print("x : ",x)

# Nota-se que o for é utilizado para iterar em objetos iteraveis
# o objeto iterável nesse caso é o range que cria uma serie
# iteravel do tipo range.

# Utilizando o for em uma lista de strings
animais = ["macaco","cachorro","gato"]

for i in animais:
    print("animal da vez : ", i)

# O for no python pode ser utilizado também na declaração de variáveis
y = np.arange(0,10)

x = [i*(i-1) for i in y]
print("x : ",x)
# dessa forma o for pode ser utilizado para declarar uma lista, realizando
# operações para cada iteração e salvando o resultado na lista em 1 linha só

# Utilizando o while
i = 0
while(i < 10):
    print("valor do i: ",i)
    i = i + 1

# Utilizando o break para parar loops
# Criando um loop intermitente por natureza e parando-o com o break
i = 0
while True:
    print("valor do i: ",i)
    i = i + 1
    if i == 10:
        break