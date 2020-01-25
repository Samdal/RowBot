import os
import discord
from discord.ext import commands
import logging
import asyncio
# import json
# import time
import random

# logging.basicConfig(level=logging.INFO) #enables console logging

bot = commands.Bot(command_prefix='+')
bot.remove_command("help")
# automatically loads all .py files in the commands folder as extensions
for subdir, dirs, files in os.walk('commands'):
    for file in files:
        if str(file).endswith(".py"):
            extension_path = (str(subdir + os.sep + file)[:-3]).replace('\\', '.')
            bot.load_extension(extension_path)
            print(f'Extension {file[:-3]} loaded!')


@bot.event # terminal message when bot is online
async def on_ready():
    print("Online!")

# global check, ignores bots
@bot.check
async def ignore_bots(ctx):
    return not ctx.message.author.bot



#HANDY FUNCTIONS

# determines if the given user is a dev
def is_dev(user_id):
    return any(user_id == dev_id for dev_id in [209973852741042187, 313703847656816642, 226441515914756097])


#COMMANDS

# shuts down the bot. should be automatically rebooted through a bat file
@bot.command()
async def crash(ctx):
    if is_dev(ctx.author.id):
        await ctx.send('Shutting down.')
        raise SystemExit
    else:
        await ctx.send('Only devs can use this command')

# prints a random line from 'all star'
@bot.command()
async def test(ctx):
    with open("allstar.txt") as allstar:
        await ctx.send(random.choice(allstar.read().splitlines()))


# reloads the given extension
@bot.command()
async def reload(ctx, extension_name):
    for subdir, _, files in os.walk('commands'):
        for file in files:
            if str(file)[:-3] == extension_name:
                extension_path = (str(subdir + os.sep + file)[:-3]).replace('\\', '.')
                
                bot.reload_extension(extension_path)
                
                await ctx.message.add_reaction("✅")
                print(f'Extension {file[:-3]} reloaded!')
                return
                
        print(f'No extension named {extension_name} found')
        return





with open("token.txt") as token: # leser tokenfilen og kjører boten
    bot.run(token.read())
