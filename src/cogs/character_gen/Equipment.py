from urllib import request
import json

API_ROOT = 'https://www.dnd5eapi.co/api/equipment/'

class Equipment:
    index = None
    name = None
    quantity = 1

    def __init__(self, equipment_obj):
        self.index = equipment_obj['equipment']['index']
        if 'quantity' in equipment_obj:
            self.quantity = equipment_obj['quantity']

        with request.urlopen(API_ROOT + self.index) as res:
            html = res.read().decode('utf-8')
            obj = json.loads(html)
            self.name = obj['name']

    def __eq__(self, other):
        return type(other) == type(self) and self.name == other.name

    def __repr__(self):
        return '{} ({})'.format(self.name, self.quantity)

    def add(self, amount):
        self.quantity += amount
    
    def remove(self, amount=1):
        self.quantity -= amount

if __name__ == '__main__':
    explorers_pack = {
        "equipment": {
            "index": "explorers-pack",
            "name": "Explorer's Pack",
            "url": "/api/equipment/explorers-pack"
        },
		"quantity": 1
    }
    explorers_pack_dup = {
        "equipment": {
            "index": "explorers-pack",
            "name": "Explorer's Pack",
            "url": "/api/equipment/explorers-pack"
        },
		"quantity": 1
    }
    javelins = {
        "equipment": {
            "index": "javelin",
            "name": "Javelin",
            "url": "/api/equipment/javelin"
        },
		"quantity": 4
    }
    equipment = [explorers_pack, javelins]
    for e in equipment:
        print(Equipment(e))
    print(explorers_pack == explorers_pack_dup)