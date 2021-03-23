import random
from urllib import request, parse
import json
# from cogs.character_gen.models.Trait import *
from Trait import *

API_ROOT = 'https://www.dnd5eapi.co/api/'

def choose_from(obj, key):
    if key in obj:
        options =  obj[key]['from']
        num_choices = obj[key]['choose']
        return (options, num_choices)
    print("NO '{}' FOUND !!!".format(key))
    return ([], 0)

class CharacterStats:
    alignment = None
    ability_scores = {}
    
    race = None
    proficiencies = []
    speed = None
    size = None
    languages = []
    traits = {}

    _class = None
    hit_die = None
    saving_throws = []

    def __init__(self):
        self.alignment = random.choice(self.get_alignments())
        self.ability_scores = self.get_ability_scores()
        
        self.race = random.choice(self.get_races())
        self.resolve_race_benefits()
        print('Finished Race')

        self._class = random.choice(self.get_classes())
        self.resolve_class_benefits()
        print('Finished Class')

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
            result += '\t\t{}\n'.format(self.traits[trait].name)
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
        with request.urlopen(API_ROOT + 'races/' + self.race) as res:
            html = res.read().decode('utf-8')
            obj = json.loads(html)
            
            # ability score bonuses
            bonuses = obj['ability_bonuses']
            for bonus in bonuses:
                self.ability_scores[bonus['ability_score']['index']] += bonus['bonus']
            opt_bonuses, num_opt_bonuses = choose_from(obj, 'ability_bonus_options')
            opt_bonuses = opt_bonuses[:num_opt_bonuses]
            for opt_bonus in opt_bonuses:
                self.ability_scores[opt_bonus['ability_score']['index']] += opt_bonus['bonus']

            # basic traits
            self.speed = obj['speed']
            self.size = obj['size']

            # proficiencies
            self.resolve_stat_collection(self.proficiencies, 
                obj, 
                'starting_proficiencies', 
                'starting_proficiency_options')

            # languages
            self.resolve_stat_collection(self.languages, 
                obj, 
                'languages', 
                'language_options')

            # traits
            race_traits = [trait['index'] for trait in obj['traits']]
            for trait in race_traits:
                if trait not in self.traits:
                    self.traits[trait] = Trait(trait)

    def resolve_class_benefits(self):
        with request.urlopen(API_ROOT + 'classes/' + self._class) as res:
            html = res.read().decode('utf-8')
            obj = json.loads(html)

            # basic traits
            self.hit_die = obj['hit_die']
            saving_throws = obj['saving_throws']
            for st in saving_throws:
                if st['index'] not in self.saving_throws:
                    self.saving_throws.append(st['index'])

            # proficiencies
            profs = [prof['index'] for prof in obj['proficiencies']]
            for prof in profs:
                if prof not in self.proficiencies:
                    self.proficiencies.append(prof)

            # proficiencies
            self.resolve_stat_collection(self.proficiencies, 
                obj, 
                'proficiencies', 
                'proficiency_choices', 
                True)

            # equipment


if __name__ == '__main__':
    cs = CharacterStats()
    # print(cs)
    print(cs._class + '/' + cs.race)
    print(cs.hit_die)
    print(cs.proficiencies)
    print(cs.saving_throws)