import discord
from discord.ext import commands, tasks
from database.JSONDatabaseController import JSONDatabaseController
from database.JSONCollection import JSONCollection

class General(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.db_controller = JSONDatabaseController()

    # events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        col = self.db_controller.get_collection('general')
        prefixes = col.get_document('server_prefix')
        col.update_document('server_prefix', {str(guild.id): prefixes['default']})

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        col = self.db_controller.get_collection('general')
        prefixes = col.get_document('server_prefix')
        prefixes.pop(str(guild.id))
        col.update_document('server_prefix', prefixes)

    # commands
    @commands.command(name='changeprefix')
    async def change_prefix(self, ctx, new_prefix):
        col = self.db_controller.get_collection('general')
        prefixes = col.get_document('server_prefix')
        col.update_document('server_prefix', {str(ctx.guild.id): new_prefix})

def setup(client):
    client.add_cog(General(client))