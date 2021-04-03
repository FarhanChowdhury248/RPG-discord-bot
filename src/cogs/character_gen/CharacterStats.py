import random
from urllib import request, parse
import json
import traceback

if __name__ == '__main__':
    from Trait import *
    from Equipment import *
else:
    from cogs.character_gen.Trait import *
    from cogs.character_gen.Equipment import *

API_ROOT = 'https://www.dnd5eapi.co/api/'

LOG_MSG = ''

def log(msg, priority=0):
    global LOG_MSG
    LOG_MSG += priority * '\t' + msg.strip() + '\n'

''' 
Maps class to class_data 
class: str representing the index of the class as found in the api
data: tuple containing (
    int: spell slots at 1st lvl, 
    int: spells learned at 1st lvl, -1 if all are known,
    bool: True if preparing, False if casting, None if non-caster
    )
'''
CLASS_TO_DATA = {
    'barbarian': (0, 0, None),
    'bard': (2, 4, False),
    'cleric': (2, -1, True),
    'druid': (2, -1, True),
    'fighter': (0, 0, None),
    'monk': (0, 0, None),
    'paladin': (0, 0, None),
    'ranger': (0, 0, None),
    'rogue': (0, 0, None),
    'sorcerer': (2, 2, False),
    'warlock': (1, 2, False),
    'wizard': (2, 6, True)
}

'''
Maps armor type to function that can calculate armor class
armor type: str representing the index of the armor type
function: anonymous function mapping dex bonus to ac
'''
ARMOR_TO_AC = {
    'padded': lambda x: 11 + x,
    'leather': lambda x: 11 + x,
    'studded-leather': lambda x: 12 + x,
    'hide': lambda x: 12 + min(x, 2),
    'chain-shirt': lambda x: 13 + min(x, 2),
    'scale-mail': lambda x: 14 + min(x, 2),
    'breastplate': lambda x: 14 + min(x, 2),
    'half-plate': lambda x: 15 + min(x, 2),
    'ring-mail': lambda x: 14,
    'chain-mail': lambda x: 16,
    'splint': lambda x: 17,
    'chain-shirt': lambda x: 18,
    'natural': lambda x: 10 + x
}

def query_api(suffix):
    with request.urlopen(API_ROOT + suffix) as res:
        html = res.read().decode('utf-8')
        return json.loads(html)

def choose_from(obj, key):
    if key in obj:
        options =  obj[key]['from']
        num_choices = obj[key]['choose']
        return (options, num_choices)
    log("Warning: NO '{}' FOUND !!!".format(key), 1)
    return ([], 0)

