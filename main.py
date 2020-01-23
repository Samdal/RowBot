
import discord
from discord.ext import commands
import logging
import asyncio
# import json
# import time
import random

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='*')
bot.remove_command("help")

@bot.event # Sier ifra når boten er online
async def on_ready():
    print("Online!")


# global check, ignorerer bots
@bot.check
async def ignore_bots(ctx):
    return not ctx.message.author.bot


@bot.command() # Deler opp et bilde til emojier og legger dem inn på serveren
async def emojify(ctx):

@bot.command() # all star limago
async def test(ctx):
    with open("allstar.txt") as allstar:
        await ctx.send(random.choice(allstar.read().splitlines()))

with open("token.txt") as token: # leser tokenfilen og kjører boten
    bot.run(token.read())
