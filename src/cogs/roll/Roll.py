import discord
from discord.ext import commands, tasks
import random

class Roll(commands.Cog):
    def __init__(self, client):
        self.client = client

    def roll_parser(self, roll_msg):
        num_dice = ''
        die_type = ''
        mod = ''
        i = -1
        len_msg = len(roll_msg)
        while i < len_msg - 1:
            i += 1
            if roll_msg[i] == 'd':
                break
            num_dice += roll_msg[i]
        while i < len_msg - 1:
            i += 1
            if roll_msg[i] in ['+', '-']:
                mod += roll_msg[i]
                break
            die_type += roll_msg[i]
        while i < len_msg - 1:
            i += 1
            mod += roll_msg[i]
        if num_dice == '':
            num_dice = 1
        num_dice = int(num_dice)
        die_type = int(die_type)
        if mod == '':
            mod = 0
        else:
            mod = int(mod)
        return num_dice, die_type, mod

    def get_roll_embed(self, roll_msg):
        try:
            num_dice, die_type, mod = self.roll_parser(roll_msg)
            result = mod
            rolls = []
            for i in range(num_dice):
                rolls.append(random.randint(1, die_type))
                result += rolls[-1]
            desc = '{}: {} '.format(roll_msg, rolls)
            if mod < 0:
                desc += '- {} '.format(abs(mod))
            elif mod > 0:
                desc += '+ {} '.format(mod)
            desc += '= {}'.format(result)
            return discord.Embed(
                title='Rolling...',
                description=desc,
                colour=discord.Color.blue()
            )
        except:
            return discord.Embed(
                title='Error',
                description='Roll description must be in the form:\n[int]d[int][+|-][int]',
                colour=discord.Color.red()
            )

    @commands.command(aliases=['r'])
    async def roll(self, ctx, arg):
        await ctx.send(embed=self.get_roll_embed(arg))

    @commands.command(name='secretroll', aliases=['sr'])
    async def secret_roll(self, ctx, arg):
        await ctx.author.send(embed=self.get_roll_embed(arg))

def setup(client):
    client.add_cog(Roll(client))