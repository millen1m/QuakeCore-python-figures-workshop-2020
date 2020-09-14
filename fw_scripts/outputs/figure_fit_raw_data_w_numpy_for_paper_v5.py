import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap
import engformat as ef
import settings as ops
from bwplot import cbox

def create(show=0, save=0):

    data = np.loadtxt(ap.MODULE_DATA_PATH + 'basic_raw_data.csv', skiprows=1, delimiter=',').T
    x = data[0]
    y = data[1]
    ps = np.polyfit(x, y, deg=2)
    y_fit = ps[0] * x ** 2 + ps[1] * x + ps[2]
    bf, subplots = plt.subplots(nrows=2, sharex='col', figsize=(ops.ONE_COL, 5))
    for i in range(len(x)):
        subplots[0].plot(x[i], y[i], 'o', c='b', alpha=0.5, label='Raw data')
    subplots[0].plot(x, y_fit, c='r', label='Fitted')
    subplots[0].axvspan(0.5, 1.5, color='orange', alpha=0.3)

    dd = {'Monday': 3,
          'Tuesday': 4,
          'Wednesday': 6
          }
    counter = 0
    for day in dd:
        subplots[1].plot(x, y + dd[day], c=cbox(counter), label=day)
        counter += 1

    cline = ef.create_custom_legend_patch('Critical zone', c='orange', alpha=0.3)
    ef.revamp_legend(subplots[0], loc='upper left', add_handles=[cline])
    ef.xy(subplots[0], x_origin=True, y_origin=True)
    ef.revamp_legend(subplots[1], loc='upper left')
    ef.xy(subplots[1], x_origin=True, y_origin=True)
    subplots[1].set_xlabel('Pizza eaten [slices]')
    subplots[0].set_ylabel('My love for Pizza [J]')
    subplots[1].set_ylabel('My love for Pizza [J]')
    name = __file__.replace('.py', '')
    name = name.split("figure_")[-1]
    if save:
        bf.savefig(ap.PUB_FIG_PATH + 'name' + ops.PUB_FIG_FILE_TYPE, dpi=ops.PUB_FIG_DPI)
        print(ef.latex_for_figure(ap.FIG_FOLDER, name, ops.PUB_FIG_FILE_TYPE))
    if show:
        plt.show()


if __name__ == '__main__':
    create(save=1, show=1)
