import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap
import pandas as pd


def create():
    df = pd.read_csv(ap.MODULE_DATA_PATH + 'basic_raw_data.csv')

    dfsmall = df[df['x'] < 3]
    bf, subplot = plt.subplots()
    subplot.plot(df['x'], df['y'], c='r')
    subplot.plot(dfsmall['x'], dfsmall['y'], c='b')
    plt.show()


if __name__ == '__main__':
    create()
