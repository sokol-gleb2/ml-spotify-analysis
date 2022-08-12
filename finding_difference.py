from data_cleaning import cleanData as data
import numpy as np
import matplotlib.pyplot as plt


regions = np.unique(data['Region'])
dates = np.unique(data['Date'])
tracks = np.unique(data['Track Name'])

positions = [[0]*len(regions) for _ in range(len(tracks))]

for track in range(5):
    trackData = data[data['Track Name'] == tracks[track]]
    for region in range(len(regions)):
        regionData = trackData[trackData['Region'] == regions[region]]
        position = []
        for date in dates:
            if regionData[regionData['Date'] == date].empty:
                position.append(201)
            else:
                position.append(regionData[regionData['Date'] == date]['Position'])
        # print(regions[region]+" "+tracks[track])
        # print(position)
        positions[track][region] = position

fig, ax = plt.subplots(figsize=(12, 5))
for reg in range(len(regions)):
    ax.plot(dates, positions[4][reg])
plt.show()

# difference = [[[0]*len(regions) for _ in range(len(regions))] for __ in range(len(tracks))]
# for i in range(len(tracks)):
#     for j in range(len(regions)):
#         for k in range(len(regions)):
#             for l in range(len(dates)):
#                 difference[i][j][k].append(position[i][j][l] - position[i][k][l])
# ## Over 19 billion itterations - will take 2/3 of the year to run :((
# print(difference)
