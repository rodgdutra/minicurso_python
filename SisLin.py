import numpy as np

V = np.array([[5],[3]]) # vetor de tensões
R = np.array([[3,-2],[-2,5]]) # matris de resistencias 

I = np.dot(np.linalg.inv(R),  V)
print(V)
print(R)
print(I)