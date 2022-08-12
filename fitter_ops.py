from fitter import Fitter
from data_cleaning import cleanData as data
import numpy as np
import matplotlib.pyplot as plt

regions = np.unique(data['Region'])
dates = np.unique(data['Date'])
tracks = np.unique(data['Track Name'])


for track in tracks:
    trackData = data[data['Track Name'] == track]
    for region in regions:
        regionData = trackData[trackData['Region'] == region]
        position = []
        for date in dates:
            p = regionData[regionData['Date'] == date]
            if p.empty:
                position.append(201)
            else:
                position.append(p['Position'])
        # fig, ax = plt.subplots(figsize=(12, 5))
        # ax.plot(dates, position)
        # plt.show()
        f = Fitter(position, distributions=['gamma', 'norm', 'uniform'])
        f.fit()
        print(f.summary())

    
