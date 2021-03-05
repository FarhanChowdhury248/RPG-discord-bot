import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from cogs.index import *
from database.JSONDatabaseController import JSONDatabaseController

def get_prefix(client, message): 
    return JSONDatabaseController().get_collection('general').get_document('server_prefix')[str(message.guild.id)]

if __name__ == '__main__':
    load_dotenv(dotenv_path=os.path.join(os.path.dirname( __file__ ), '..', '.env'))

    client = commands.Bot(command_prefix=get_prefix)

    @client.command()
    async def load(ctx, extension):
        client.load_extension('cogs.{}.{}'.format(extension.lower(), extension.capitalize()))

    @client.command()
    async def unload(ctx, extension):
        client.unload_extension('cogs.{}.{}'.format(extension.lower(), extension.capitalize()))

    @client.command()
    async def reload(ctx, extension):
        client.unload_extension('cogs.{}.{}'.format(extension.lower(), extension.capitalize()))
        client.load_extension('cogs.{}.{}'.format(extension.lower(), extension.capitalize()))

    load_extensions(client, 'cogs')

    client.run(os.getenv('TOKEN'))