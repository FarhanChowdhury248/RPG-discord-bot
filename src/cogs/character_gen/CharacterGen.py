import discord
from discord.ext import commands, tasks
from itertools import cycle

class CharacterGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['generatecharacter', 'gc'])
    async def generateCharacter(self, ctx):
        await ctx.send('Character generated!')

def setup(client):
    client.add_cog(CharacterGen(client))