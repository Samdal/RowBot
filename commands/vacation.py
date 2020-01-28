from discord.ext import commands
import datetime

@commands.command(description="Prints the amount of days until the next school break")
async def vacation(ctx):
    time_difference = datetime.datetime(2020, 2, 22) - datetime.datetime.now()
    await ctx.send(f'Days until winter break: {time_difference.days}')

def setup(bot):
    bot.add_command(vacation)