import random
from urllib import request, parse
import json
# from cogs.character_gen.models.Trait import *
from Trait import *

def choose_from(obj, key):
    if key in obj:
        options = obj[key]['from']
        num_choices = obj[key]['choose']
        random.shuffle(options)
        return options[:num_choices]
    return []

class CharacterStats:
    alignment = None
    ability_scores = {}
    race = None
    proficiencies = []
    speed = None
    size = None
    languages = []
    traits = {}

    def __init__(self):
        self.alignment = random.choice(self.get_alignments())
        self.ability_scores = self.get_ability_scores()
        
        self.race = random.choice(self.get_races())
        self.resolve_race_benefits()

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
        with request.urlopen('https://www.dnd5eapi.co/api/races') as res:
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

    def resolve_race_benefits(self):
        with request.urlopen('https://www.dnd5eapi.co/api/races/' + self.race) as res:
            html = res.read().decode('utf-8')
            obj = json.loads(html)
            
            # ability score bonuses
            bonuses = obj['ability_bonuses']
            for bonus in bonuses:
                self.ability_scores[bonus['ability_score']['index']] += bonus['bonus']
            opt_bonuses = choose_from(obj, 'ability_bonus_options')
            for opt_bonus in opt_bonuses:
                self.ability_scores[opt_bonus['ability_score']['index']] += opt_bonus['bonus']

            # basic traits
            self.speed = obj['speed']
            self.size = obj['size']

            # proficiencies
            self.proficiencies += [prof['index'] for prof in obj['starting_proficiencies']]
            opt_profs = choose_from(obj, 'starting_proficiency_options')
            for opt_prof in opt_profs:
                self.proficiencies.append(opt_prof['index'])

            # languages
            self.languages += [lang['index'] for lang in obj['languages']]
            opt_langs = choose_from(obj, 'language_options')
            for opt_lang in opt_langs:
                self.languages.append(opt_lang['index'])

            # traits
            race_traits = [trait['index'] for trait in obj['traits']]
            for trait in race_traits:
                if trait not in self.traits:
                    self.traits[trait] = Trait(trait)

if __name__ == '__main__':
    cs = CharacterStats()
    print(cs, end='')