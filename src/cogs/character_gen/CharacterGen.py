import discord
from discord.ext import commands, tasks
from itertools import cycle
from cogs.character_gen.models.CharacterStats import *

class CharacterGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['generatecharacter', 'gc'])
    async def generateCharacter(self, ctx):
        await ctx.send(CharacterStats().__repr__())

def setup(client):
    client.add_cog(CharacterGen(client))