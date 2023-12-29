import json
from pprint import pprint
from operator import itemgetter


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

# print_users_top_tracks('long_term')
print_all_plalists()