'''
This is an example cog. Use it to figure out how to create and set up cogs.
The compulsory components of a cog are defined here with comments.
Also make sure to add it to the load_extensions function in the src/cogs/index.py 
file.
'''

import discord
from discord.ext import commands, tasks
from itertools import cycle

STATUSES = cycle(['status 1', 'status 2', 'status 3'])

class Example(commands.Cog):
    '''
    The Cog class must inherit from commands.Cog and take one argument upon
    initialization.
    '''
    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Dungeons & Dragons'))
        # self.change_status.start() # start task
        print('We have logged in as {}'.format(self.client.user))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        '''
        This is an example handler for handling errors generically.
        '''
        if isinstance(err, commands.MissingRequiredArgument):
            await ctx.send('Required arguments are missing')

    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! {}ms'.format(round(self.client.latency * 1000)))

    @commands.command(aliases=['logout'])
    async def kill(self, ctx):
        await self.client.logout()

    @commands.command()
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, err):
        '''
        This handler will only get run for clear command errors.
        '''
        if isinstance(err, commands.MissingRequiredArgument):
            await ctx.send('Required arguments are missing for the clear command.')

    # tasks (note that all tasks must be started)
    @tasks.loop(seconds=10)
    async def change_status(self):
        print('hello')
        await self.client.change_presence(activity=discord.Game(next(STATUSES)))

def setup(client):
    '''
    A global setup function must be declared for all cogs in the main cog file.
    The function must take 1 argument (the bot) and add an instance of the cog
    to the bot.
    '''
    client.add_cog(Example(client))