from discord.ext import commands
from random import choice

# when you use this command the tEXT turNs INto THIS
@commands.command()
async def mock(ctx, *, content):
    output = []

    for letter in content: # 50/50 percent chance of letter being upper/lowercase
        seq = [letter.upper(), letter.lower()]
        output.append(choice(seq))
    
    if await ctx.send("".join(output)): # deletes the original message if the output is sent successfully
        await ctx.message.delete()

def setup(bot):
    bot.add_command(mock)