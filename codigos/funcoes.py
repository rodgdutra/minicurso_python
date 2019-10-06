
# Definindo funções e organizando o cogido no python

import numpy as np
# para definir uma função utiliza-se o def
# Os argumentos da função devem estar entre ()
# O corpo deve estar em um bloco de codigo identado por tab

# definindo uma função para retornar a soma dos elementos de um array
def somatorio(a):
    soma = 0
    for i in a:
        soma = soma + i

    return soma
    # O return é necessário para retornar o dado

# Definindo uma função principal
# Nota-se que esse passo não é realmente necessário, porém organizar um
# codigo com uma função principal e outras secundárias é o ideal para
# a organização do codigo
def main():
    x = np.arange(10)
    soma = somatorio(x)
    print("soma :", soma)

# Esse bloco do if __name__ == é necessário para chamar a função main
if __name__ == "__main__":
    main()