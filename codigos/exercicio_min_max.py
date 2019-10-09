import numpy as np
import matplotlib.pyplot as plt

def min_func(y):
    id  = 0
    min_v = y[0]
    min_id = id
    while id + 1 < len(y):
        if y[id] < min_v:
            min_v = y[id]
            min_id = id
        id = id + 1
    return min_id, min_v

def max_func(y):
    id  = 0
    max_v = y[0]
    max_id = id
    while id + 1 < len(y):
        if y[id] > max_v:
            max_v = y[id]
            max_id = id
        id = id + 1
    return max_id, max_v

def main():
    t  = np.arange(0, 0.5, 0.01)
    y = np.sin(2*np.pi*t)
    min_id, min_v = min_func(y)
    max_id, max_v = max_func(y)

    plt.plot(t, y, 'b', label="seno")
    plt.plot(t[min_id], min_v, 'r^', label="ponto mínimo")
    plt.plot(t[max_id], max_v, 'g^', label="ponto máximo")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":  main()