class CharacterStats:
    def __init__(self):
        self.alignment = None
        self.ability_scores = {}
        self.proficiency_bonus = None
        self.ac = None
        self.hit_points = None
        self.passive_perception = None
        
        self.race = None
        self.proficiencies = []
        self.speed = None
        self.size = None
        self.languages = []
        self.traits = []

        self._class = None
        self.hit_die = None
        self.saving_throws = []
        self.equipment = []

        self.spellcasting_ability = None
        self.known_spells = []
        self.prepared_spells = []
        self.spell_slots = {}
        for i in range(1, 10):
            self.spell_slots[i] = 0

        self.alignment = random.choice(self.get_alignments())
        self.ability_scores = self.get_ability_scores()
        self.proficiency_bonus = 2
        
        self.race = random.choice(self.get_races())
        log('Race: ' + str(self.race))
        self.resolve_race_benefits()
        log('Finished Race')

        self._class = random.choice(self.get_classes())
        log('Class: ' + str(self._class))
        self.resolve_class_benefits()
        log('Finished Class')

        self.resolve_armor_class()
        self.resolve_hit_points()
        self.resolve_passive_perception()

    def resolve_armor_class(self):
        valid_armors = [e.index for e in self.equipment if e.index in ARMOR_TO_AC]
        mod = self.get_modifier('dex')
        ac = 0
        if len(valid_armors) == 0:
            ac = ARMOR_TO_AC['natural'](mod)
        else:
            for armor in valid_armors:
                ac = max(ac, ARMOR_TO_AC[armor](mod))
        self.ac = ac
        log('Armor Class: {}'.format(self.ac))

    def resolve_hit_points(self):
        self.hit_points = self.hit_die + self.get_modifier('con')

    def resolve_passive_perception(self):
        self.passive_perception = 10 + self.proficiency_bonus + self.get_modifier('wis')

    def __repr__(self):
        result = 'Character:\n'
        result += '\tAlignment: {}\n'.format(self.alignment)
        result += '\tRace: {}\n'.format(self.race)
        result += '\tSize: {}\n'.format(self.size)
        result += '\tSpeed: {}\n'.format(self.speed)
        
        result += '\tAbility Scores:\n'
        for key in self.ability_scores:
            result += '\t\t{} - {} (+{})\n'.format(
                key.upper(), 
                self.ability_scores[key],
                (self.ability_scores[key] - 10) // 2)

        result += '\tProficiencies:\n'
        for prof in self.proficiencies:
            result += '\t\t{}\n'.format(prof)

        result += '\tLanguages:\n'
        for lang in self.languages:
            result += '\t\t{}\n'.format(lang)

        result += '\tTraits:\n'
        for trait in self.traits:
            result += '\t\t{}\n'.format(trait.name)
        return result

    def get_alignments(self):
        xs = ['chaotic', 'neutral', 'lawful']
        ys = ['evil', 'neutral', 'good']
        results = [x + ' ' + y if x != 'neutral' or y != 'neutral' else 'true neutral' for x in xs for y in ys]
        return results

    def get_races(self):
        with request.urlopen(API_ROOT + 'races') as res:
            html = res.read().decode('utf-8')
            obj = json.loads(html)
            return [key['index'] for key in obj['results']]

    def get_classes(self):
        with request.urlopen(API_ROOT + 'classes') as res:
            html = res.read().decode('utf-8')
            obj = json.loads(html)
            return [key['index'] for key in obj['results']]

    def get_ability_scores(self):
        def calc_score():
            rolls = [random.randint(1, 6) for i in range(4)]
            return sum(rolls) - min(rolls)
        traits = ['str', 'dex', 'con', 'int', 'wis', 'cha']
        scores = {}
        for t in traits:
            scores[t] = calc_score()
        return scores

    def get_modifier(self, stat):
        return (self.ability_scores[stat] - 10) // 2

    def resolve_stat_collection(self, stat_collection, obj, mandatory_choices, optional_choices, optional_has_list=False):
        choices = [choice['index'] for choice in obj[mandatory_choices]]
        for choice in choices:
            if choice not in stat_collection:
                stat_collection.append(choice)

        def process_option_set(opt_choices, num_opt_choices):
            random.shuffle(opt_choices)
            opt_choices_count = 0
            for opt_choice in opt_choices:
                if opt_choice['index'] not in stat_collection:
                    if opt_choices_count == num_opt_choices:
                        break
                    stat_collection.append(opt_choice['index'])
                    opt_choices_count += 1
        
        if optional_has_list:
            if optional_choices in obj:
                option_sets =  obj[optional_choices]
                for opt_set in option_sets:
                    process_option_set(opt_set['from'], opt_set['choose'])
            else:
                print("NO '{}' FOUND !!!".format(optional_choices))
        else:
            opt_choices, num_opt_choices = choose_from(obj, optional_choices)
            process_option_set(opt_choices, num_opt_choices)

    def resolve_race_benefits(self):
        race_data = query_api('races/' + self.race)
            
        # ability score bonuses
        bonuses = race_data['ability_bonuses']
        for bonus in bonuses:
            self.ability_scores[bonus['ability_score']['index']] += bonus['bonus']
        opt_bonuses, num_opt_bonuses = choose_from(race_data, 'ability_bonus_options')
        opt_bonuses = opt_bonuses[:num_opt_bonuses]
        for opt_bonus in opt_bonuses:
            self.ability_scores[opt_bonus['ability_score']['index']] += opt_bonus['bonus']
        log('Ability Scores: {}'.format(self.ability_scores), 1)

        # basic traits
        self.speed = race_data['speed']
        self.size = race_data['size']
        log('Speed: {}'.format(self.speed), 1)
        log('Size: {}'.format(self.size), 1)

        # proficiencies
        self.resolve_stat_collection(self.proficiencies, 
            race_data, 
            'starting_proficiencies', 
            'starting_proficiency_options')
        log('Proficiencies: {}'.format(self.proficiencies), 1)

        # languages
        self.resolve_stat_collection(self.languages, 
            race_data, 
            'languages', 
            'language_options')
        log('Languages: {}'.format(self.languages), 1)

        # traits
        race_traits = [trait['index'] for trait in race_data['traits']]
        for trait in race_traits:
            if trait not in self.traits:
                self.traits.append(Trait(trait))
        log('Traits: {}'.format(self.traits), 1)

    def add_equipment(self, equipment):
        not_found = True
        for e in self.equipment:
            if equipment == e:
                not_found = False
                e.add(equipment.quantity)
                break
        if not_found:
            self.equipment.append(equipment)

    def resolve_class_benefits(self):
        class_data = query_api('classes/' + self._class)

        # basic traits
        self.hit_die = class_data['hit_die']
        saving_throws = class_data['saving_throws']
        for st in saving_throws:
            if st['index'] not in self.saving_throws:
                self.saving_throws.append(st['index'])
        log('Hit die: {}'.format(self.hit_die), 1)
        log('Saving Throws: {}'.format(self.saving_throws), 1)

        # proficiencies
        self.resolve_stat_collection(self.proficiencies, 
            class_data, 
            'proficiencies', 
            'proficiency_choices', 
            True)
        log('Proficiencies: {}'.format(self.proficiencies), 1)

        # equipment
        for e in class_data['starting_equipment']:
            self.add_equipment(Equipment(e))
        opt_equip_sets = class_data['starting_equipment_options']
        for opt_equip_set in opt_equip_sets:
            opt_equips, num_opt_equips = choose_from({'key': opt_equip_set}, 'key')
            opt_equips = opt_equips[:num_opt_equips]
            random.shuffle(opt_equips)
            for opt_equip in opt_equips:
                if 'equipment' in opt_equip:
                    self.add_equipment(Equipment(opt_equip))
        log('Equipment: {}'.format(self.equipment), 1)

        # spellcasting
        if 'spellcasting' in class_data:
            self.spellcasting_ability = class_data['spellcasting']['spellcasting_ability']['index']
        
            relevant_spells = [spell['index'] for spell in query_api('classes/{}/levels/1/spells'.format(self._class))['results']]
            
            spell_slots, spells_learned, is_preparing = CLASS_TO_DATA[self._class]
            self.spell_slots[1] = spell_slots
            random.shuffle(relevant_spells)
            if spells_learned != -1:
                self.known_spells = relevant_spells[:spells_learned]
            else:
                self.known_spells = relevant_spells
            if is_preparing:
                random.shuffle(self.known_spells)
                self.prepared_spells = self.known_spells[:max(1, 1 + self.get_modifier(self.spellcasting_ability))]
        
        log('Spellcasting Ability: {}'.format(self.spellcasting_ability), 1)
        log('Known Spells: {}'.format(self.known_spells), 1)
        log('Prepared Spells: {}'.format(self.prepared_spells), 1)

if __name__ == '__main__':
    try:
        cs = CharacterStats()
    except Exception as e:
        log('ERROR: {}'.format(traceback.format_exc()))
    finally:
        print(LOG_MSG)