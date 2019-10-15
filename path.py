import os

def path(pas):
    listaArquivos =  os.listdir(pas)
    print(pas)
    for x in listaArquivos:
        if os.path.isdir(pas+ '/' + x):
            path(pas + '/'+ x)
        else:
            print(pas + x) 

        

pasta = input("digite o caminho da pasta: ")

print(path(pasta))
