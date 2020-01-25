from discord.ext import commands


#outputs the given input, but e   m   p   h   a   s   i   s   e   d 
@commands.command()
async def emphasise(ctx, content):
    output = ''
    for character in content:
        output += character + '   '
    
    await ctx.send(f"***{output[:-3]}***")
    await ctx.message.delete()

def setup(bot):
    bot.add_command(emphasise)