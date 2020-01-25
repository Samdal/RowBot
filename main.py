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
# bot.remove_command("help")
# automatically loads all .py files in the commands folder as extensions
for subdir, dirs, files in os.walk('commands'):
    for file in files:
        if str(file).endswith(".py"):
            extension_path = (str(subdir + os.sep + file)[:-3]).replace('\\', '.')
            try:
                bot.load_extension(extension_path)
                print(f'Extension {file[:-3]} loaded!')
            except commands.ExtensionNotFound:
                print(f'Extension {file[:-3]} failed to load')




@bot.event # terminal message when bot is online
async def on_ready():
    print("Online!")
    with open("presence.txt", "r", encoding="utf-8") as obj: # opens presence.txt
        presence = obj.read()
    await bot.change_presence(activity=discord.Game(presence)) # sets presence on discord


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
@bot.command(help = "Crashes the bot. Admins only.")
async def crash(ctx):
    if is_dev(ctx.author.id):
        await ctx.send('Shutting down.')
        raise SystemExit
    else:
        await ctx.send('Only devs can use this command')


@bot.command(aliases = ["p"], help = "Changes the bot's presence.")
async def presence(ctx, *, message):
    if ctx.message.author.id in [313703847656816642, 209973852741042187, 226441515914756097]:
        with open("presence.txt", "w", encoding="utf-8") as presence: # opens presence text file
            presence.write(message) # replaces old text with new
        await bot.change_presence(activity=discord.Game(message)) # changes presence on discord



# prints a random line from 'all star'
@bot.command(aliases = ["t"], help = "Prints a random line from 'all star'")
async def test(ctx):
    with open("allstar.txt") as allstar:
        await ctx.send(random.choice(allstar.read().splitlines()))


# reloads the given extension
@bot.command(aliases = ["r"], help = "Reloads the specified command.")
async def reload(ctx, extension_name):
    for subdir, _, files in os.walk('commands'):
        for file in files:
            #print(file) #DEBUGGING
            if str(file)[:-3] == extension_name and str(file).endswith('.py'):
                extension_path = (str(subdir + os.sep + file)[:-3]).replace('\\', '.')
                bot.reload_extension(extension_path)
                await ctx.message.add_reaction("✅")
                print(f'Extension {file[:-3]} reloaded!')
                return
    print(f'No extension named {extension_name} found')
    await ctx.message.add_reaction("❌")
    return



with open("token.txt") as token: # reads the token file and runs the bot
    bot.run(token.read())
