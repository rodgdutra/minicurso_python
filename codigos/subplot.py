# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Definindo o eixo x ,função y e z
x = np.arange(0, 0.5, 0.01)
y = np.sin(2*np.pi*x)
z = np.cos(2*np.pi*x)

plt.subplot(211)                     # Registrando o primeiro plot como subplot
plt.plot(x, y, 'r', label="seno")
plt.legend()                         # Aplicando as legendas das funções
plt.grid('on')                       # Adicionando grid ao plot
plt.xlabel("tempo")                  # Adicionando uma legenda no eixo x
plt.ylabel("volts")                  # Adicionando uma legenda no eixo y
plt.subplot(212)                     # Registrando o segundo plot como subplot
plt.plot(x, z, 'b', label="coseno")  # Adicionando uma segunda função
plt.legend()                         # Aplicando as legendas das funções
plt.grid('on')                       # Adicionando grid ao plot
plt.xlabel("tempo")                  # Adicionando uma legenda no eixo x
plt.ylabel("volts")                  # Adicionando uma legenda no eixo y
plt.savefig('plot.png')              # Salvando a figura