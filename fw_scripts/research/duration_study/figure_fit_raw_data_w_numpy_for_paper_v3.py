import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap
import engformat as ef


def create():

    data = np.loadtxt(ap.MODULE_DATA_PATH + 'basic_raw_data.csv', skiprows=1, delimiter=',').T
    x = data[0]
    y = data[1]
    ps = np.polyfit(x, y, deg=2)
    y_fit = ps[0] * x ** 2 + ps[1] * x + ps[2]
    bf, subplot = plt.subplots()
    for i in range(len(x)):
        subplot.plot(x[i], y[i], 'o', c='b', alpha=0.5, label='Raw data')
    subplot.plot(x, y_fit, c='r', label='Fitted')
    subplot.axvspan(0.5, 1.5, color='orange', alpha=0.3)
    cline = ef.create_custom_legend_patch('Critical zone', c='orange', alpha=0.3)
    ef.revamp_legend(subplot, loc='upper left', add_handles=[cline])
    subplot.yaxis.label.set_color((0.15, 0.15, 0.15))
    subplot.xaxis.label.set_color((0.15, 0.15, 0.15))
    subplot.tick_params(axis='x', colors=(0.05, 0.05, 0.05), width=0.5, which='major', top=True)
    subplot.tick_params(axis='y', colors=(0.05, 0.05, 0.05), width=0.5, which='major', left=True)
    ef.xy(subplot, x_origin=True, y_origin=True)
    subplot.set_xlabel('Pizza eaten [slices]')
    subplot.set_ylabel('My love for Pizza [J]')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    create()
