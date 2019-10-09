# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Definindo o eixo x ,função y e z
x = np.arange(0, 2, 0.01)
y = np.sin(2*np.pi*x)
z = np.cos(2*np.pi*x)

plt.plot(x, y, 'r', label="seno")
plt.plot(x, z, 'b', label="coseno")  # Adicionando uma segunda função
plt.legend()                         # Aplicando as legendas das funções
plt.grid('on')                       # Adicionando grid ao plot
plt.xlabel("tempo")                  # Adicionando uma legenda no eixo x
plt.ylabel("volts")                  # Adicionando uma legenda no eixo y
plt.show()                           # mostrando o plot