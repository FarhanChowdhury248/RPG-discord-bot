from urllib import request
import json

API_ROOT = 'https://www.dnd5eapi.co/api/traits/'

class Trait:
    index = None
    name = None
    desc = None

    def __init__(self, trait_index):
        self.index = trait_index
        
        with request.urlopen(API_ROOT + trait_index) as res:
            html = res.read().decode('utf-8')
            obj = json.loads(html)
            self.name = obj['name']
            self.desc = " ".join(obj['desc'])

    def __repr__(self):
        result = '{}'.format(self.name)
        return result

    def __eq__(self, other):
        if type(other) == type(''):
            return self.index == other or self.name == other
        elif type(other) == type(self):
            return self.index == other.index

if __name__ == '__main__':
    traits = ['fey-ancestry']
    for t in traits:
        print(Trait(t))