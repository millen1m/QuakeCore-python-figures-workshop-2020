import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap


def create():
    x = np.linspace(0, 5, 100)
    np.random.seed(0)
    y = 0.4 * x ** 2 + x + 0.3 + np.random.random(len(x))
    name = __file__.replace('.py', '')
    name = name.split("generate_")[-1]
    data = np.array([x, y]).T
    np.savetxt(ap.MODULE_DATA_PATH + name + '.csv', data, delimiter=',', header='x,y', comments='', fmt='%.6g')

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    create()
