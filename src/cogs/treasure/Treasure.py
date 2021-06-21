import discord
from discord.ext import commands, tasks
from urllib import request, parse
import json
from database.JSONDatabaseController import JSONDatabaseController
from database.JSONCollection import JSONCollection
from random import randint, choice

API_ROOT = 'https://www.dnd5eapi.co/api/'

def query_api(suffix):
    with request.urlopen(API_ROOT + suffix) as res:
        html = res.read().decode('utf-8')
        return json.loads(html)

def find_bracket_key(target, brackets):
    target_int = int(target)
    copy_brackets = [int(br) for br in brackets]
    copy_brackets.sort()
    key = None
    for br in copy_brackets:
        key = br
        if target_int <= br:
            break
    return str(key)


class Treasure(commands.Cog):
    def __init__(self, client):
        self.client = client

    def do_coin_roll(self, roll):
        roll_value = 0
        for i in range(int(roll['num_dice'])):
            roll_value += randint(1, int(roll['die_type']))
        return roll_value * int(roll['multiplier']), roll['piece_type']

    def do_valuable_roll(self, roll):
        roll_value = 0
        for i in range(int(roll['num_dice'])):
            roll_value += randint(1, int(roll['die_type']))
        return roll_value, int(roll['value']), roll['valuable_type']

    def do_roll(self, num_dice, die_type):
        roll_value = 0
        for i in range(int(num_dice)):
            roll_value += randint(1, int(die_type))
        return roll_value

    def parse_valuable_roll(self, num_valuables, valuable_worth, valuable_type):
        valuable_data = JSONDatabaseController().get_collection('loot').get_document('{}s'.format(valuable_type))
        all_choices = valuable_data[str(valuable_worth)]
        selected_choices = {}
        for i in range(int(num_valuables)):
            cur_choice = choice(all_choices)
            if cur_choice in selected_choices:
                selected_choices[cur_choice] +=  1
            else:
                selected_choices[cur_choice] = 1
        return [(selected_choices[val], val) for val in selected_choices]

    def process_magic_item_roll(self, num_items, table_type):
        magic_items_data = JSONDatabaseController().get_collection('loot').get_document('magic items')[table_type]
        rolled_items = {}
        for i in range(int(num_items)):
            d100_roll = randint(1, 100)
            roll_bracket = find_bracket_key(d100_roll, magic_items_data.keys())
            if magic_items_data[roll_bracket] in rolled_items:
                rolled_items[magic_items_data[roll_bracket]] += 1
            else:
                rolled_items[magic_items_data[roll_bracket]] = 1
        return ['{} ({})'.format(key, rolled_items[key]) for key in rolled_items]

    @commands.command()
    async def getIndTreasure(self, ctx, target_cr):
        target_cr_int = int(target_cr)
        
        treasure_data = JSONDatabaseController().get_collection('loot').get_document('individual treasure')
        cr_bracket = find_bracket_key(target_cr_int, treasure_data.keys())
        
        roll_data = treasure_data[cr_bracket]
        roll = randint(1, 100)
        roll_bracket = find_bracket_key(roll, roll_data.keys())
        
        rolls = roll_data[roll_bracket]
        coin_rolls = []
        for r in rolls:
            coin_rolls.append(self.do_coin_roll(r))

        embed = discord.Embed(
            title = 'Rolling For Individual Treasure',
            colour = discord.Color.blue()
        )
        embed.add_field(name = 'D100 Roll', value = roll, inline = False)
        embed.add_field(
            name = 'Treasure Rolls', 
            value = '\n'.join(['{}d{} x {} {}P: {}'.format(
                r['num_dice'], 
                r['die_type'], 
                r['multiplier'], 
                r['piece_type'][0].upper(), 
                cr[0]
            ) for r, cr in zip(rolls, coin_rolls)]),
            inline = False
        )
        await ctx.send(embed = embed)

    @commands.command()
    async def getHordeTreasure(self, ctx, target_cr):
        target_cr_int = int(target_cr)

        treasure_data = JSONDatabaseController().get_collection('loot').get_document('treasure hoard')
        cr_bracket = find_bracket_key(target_cr_int, treasure_data.keys())

        coin_rolls = treasure_data[cr_bracket]['coins']
        rolled_coins = [self.do_coin_roll(r) for r in coin_rolls]

        d100_roll = randint(1, 100)
        roll_bracket = find_bracket_key(
            d100_roll, 
            treasure_data[cr_bracket]['treasure'].keys()
        )
        items = treasure_data[cr_bracket]['treasure'][roll_bracket]
        valuable_roll = self.do_valuable_roll(items['valuable'])
        valuables = self.parse_valuable_roll(*valuable_roll)
        
        num_magic_item_rolls = [(
            self.do_roll(mi['num_dice'], mi['die_type']), 
            mi['magic_item_table']
        ) for mi in items['magic items']]
        print()
        magic_items = []
        for mir in num_magic_item_rolls:
            magic_items += self.process_magic_item_roll(*mir)
        print(magic_items)
        
        embed = discord.Embed(
            title = 'Rolling For Horde Treasure',
            colour = discord.Color.blue(),
            description = 'CR: {}'.format(cr_bracket)
        )
        embed.add_field(
            name = 'Coin Rolls',
            value = '\n'.join(['{}d{} x {} {}P: {}'.format(
                r['num_dice'], 
                r['die_type'], 
                r['multiplier'], 
                r['piece_type'][0].upper(), 
                cr[0]
            ) for r, cr in zip(coin_rolls, rolled_coins)]),
            inline = False
        )
        embed.add_field(
            name = 'D100 Roll',
            value = '{} - {}'.format(d100_roll, roll_bracket),
            inline = False
        )
        embed.add_field(
            name = 'Valuables ({} GP Each)'.format(valuable_roll[1]),
            value = '\n'.join([
                '{1} ({0})'.format(*vals) for vals in valuables
            ]),
            inline = False
        )
        if len(num_magic_item_rolls) != 0:
            embed.add_field(
                name = 'Magic Items',
                value = '\n'.join(magic_items),
                inline = False
            )
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Treasure(client))
