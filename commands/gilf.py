from discord.ext import commands
from discord import File
from os import listdir
from os.path import isfile, join
from random import choice


@commands.command()
async def gilf(ctx):
    files = [f for f in listdir("commands/gilf/images") if isfile(join("commands/gilf/images", f))] 
    # ^lists all files in the gilf folder.
    image = choice(files) # picks a random image from the list
    await ctx.channel.send(file=File(f"./commands/gilf/images/{image}"))

def setup(bot):
    bot.add_command(gilf)
