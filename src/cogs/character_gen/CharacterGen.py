import discord
from discord.ext import commands, tasks
from itertools import cycle
import cogs.character_gen.CharacterStats as Stats
import traceback

class CharacterGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['generatecharacter', 'gc'])
    async def generateCharacter(self, ctx):
        try:
            value = Stats.CharacterStats().__repr__()
        except:
            Stats.log('ERROR: {}'.format(traceback.format_exc()))
            value = Stats.LOG_MSG
            Stats.LOG_MSG = ''
        await ctx.send(value)

def setup(client):
    client.add_cog(CharacterGen(client))