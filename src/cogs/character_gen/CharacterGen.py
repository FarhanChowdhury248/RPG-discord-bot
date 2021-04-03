import discord
from discord.ext import commands, tasks
from itertools import cycle
import cogs.character_gen.CharacterStats as Stats
import traceback

class CharacterGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['generatecharacter', 'gc'])
    async def generateCharacter(self, ctx):
        try:
            await ctx.send(embed=self.get_embed(Stats.CharacterStats()))
            print(Stats.LOG_MSG)
            Stats.LOG_MSG = ''
        except:
            Stats.log('ERROR: {}'.format(traceback.format_exc()))
            values = Stats.LOG_MSG.split('ERROR:')
            Stats.LOG_MSG = ''
            await ctx.send(embed = self.get_error_embed(values[0], values[1]))

    def get_error_embed(self, log_info, error_info):
        embed = discord.Embed(
            title='Error',
            description='An error occurred. Please report this to our GitHub.',
            colour=discord.Color.red(),
            type='rich'
        )
        embed.add_field(
            name='Log Info',
            value=log_info.strip(),
            inline=False
        )
        embed.add_field(
            name='Error Info',
            value=error_info.strip(),
            inline=False
        )
        return embed

    def get_embed(self, character):
        def getModifier_value(val):
            if val < 0:
                return str(val)
            return '+{}'.format(val)

        embed = discord.Embed(
            title='Character Name',
            description='This was a randomly generated character',
            colour=discord.Color.blue(),
            type='rich'
        )
        
        embed.set_footer(text='Notice a problem? Report to our GitHub!')
        embed.set_author(name='D&D Support Bot', icon_url='https://i.imgur.com/IiFhDDP.jpg')

        embed.add_field(name='Alignment', value=character.alignment.capitalize(), inline=True)
        embed.add_field(name='Race', value=character.race.capitalize(), inline=True)
        embed.add_field(name='Class', value=character._class.capitalize(), inline=True)

        embed.add_field(name='AC', value=character.ac, inline=True)
        embed.add_field(name='Initiative', value=getModifier_value(character.get_modifier('dex')), inline=True)
        embed.add_field(name='Speed', value=character.speed, inline=True)

        embed.add_field(name='Proficiency Bonus', value=getModifier_value(character.proficiency_bonus), inline=True)
        embed.add_field(name='Size', value=character.size, inline=True)
        embed.add_field(name='Saving Throws', value=', '.join(character.saving_throws).upper(), inline=True)

        embed.add_field(name='Hit points', value=character.hit_points, inline=True)
        embed.add_field(name='Hit Die', value='d{}'.format(character.hit_die), inline=True)
        embed.add_field(name='Passive Perception', value=character.passive_perception, inline=True)

        ability_scores_value = '\n'.join(
            ['{} - {} ({})'.format(
                key.upper(),
                character.ability_scores[key],
                getModifier_value(character.get_modifier(key))
            ) for key in character.ability_scores]
        )
        embed.add_field(name='Ability Scores', value=ability_scores_value, inline=True)

        languages_value = '\n'.join(character.languages)
        embed.add_field(name='Languages', value=languages_value, inline=True)
        
        traits_value = '\n'.join([str(t) for t in character.traits])
        embed.add_field(name='Traits', value=traits_value, inline=True)

        if len(character.known_spells) != 0:
            known_spells_value = '\n'.join(character.known_spells)
        else:
            known_spells_value = 'None'
        embed.add_field(name='Spells Known', value=known_spells_value, inline=True)

        if len(character.prepared_spells) != 0:
            spells_prepared_value = '\n'.join(character.prepared_spells)
        else:
            spells_prepared_value = 'None'
        embed.add_field(name='Spells Prepared', value=spells_prepared_value, inline=True)

        embed.add_field(name='Spellcasting Ability', value=character.spellcasting_ability, inline=True)

        spell_slots_value = '\n'.join(
            ['Level {}: {}'.format(
                level, 
                character.spell_slots[level]
            ) for level in character.spell_slots if character.spell_slots[level] != 0]
        )
        if spell_slots_value == '':
            spell_slots_value = 'None'
        embed.add_field(name='Spell Slots', value=spell_slots_value, inline=True)

        proficiencies_value = '\n'.join(character.proficiencies)
        embed.add_field(name='Proficiencies', value=proficiencies_value, inline=True)

        return embed

def setup(client):
    client.add_cog(CharacterGen(client))