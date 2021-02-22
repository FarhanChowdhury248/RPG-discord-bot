import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from cogs.index import *

if __name__ == '__main__':
    load_dotenv(dotenv_path='../.env')

    client = commands.Bot(command_prefix='.')

    @client.event
    async def on_ready():
        print('We have logged in as {}'.format(client.user))

    @client.command()
    async def ping(ctx):
        await ctx.send('Pong! {}ms'.format(round(client.latency * 1000)))

    @client.command(aliases=['logout'])
    async def kill(ctx):
        await client.logout()

    @client.command()
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @client.command()
    async def load(ctx, extension):
        await client.load_extension('cogs.{}'.format(extension))

    @client.command()
    async def unload(ctx, extension):
        await client.unload_extension('cogs.{}'.format(extension))

    load_extensions(client, 'cogs')

    client.run(os.getenv('TOKEN'))