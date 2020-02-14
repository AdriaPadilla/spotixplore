import spotipy
import json
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotify_track_data.credentials as cr

### CREDENTIALS

api_client_id = cr.SPOTIPY_CLIENT_ID
api_client_secret = cr.SPOTIPY_CLIENT_SECRET