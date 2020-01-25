import os
import discord
from discord.ext import commands
import logging
import asyncio
# import json
# import time
import random

#logging.basicConfig(level=logging.INFO) #enables console logging

bot = commands.Bot(command_prefix='+')
bot.remove_command("help")

#automatically loads all .py files in the commands folder as extensions
for subdir, dirs, files in os.walk('commands'):
    for file in files:
        if str(file).endswith(".py"):
            extension_path = (str(subdir + os.sep + file)[:-3]).replace('\\', '.')
            bot.load_extension(extension_path)
            print(f'Extension {file[:-3]} loaded!')


@bot.event # Sier ifra når boten er online
async def on_ready():
    print("Online!")


# global check, ignorerer bots
@bot.check
async def ignore_bots(ctx):
    return not ctx.message.author.bot

@bot.command() # prints a random line from 'all star'
async def test(ctx):
    with open("allstar.txt") as allstar:
        await ctx.send(random.choice(allstar.read().splitlines()))


@bot.command()
async def reload(ctx, extension_name):
    for subdir, _, files in os.walk('commands'):
        for file in files:
            if str(file)[:-3] == extension_name:
                extension_path = (str(subdir + os.sep + file)[:-3]).replace('\\', '.')
                bot.reload_extension(extension_path)
                print(f'Extension {file[:-3]} reloaded!')
                return


with open("token.txt") as token: # leser tokenfilen og kjører boten
    bot.run(token.read())
