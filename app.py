import lyricsgenius
import pandas as pd
client_access_token= ''
genius = lyricsgenius.Genius(client_access_token)

artist = pd.read_csv('solo_artist_01_11.csv')
list1 = artist['name'].tolist()
data = pd.DataFrame()

for i in list1[10:15]:
    print(i)
    try:
        artist = genius.search_artist(i, sort="popularity")
        a=artist.songs
        for j in range(500):
            try:
                ab = [a[j].artist,a[j].title,a[j].lyrics]
                pq=pd.DataFrame(ab).T
                data = data.append(pq)
            except IndexError:
                pass
    except TimeoutError:
        pass        
        
    


# type(a)
# len(a)
# data


# for j in range(500):
#     try:
#         ab = [a[j].artist,a[j].title,a[j].lyrics]
#         pq=pd.DataFrame(ab).T
#         data = data.append(pq)
#     except IndexError:
#         pass

# data

# list12 = []

# for i in range(len(a)):
#     list12.append(a[i])

