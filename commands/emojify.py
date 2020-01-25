from discord.ext import commands


# Deler opp et bilde til emojier og legger dem inn på serveren
@commands.command(hidden = True)
async def emojify(ctx):
    pass

def setup(bot):
    bot.add_command(emojify)