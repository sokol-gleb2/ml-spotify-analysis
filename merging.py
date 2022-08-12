## How about we first group tracks into similar music groups using spotipy
## Then we test the hypothesis that songs with similar genre are liked by same regions

from spotipy_ops import songAnalysis, urls, randomSample
from data_cleaning import cleanData as data
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
import seaborn as sns

## Merging the databases: -----------------------------------------------------

# newData = pd.merge(data, songAnalysis, left_index=True, right_index=True)

##------------------------------------------------------------------------------





songAnalysisClean = songAnalysis.dropna(axis=0)
XS = songAnalysisClean[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo']]

X = XS.to_numpy()
linked = linkage(X, 'single')
labelList = randomSample





## Plotting Dendograms: --------------------------------------------------------

# plt.figure(figsize=(17, 8))
# plt.title("Song Dendograms")
# dend = shc.dendrogram(shc.linkage(X, method='ward'))
# plt.show()

##------------------------------------------------------------------------------





## Song Attributes Correlation Heatmap: ----------------------------------------

# f, ax = plt.subplots(figsize=(17, 8))
# corr = XS.corr()
# hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f',
#                  linewidths=.05)
# f.subplots_adjust(top=0.93)
# t= f.suptitle('Song Attributes Correlation Heatmap', fontsize=14)
# plt.show()

##------------------------------------------------------------------------------






## Creating Clusters: ----------------------------------------------------------

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
cluster.fit_predict(X)
clustersGroups = cluster.labels_

##------------------------------------------------------------------------------



## Need to add clustersGroups to songAnalysisClean:
songAnalysisClean['cluster_group'] = clustersGroups
# print(songAnalysisClean['URL'])



## Visualizing Clusters: -------------------------------------------------------

# fig, ax = plt.subplots(2, 2, figsize=(17, 8))
# ax[0][0].scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')
# ax[0][0].set_title("danceability vs energy")
#
# ax[0][1].scatter(X[:,2],X[:,3], c=cluster.labels_, cmap='rainbow')
# ax[0][1].set_title("loudness vs speechiness")
#
# ax[1][0].scatter(X[:,4],X[:,5], c=cluster.labels_, cmap='rainbow')
# ax[1][0].set_title("acousticness vs instrumentalness")
#
# ax[1][1].scatter(X[:,6],X[:,7], c=cluster.labels_, cmap='rainbow')
# ax[1][1].set_title("liveness vs tempo")
# plt.show()

##------------------------------------------------------------------------------





## Plotting Dendogram: ---------------------------------------------------------

# plt.figure(figsize=(17, 8))
# dendrogram(linked,
#             orientation='top',
#             labels=labelList,
#             distance_sort='descending',
#             show_leaf_counts=True)
# plt.show()

##------------------------------------------------------------------------------
