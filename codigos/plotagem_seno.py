# Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

# Definindo o eixo x e a função y
x = np.arange(0,2,0.01)
y = np.sin(2*np.pi*x)

plt.plot(x,y)
plt.show()