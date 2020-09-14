import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap


def my_formatter(subplot, x_origin=True, y_origin=True):
    if x_origin:
        x_lims = subplot.get_xlim()
        subplot.set_xlim([0, x_lims[1]])
    if y_origin:
        y_lims = subplot.get_ylim()
        subplot.set_ylim([0, y_lims[1]])


def create():

    data = np.loadtxt(ap.MODULE_DATA_PATH + 'basic_raw_data.csv', skiprows=1, delimiter=',').T
    x = data[0]
    y = data[1]
    ps = np.polyfit(x, y, deg=2)
    y_fit = ps[0] * x ** 2 + ps[1] * x + ps[2]
    bf, subplot = plt.subplots()

    subplot.plot(x, y, c='b')
    subplot.plot(x, y_fit, c='r')
    subplot.set_xlim([0, 5])  # TODO: comment this out
    subplot.set_ylim([0, 16])  # TODO: comment this out
    # my_formatter(subplot)  # TODO: uncomment this
    plt.show()


if __name__ == '__main__':
    create()
