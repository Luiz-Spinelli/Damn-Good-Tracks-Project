# write the main functions here

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))


