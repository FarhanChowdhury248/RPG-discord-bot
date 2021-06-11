
def load_extensions(client, pre):
    # this is an example line to display how to add a cog to the bot
    client.load_extension('{}.example.Example'.format(pre))
    client.load_extension('{}.general.General'.format(pre))
    client.load_extension('{}.character_gen.CharacterGen'.format(pre))
    client.load_extension('{}.roll.Roll'.format(pre))
    client.load_extension('{}.search.Search'.format(pre))
    client.load_extension('{}.treasure.Treasure'.format(pre))