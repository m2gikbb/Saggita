import json
from pprint import pprint
from operator import itemgetter

filename = 'data/get-users-top-artists-and-tracks-medium_term.json'
# filename = 'data/get-users-top-artists-and-tracks-long_term.json'

with open(filename) as fp:
    data = json.load(fp)
    # print(json.dumps(data, indent=1, sort_keys=True))
    # print(list(data.keys()))
    # pprint(data['items'])
    sorted_list = sorted(data['items'], key=itemgetter('popularity')) 
    formatted_list = list(map(lambda item: f"{item['popularity']} {item['artists'][0]['name']} - {item['name']}",sorted_list))
    pprint(formatted_list)
