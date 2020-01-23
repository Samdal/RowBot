
import discord
from discord.ext import commands
import logging
import asyncio
# import json
# import time
import random

logging.basicConfig(level=logging.INFO) #enables console logging

bot = commands.Bot(command_prefix='+')
bot.remove_command("help")


bot.load_extension('commands.emojify')


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

with open("token.txt") as token: # leser tokenfilen og kjører boten
    bot.run(token.read())
