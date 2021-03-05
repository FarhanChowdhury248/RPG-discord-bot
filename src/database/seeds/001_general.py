import os
import json

PATH_TO_DATA = os.path.dirname(__file__)

def get_path(file):
    return os.path.join(PATH_TO_DATA, 'data', '{}.json'.format(file))

with open(get_path('general'), 'w+') as f:
    data = {
        'server_prefix': {
            'default': '.'
        }
    }
    json.dump(data, f, indent=4, sort_keys=True)
    print('\tSeeded default settings')