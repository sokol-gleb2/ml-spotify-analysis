import pandas as pd


data = pd.read_csv('https://www.inf.ed.ac.uk/teaching/courses/fds/data/project-2021-2022/spotify/data.csv.zip')



# for i in data.columns:
#     print(str(i)+" : "+str(data[i].isna().sum()))

## Output:
# Position : 0
# Track Name : 657
# Artist : 657
# Streams : 0
# URL : 8
# Date : 0
# Region : 0

# So only 657 rows of over 3 million was removed so not enough to be significant


# print(data[data['Track Name'].isna()])

cleanData = data.dropna(axis=0, subset=['Track Name', 'Artist'])
# cleanData.set_index('URL')
#
# print(cleanData.index)
# print(cleanData['URL'])
# for i in range(len(cleanData['URL'])):
#     if cleanData['URL'].loc[i] == "https://open.spotify.com/track/27ebni0DfbT5Owz6W42HP8":
#         print(cleanData['URL'].loc[i+1])

# for i in cleanData.columns:
#     print(str(i)+" : "+str(cleanData[i].isna().sum()))
