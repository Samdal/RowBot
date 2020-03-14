from discord.ext import commands

class rename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Lets a moderator rename the given user, regardless of their role")
    async def rename(self, ctx, mention, *, new_name):
        member = ctx.message.mentions[0]
        if new_name != '':
            await member.edit(nick=new_name)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(rename(bot))