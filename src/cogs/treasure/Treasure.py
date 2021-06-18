import discord
from discord.ext import commands, tasks
from urllib import request, parse
import json
from database.JSONDatabaseController import JSONDatabaseController
from database.JSONCollection import JSONCollection
from random import randint

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

    def do_roll(self, roll):
        roll_value = 0
        for i in range(int(roll['num_dice'])):
            roll_value += randint(1, int(roll['die_type']))
        return roll_value * int(roll['multiplier']), roll['piece_type']

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
            coin_rolls.append(self.do_roll(r))

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

def setup(client):
    client.add_cog(Treasure(client))
