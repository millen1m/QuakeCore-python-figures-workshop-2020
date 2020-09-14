import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap


def create():

    data = np.loadtxt(ap.MODULE_DATA_PATH + 'basic_raw_data.csv', skiprows=1, delimiter=',').T
    x = data[0]
    y = data[1]
    ps = np.polyfit(x, y, deg=2)
    y_fit = ps[0] * x ** 2 + ps[1] * x + ps[2]
    eq = f'y = {ps[0]:.2g} \cdot x ^ 2 + {ps[1]:.2g} \cdot x + {ps[0]:.2f}'
    bf, subplot = plt.subplots()
    subplot.text(0.6, 0.2, '$%s$' % eq,
                 verticalalignment='center', horizontalalignment='center',
                 transform=subplot.transAxes,
                 color='k', fontsize=9)
    subplot.plot(x, y, c='b')
    subplot.plot(x, y_fit, c='r')
    plt.show()


if __name__ == '__main__':
    create()
