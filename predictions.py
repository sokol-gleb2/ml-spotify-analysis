from merging import songAnalysisClean
from data_cleaning import cleanData as data
import pandas as pd


regions = pd.unique(data['Region'])

newData = pd.merge(data, songAnalysisClean, on="URL", how="left")
# newData = newData.dropna(axis=0, subset=['cluster_group'])
# print(newData)

a = newData[newData['cluster_group'] == 0]
print("Cluster 0: "+str(len(a)))
b = newData[newData['cluster_group'] == 1]
print("Cluster 1: "+str(len(b)))
c = newData[newData['cluster_group'] == 2]
print("Cluster 2: "+str(len(c)))

analysisA = a[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo']]
analysisB = b[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo']]
analysisC = c[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'tempo']]

pd.set_option('max_columns', None)

print("Cluster 0: ")
print(analysisA.describe())
print("\n")
print("Cluster 1: ")
print(analysisB.describe())
print("\n")
print("Cluster 2: ")
print(analysisC.describe())
print("\n")




countA = []
countB = []
countC = []

for i in range(len(regions)):
    countA.append((regions[i], len(a[a['Region'] == regions[i]]['Region'])))
    countB.append((regions[i], len(b[b['Region'] == regions[i]]['Region'])))
    countC.append((regions[i], len(c[c['Region'] == regions[i]]['Region'])))

print(countA)
print(countB)
print(countC)

countA.sort(key=lambda i:i[1],reverse=True)
countB.sort(key=lambda i:i[1],reverse=True)
countC.sort(key=lambda i:i[1],reverse=True)

print(countA)
print(countB)
print(countC)

## Need to print the countries for each cluster
## And analyze each cluster: mean, s.d, etc.
