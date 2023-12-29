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

print_users_top_tracks('long_term')