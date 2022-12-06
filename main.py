# write the main functions here

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
from pprint import pprint
import random
import urllib.request

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

def get_artistID(artist_name):
    """
    Input: artist name (from the user)
    Output: bool (if input is accurate), artistID 
    """
    results = spotify.search(q=artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        correct_name = artist['name']
        if correct_name == artist_name:
            # print(artist['name'], artist['images'][0]['url'])
            return True, artist['id']
        else:
            # print(f'Oops, did you mean {correct_name}?')
            return False, correct_name
    else: 
        print("There is no artist with this name. Try again.")
        return True
    
def get_relatedArtists(artistID, num=10):
    """
    Input: artistID
    Output: list of related artists IDs
    """
    answers = spotify.artist_related_artists(artistID)
    related_artists = answers['artists']

    ids = []

    for i in range(num):
        if related_artists[i]['id'] != artistID:
            ids.append(related_artists[i]['id'])
        else:
            num +=1

    return ids

def rec_songs(list_artists_IDs, tracks_per_artist=2):
    """
    Input: list of artists IDs
    Output: dict of recommended tracks
    """
    tracks = {}
    for id in list_artists_IDs:
        answers = spotify.artist_top_tracks(id)
        answers = answers['tracks']
        if len(answers) == 0:  # edge case when artist has zero tracks
            continue
        sample_tracks = random.sample(answers, tracks_per_artist)

        for t in sample_tracks:
            track_id = t['id']
            track_name = t['name']
            track_artist = t['artists'][0]['name']
            track_url = t['external_urls']['spotify']
            tracks[track_id] = {'name': track_name, 'artist': track_artist, 'url': track_url}

    return tracks

def rec_albums(list_artists_IDs, albums_per_artist=1):
    """
    Input: list of artists IDs
    Output: dict of recommended albums
    """
    albums = {}
    for id in list_artists_IDs:
        answers = spotify.artist_albums(id, 'album', 'US')
        answers = answers['items']
        if len(answers) == 0:  # edge case when artist has zero albums
            continue
        sample_albums = random.sample(answers, albums_per_artist)

        for a in sample_albums:
            album_id = a['id']
            album_name = a['name']
            album_artist = a['artists'][0]['name']
            album_url = a['external_urls']['spotify']
            albums[album_id] = {'name': album_name, 'artist': album_artist, 'url': album_url}
        
    return albums

def get_artist(artistID):
    return spotify.artist(artistID)

def main():
    id = get_artistID('Bruno Mars')
    # related = get_relatedArtists(id[1])
    # pprint(rec_albums(related))
    # pprint(get_artist(id[1]))
    # artist_img = get_artist(id[1])['images'][-1]['url']
    # urllib.request.urlretrieve(artist_img, "data/image.jpg")

if __name__ == '__main__':
    main()