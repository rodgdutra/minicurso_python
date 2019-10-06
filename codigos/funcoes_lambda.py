# Utilizando lambda

# Primeiramente, definindo uma função da forma tradicional
# Função para calcular o quadrado de um número:

def quadrado(x):
    return x*x

# Função main
def main():
    x = 2
    x_2 = quadrado(x)

    # Utilizando o lambda
    # Uma função lambda é declarada da seguinte forma
    # o argumento vem aṕos do lambda
    # a expressão para ser retornada fica após o :
    quadrado_lambda = lambda x: x*x

    x_2_lambda = quadrado_lambda(x)
    print("x_2 : {0}, x_2_lambda {1}".format(x_2,x_2_lambda))

if __name__ == "__main__":
    main()
