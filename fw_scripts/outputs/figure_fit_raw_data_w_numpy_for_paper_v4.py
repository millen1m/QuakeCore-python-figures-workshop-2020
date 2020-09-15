import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap
import engformat as ef
import settings as ops

from matplotlib import rc
rc('font', family='Helvetica', size=9, weight='light')
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42  # To avoid type 3 fonts


def create(show=0, save=0):

    data = np.loadtxt(ap.MODULE_DATA_PATH + 'basic_raw_data.csv', skiprows=1, delimiter=',').T
    x = data[0]
    y = data[1]
    ps = np.polyfit(x, y, deg=2)
    y_fit = ps[0] * x ** 2 + ps[1] * x + ps[2]
    bf, subplot = plt.subplots(figsize=(ops.ONE_COL, 3))
    for i in range(len(x)):
        subplot.plot(x[i], y[i], 'o', c='b', alpha=0.5, label='Raw data')
    subplot.plot(x, y_fit, c='r', label='Fitted')
    subplot.axvspan(0.5, 1.5, color='orange', alpha=0.3)
    cline = ef.create_custom_legend_patch('Critical zone', c='orange', alpha=0.3)
    ef.revamp_legend(subplot, loc='upper left', add_handles=[cline])
    ef.xy(subplot, x_origin=True, y_origin=True)

    eq = f'y = {ps[0]:.2g} \cdot x ^ 2 + {ps[1]:.2g} \cdot x + {ps[0]:.2f}'
    ef.text_at_rel_pos(subplot, 0.6, 0.1, '$%s$' % eq)

    subplot.set_xlabel('Pizza eaten [slices]')
    subplot.set_ylabel('My love for Pizza [J]')

    plt.tight_layout()
    # if you are using complex layouts then use GridSpec

    name = __file__.replace('.py', '')
    name = name.split("figure_")[-1]
    if save:
        bf.savefig(ap.PUB_FIG_PATH + name + ops.PUB_FIG_FILE_TYPE, dpi=ops.PUB_FIG_DPI)
        print(ef.latex_for_figure(ap.FIG_FOLDER, name, ops.PUB_FIG_FILE_TYPE))
    if show:
        plt.show()


if __name__ == '__main__':
    create(save=0, show=1)
