import spotipy
import sys
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# load environmental variables (the api keys & id)
load_dotenv()
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
))

def get_pic_url(artist_name):
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = artist_name #'Kendrick Lamar' # should suggest what artist as end user starts typing in website 

    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        print(artist['name'], artist['images'][0]['url'])

        pic = artist['images'][0]['url']
    return pic 

