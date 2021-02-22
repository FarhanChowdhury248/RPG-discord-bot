'''
This is an example cog. Use it to figure out how to create and set up cogs.
The compulsory components of a cog are defined here with comments.
Also make sure to add it to the load_extensions function in the src/cogs/index.py 
file.
'''

import discord
from discord.ext import commands

class Example(commands.Cog):
    '''
    The Cog class must inherit from commands.Cog and take one argument upon
    initialization.
    '''
    def __init__(self, client):
        self.client = client

def setup(client):
    '''
    A global setup function must be declared for all cogs in the main cog file.
    The function must take 1 argument (the bot) and add an instance of the cog
    to the bot.
    '''
    client.add_cog(Example(client))