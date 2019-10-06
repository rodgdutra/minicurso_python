# Codigo de exemplo da sintaxe do python para funções de decisão
# Alocando um valor boleano a x
x = True

# Utilizando o If
# Para marcar o final da declaração do if é utilizado o :
# Para demarcar o que estará dentro do if, o seu corpo, é utilizado um tab
# Nota-se que 4 espaços forma-se um tab.
if x == True:
    print("X é True")

# Utilizando if e else
# Para definir um else depois do if
if x == True:
    print("X é True")
else:
    print("X é False")

# If e Else encadeado
# Para definir operações de if e else juntas é utilizado o elif
x = 5

if x == True:
    print("X é True")
elif x == False:
    print("X é False")
else:
    print("X não é boleano")

# Utilização do If e else na declaração de variáveis
y = 5 if x==True else 6
print("y é {0}".format(y))
x = True
y = 5 if x==True else 6
print("y é {0}".format(y))
# Nota-se que nesse tipo de utilização é necessário o if e o else,
# caso somente o if irá dar erro