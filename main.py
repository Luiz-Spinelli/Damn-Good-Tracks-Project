# write the main functions here

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
from pprint import pprint

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

def get_artistID(artist_name):
    """
    Input: artist name 
    output: artistID 
    """
    results = spotify.search(q=artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        correct_name = artist['name']
        if correct_name == artist_name:
            # print(artist['name'], artist['images'][0]['url'])
            return artist['id']
        else:
            print(f'Oops, did you mean {correct_name}?')
            return True
    else: 
        print("There is no artist with this name. Try again.")
        return True
    
def get_relatedArtists(artistID, num=10):
    """
    Input: artistID
    Output: list of related artists ID
    """
    answers = spotify.artist_related_artists(artistID)
    related_artists = answers['artists']
    ids = []

    for i in range(num):
        ids.append(related_artists[i]['id'])

    return ids

def rec_songs(list_artists_IDs):
    """
    Input: list of related artits ID
    Recommendation algorithm (proposed by me & Bruno)
        - pick to 10 related artists
        - pick each related artists top 5 songs 
        - assign all 50 songs into a list
        - randomize by picking 20 out of 50 songs 
    Output: list of track IDs
    """
    tracks = []
    for id in list_artists_IDs:
        output = spotify.artist_top_tracks(id)
        answers = output['tracks']
        for t in answers:
            tracks.append(t['name'])

    return tracks

def rec_albums(list_artists_IDs):
    """
    Input: list of related artits IDs
    Recommendation algorithm/logic = TBD
        - Pick 1 randomized album for each artist
    Output: list of 10 final related 
    """

def main():
    id = get_artistID('Kanye West')
    related = get_relatedArtists(id)
    pprint(rec_songs(related))

if __name__ == '__main__':
    main()