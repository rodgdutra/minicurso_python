import numpy as np
import matplotlib.pyplot as plt

def Vc_RC(t, r=5, c=0.1, vin=1):
    """
    Tensão de um capacitor em um circuito RC
    """
    tau = -t/(r*c)
    vc  = vin*(1 - np.exp(tau))

    return vc


def main():
    t  = np.arange(0, 3, 0.1)
    vc = Vc_RC(t)

    plt.plot(t, vc, 'b', label="tensão VC calculada")
    plt.legend()
    plt.grid()
    plt.xlabel("tempo")
    plt.ylabel("tensão")
    plt.show()


if __name__ == "__main__":
    main()