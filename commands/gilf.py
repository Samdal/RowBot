from discord.ext import commands
from discord import File
from os import listdir
from os.path import isfile, join
from random import choice


@commands.command()
async def gilf(ctx):
    files = [f for f in listdir("commands/gilf") if isfile(join("commands/gilf", f))]
    image = choice(files)
    await ctx.channel.send(file=File(f"./commands/gilf/{image}"))

def setup(bot):
    bot.add_command(gilf)
