import numpy as np
import matplotlib.pyplot as plt


def create():
    x = np.linspace(0, 5, 100)
    y = np.sin(x) + x

    bf, subplot = plt.subplots()
    subplot.plot(x, y)
    plt.show()


if __name__ == '__main__':
    create()
