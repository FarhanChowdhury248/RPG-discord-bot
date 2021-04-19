import discord
from discord.ext import commands, tasks
from urllib import request, parse
import json

API_ROOT = 'https://www.dnd5eapi.co/api/'

def query_api(suffix):
    with request.urlopen(API_ROOT + suffix) as res:
        html = res.read().decode('utf-8')
        return json.loads(html)

class Search(commands.Cog):
    def __init__(self, client):
        self.client = client

    def get_all_conditions(self):
        return [element['index'] for element in query_api('conditions')['results']]

    @commands.command(name='allConditions')
    async def all_conditions(self, ctx):
        all_cs = self.get_all_conditions()
        desc = ''
        for c in all_cs:
            desc += '- {}\n'.format(c)
        embed = discord.Embed(
            title = 'Conditions',
            description = desc,
            colour = discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def condition(self, ctx, condition):
        all_conditions = self.get_all_conditions()
        parsed_condition = condition.lower()
        if parsed_condition not in all_conditions:
            embed = discord.Embed(
                title = 'Error',
                description = 'That is not a valid condition.',
                colour = discord.Color.red()
            )
            await ctx.send(embed=embed)
            return
        data = query_api('conditions/{}'.format(parsed_condition))
        condition_desc = ''
        for point in data['desc']:
            condition_desc += '{}\n'.format(point)
        embed = discord.Embed(
            title = 'Condition: {}'.format(parsed_condition.capitalize()),
            description = condition_desc,
            colour = discord.Color.blue()
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Search(client))