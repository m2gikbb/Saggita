import json
from pprint import pprint
from operator import itemgetter
import argparse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

parser = argparse.ArgumentParser()
parser.add_argument("spotify_client_id")
parser.add_argument("spotify_client_secret")
parser.add_argument("redirect_uri")
args = parser.parse_args()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=args.spotify_client_id,
                                               client_secret=args.spotify_client_secret,
                                               redirect_uri=args.redirect_uri,
                                               scope="user-library-read"))
def current_user_saved_tracks():
    results = sp.current_user_saved_tracks(limit=50)
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

def print_users_top_tracks(time_range='medium_term'):
    """Print sorted list of most popular tracks played by user.

    Keyword arguments:
    time_range -- string that can get 2 values: medium_term or long_term
    """
    with open(f'data/get-users-top-artists-and-tracks-{time_range}.json') as fp:
        data = json.load(fp)
        sorted_list = sorted(data['items'], key=itemgetter('popularity')) 
        formatted_list = list(map(lambda item: f"{item['popularity']} {item['artists'][0]['name']} - {item['name']}",sorted_list))
        pprint(formatted_list)

def print_all_plalists():
    """Print all playlist of current user."""
    file_name_counter = 1
    items = []
    while True:        
        try:
            with open(f'data/get-a-list-of-current-users-playlists_part_{file_name_counter}.json') as fp:
                data = json.load(fp)
                items += data['items']
                file_name_counter += 1
        except (OSError, IOError) as e:
            break
    
    sorted_list = sorted(items, key=lambda x: x['tracks']['total'],reverse=True) 
    formatted_list = list(map(lambda item: f"{item['name']} by {item['owner']['display_name']} contains {item['tracks']['total']} tracks",sorted_list))
    pprint(formatted_list)
    print(f'Total # of playlists {len(items)}')

def show_featured_playlists():
    response = sp.featured_playlists()
    print(response['message'])

    while response:
        playlists = response['playlists']
        for i, item in enumerate(playlists['items']):
            print(playlists['offset'] + i, item['name'])

        if playlists['next']:
            response = sp.next(playlists)
        else:
            response = None

# print_users_top_tracks('long_term')
# print_all_plalists()
# current_user_saved_tracks()
show_featured_playlists()