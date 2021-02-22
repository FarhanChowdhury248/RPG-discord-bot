import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from cogs.index import *

if __name__ == '__main__':
    load_dotenv(dotenv_path='../.env')

    client = commands.Bot(command_prefix='.')

    @client.command()
    async def load(ctx, extension):
        client.load_extension('cogs.{}.{}'.format(extension.lower(), extension.capitalize()))

    @client.command()
    async def unload(ctx, extension):
        client.unload_extension('cogs.{}.{}'.format(extension.lower(), extension.capitalize()))

    @client.command()
    async def reload(ctx, extension):
        client.load_extension('cogs.{}.{}'.format(extension.lower(), extension.capitalize()))
        client.unload_extension('cogs.{}.{}'.format(extension.lower(), extension.capitalize()))

    load_extensions(client, 'cogs')

    client.run(os.getenv('TOKEN'))