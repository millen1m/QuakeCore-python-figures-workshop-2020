import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap


def create():

    data = np.loadtxt(ap.MODULE_DATA_PATH + 'basic_raw_data.csv', skiprows=1, delimiter=',').T
    x = data[0]
    y = data[1]
    bf, subplot = plt.subplots()
    subplot.plot(x, y, c='b')
    plt.show()


if __name__ == '__main__':
    create()
