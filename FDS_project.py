import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D
import math

dat = pd.read_csv('https://www.inf.ed.ac.uk/teaching/courses/fds/data/project-2021-2022/spotify/data.csv.zip')




def groupByDates(type, name):

    # print(len(dat['Position'])/200)

    top = dat[dat['Position'] == 1]
    regions = pd.unique(dat['Region'])

    rows, cols = (54, 374)
    shared = [[0]*cols]*rows
    data = []
    for i in range(54):
        shared[i] = top[top['Region'] == regions[i]]
    for i in shared:
        for j in range(len(i)):
            if i.iloc[j][type] == name:
                data.append(i.iloc[j])
                # print(i.iloc[j]['Region'] + " : " + i.iloc[j]['Date'])

    dates = []
    for i in data:
        if i['Date'] not in dates: dates.append(i['Date'])

    for i in dates:
        print(i + " {")
        for j in data:
            if j['Date'] == i:
                print("     " + j['Region'])
        print("}")
        print("\n")




# groupByDates("Track Name", "All That Is or Ever Was or Ever Will Be")



def visual1(type, name):
    regions = pd.unique(dat['Region'])
    regions1 = [regions[0:3], regions[3:6], regions[6:9]]
    regions2 = [regions[9:12], regions[12:15], regions[15:18]]
    regions3 = [regions[18:21], regions[21:24], regions[24:27]]
    regions4 = [regions[27:30], regions[30:33], regions[33:36]]
    regions5 = [regions[36:39], regions[39:42], regions[42:45]]
    regions6 = [regions[45:48], regions[48:51], regions[51:54]]

    fig, ax = plt.subplots(3, 3, figsize=(17, 8))
    fig.tight_layout()

    dates = np.unique(dat['Date'])


    for i in range(3):
        for j in range(3):
            region = regions6[i][j]
            data = dat[(dat['Region'] == region)]
            plotData = []
            for k in dates:
                if data[(data['Date'] == k) & (data[type] == name)].empty:
                    plotData.append(200)
                else:
                    plotData.append(data[(data['Date'] == k) & (data[type] == name)]['Position'])

            print(plotData)
            ax[i, j].set_title(region)
            ax[i, j].plot(dates, plotData)
            plt.setp(ax, ylim=[200, 0], ylabel='Position')


    plt.show()

visual1("Track Name", "Starboy")


def regionsWithBiggestSimilarities():
    return 0
