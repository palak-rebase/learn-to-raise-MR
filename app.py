import lyricsgenius
client_access_token= ''
genius = lyricsgenius.Genius(client_access_token)
search_term = "Andy Shauf"
# genius = Genius()
artist = genius.search_artist(search_term, max_songs=50, sort="title")
print(artist.songs)

