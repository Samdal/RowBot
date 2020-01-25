from discord.ext import commands
from discord import Embed


@commands.command()
async def help(ctx): # hjelpemeldingen
    embed = Embed(title="Commands", description="""
:small_blue_diamond: +gilf sends a sexy picture ( ͡° ͜ʖ ͡°) of (hopefully) Otto
:small_blue_diamond: +emphasise makes text ***l   o   n   g***
:small_blue_diamond: +mock makes the text lIKe THis

More useless shit coming soon...
""", color=0x1234d6)
    embed.set_footer(text="RowBoat by DRAVA, voiden, and Quesamo.")
    await ctx.send(embed=embed) # sender embed

def setup(bot):
    bot.add_command(help)