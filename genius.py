import lyricsgenius
import os
from dotenv import load_dotenv

# load environmental variables (the api key)
load_dotenv()
access_token= os.getenv('accessToken')

def return_lyrics(name_of_artist, access_token):
    # return lyrics 
    genius = lyricsgenius.Genius(access_token)
    genius.remove_section_headers = True
    genius.skip_non_songs = True
    artist = genius.search_artist(name_of_artist, max_songs = 3)
    songs = artist.songs
    # print(songs)
    # print(type(songs))
    lyrics_list = []
    for ele in songs:
        #print(ele.lyrics)
        lyrics_list.append(str(ele.lyrics))

    return " ".join(lyrics_list)

