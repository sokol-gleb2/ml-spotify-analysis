import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from data_cleaning import cleanData
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="9c76ed5fd36b4b178383320170fbbb82",
                                                           client_secret="b44b3a55a6524aff8188c43e402c0083"))



## Wasn't running at first: timeout error - had to run: sudo pip install --default-timeout=100 future



columnsDF = []
columnsDF.append('URL')
for url in cleanData['URL']:
    # danceability.append(sp.audio_features(url)[0]['danceability'])
    for i in sp.audio_features(url)[0].keys():
        columnsDF.append(i)
    break


urls = pd.unique(cleanData['URL'])
# songAnalysis = pd.DataFrame(columns=columnsDF, index=urls)
songAnalysis = pd.DataFrame(columns=columnsDF)

exceptionsURL = []
count = 0

# randomSample = random.sample(range(1, len(urls)), int(len(urls)/2))
randomSample = random.sample(range(1, len(urls)), 100)
# print(randomSample)
# for i in randomSample:
#     print(cleanData[cleanData['URL'] == urls[i]]['Region'])

for url in range(len(urls)): ##len(urls)
    row = []
    try:
        row.append(urls[url])
        for i in sp.audio_features(urls[url])[0].values():
            row.append(i)
        songAnalysis.loc[url] = row
        count += 1
        print(count)
    except AttributeError:
        exceptionsURL.append(urls[url])
        print(urls[url])
        # print(songAnalysis)

    except ReadTimeout:
        exceptionsURL.append(urls[randomSample[url]])
        # print(cleanData['URL'][url])


# fig, ax = plt.subplots(111, projection='3d')
# ax.scatter(songAnalysis['danceability'], songAnalysis['energy'], songAnalysis['loudness'], songAnalysis['speechiness'])
# plt.show()


## Histograms:

# fig, ax = plt.subplots(4, 2, figsize=(17, 8))
# fig.tight_layout()
# ax[0][0].hist(songAnalysis['danceability'])
# ax[0][0].set_title("Danceability")
#
# ax[0][1].hist(songAnalysis['energy'])
# ax[0][1].set_title("Energy")
#
# ax[1][0].hist(songAnalysis['loudness'])
# ax[1][0].set_title("Loudness")
#
# ax[1][1].hist(songAnalysis['speechiness'])
# ax[1][1].set_title("Speechiness")
#
# ax[2][0].hist(songAnalysis['acousticness'])
# ax[2][0].set_title("Acousticness")
#
# ax[2][1].hist(songAnalysis['instrumentalness'])
# ax[2][1].set_title("Instrumentalness")
#
# ax[3][0].hist(songAnalysis['liveness'])
# ax[3][0].set_title("Liveness")
#
# ax[3][1].hist(songAnalysis['tempo'])
# ax[3][1].set_title("Tempo")
# plt.show()
