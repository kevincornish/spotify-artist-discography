import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

## Load enviroment varibles
load_dotenv()
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def search_artist(artist):
    """
    This function will search the spotify api for the given artist name and return the first found artist_uri
    """
    results = spotify.search(q="artist:" + artist, type="artist")
    items = results["artists"]["items"]

    ## Not had any issue with it yet, but I can imagine someone may run into an issue with an artist of the same name with less popularity
    if len(items) > 0:
        artist = items[0]
    artist_uri = artist["uri"]
    return artist_uri


def find_albums(artist):
    """
    This function will search the spotify api for the given artist_uri, loop through the page results, build a list of albums and remove the duplicates
    """
    results = spotify.artist_albums(artist_uri, album_type="album")
    albums = results["items"]
    while results["next"]:
        results = spotify.next(results)
        albums.extend(results["items"])
    album_name = []
    for album in albums:
        album_name.append(album["name"])

    no_dupes = [x for n, x in enumerate(album_name) if x not in album_name[:n]]
    return no_dupes


## Lets grab the artist list
with open("artists.txt") as f:
    artists = f.read().splitlines()

discography = {}

##FIXME: added a try / except here for when spotify doesn't match an artist
for artist in artists:
    try:
        artist_uri = search_artist(artist)
    except (TypeError):
        print("no artist found")
        continue
    albums = find_albums(artist_uri)
    discography[artist] = {"albums": albums}

# Show results
print(json.dumps(discography, indent=4))
