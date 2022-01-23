import discord
from discord.ext import commands, tasks
from urllib import request, parse
import json
import asyncio
from database.JSONDatabaseController import JSONDatabaseController
from database.JSONCollection import JSONCollection

class Jukebox(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.players = {}

  @commands.command()
  async def ping2(self, ctx):
    print()
    guild = ctx.message.guild
    print(guild.id)
    if not ctx.message.author.voice:
      return await ctx.send('You must be in a voice channel to use this command')
    voice_channel = ctx.message.author.voice.channel
    print('{} : {}'.format(type(voice_channel), voice_channel))
    # print(help(voice_channel.connect))
    await voice_channel.connect()
    
    # try:
    #   await voice_channel.connect()
    #   # print(voice_client)
    # except asyncio.TimeoutError:
    #   print('Error: timeout')
    # except discord.ClientException:
    #   print('Error: Client')
    # except discord.opus.OpusError:
    #   print('Error: Opus')
    # except:
    #   print('Error: Unkown')
    await ctx.send('You are in\n\tGuild: {}\n\tVoice Channel: {}'.format(guild.id, voice_channel))

  @ping2.error
  async def ping2_error(self, ctx, err):
      print(err)
      await ctx.send('Sorry, something went wrong.')
      

def setup(client):
  client.add_cog(Jukebox(client))
