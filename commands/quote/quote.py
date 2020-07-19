from discord.ext import commands
import json
import os
import random

class quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Saves the last message sent in the channel, or another message from its ID", aliases=["q"])
    async def quote(self, ctx, target_message=''): #add support for pinning from message IDs
        
        quotes_file_path = ('commands\\quote\\quotes.json' if os.name == 'nt' else 'commands/quote/quotes.json') #changes the path format based on the OS
        
        try:
            if target_message == '': #if no message ID is given
                #gets the last message sent in the channel
                counter = 0
                for message in await ctx.channel.history(limit=2).flatten(): #.history also gets the message used to trigger the command
                    if counter > 0:
                        quote = message
                    counter += 1
            else:
                quote = await ctx.channel.fetch_message(int(target_message))
        except:
            await ctx.send("Not a valid message ID")
            print("\n!!!Could not find message ID, ignore below traceback!!!\n\n")
                    
        #opens the json file, parses and stores the contents in a var, modifies it, and dumps it back
        with open(quotes_file_path, 'r+') as quotes_file:
            quotes = json.loads(quotes_file.read())
            quotes['quotes'].append({str(quote.author.id):quote.content})
        with open(quotes_file_path, 'w+') as quotes_file:
            json.dump(quotes, quotes_file)

        await ctx.send("Quote saved!")



    @commands.command(description="Sends a random saved message. Include a user ping to send a random saved message from that person", aliases=["rq"])
    async def randomquote(self, ctx, *, user=''):
        
        quotes_file_path = ('commands\\quote\\quotes.json' if os.name == 'nt' else 'commands/quote/quotes.json')
        
        with open(quotes_file_path, 'r+') as quotes_file:
            quotes = json.loads(quotes_file.read())
            
            if user == '': #if no user is given
                output_quote = random.choice(quotes['quotes'])
            else: #if a user is given
                user_quotes = []
                for quote in quotes['quotes']:
                    '''
                    each quote is a dict with the author id as the key and the text as the value
                    'user' is the user mention as str
                    it must be sliced to not display the <@!> around the id itself
                    '''
                    quote_author = str(list(quote.keys())[0])
                    if quote_author == user[3:-1]:
                        user_quotes.append(quote)
                output_quote = random.choice(user_quotes)


        output_quote_author_id = list(output_quote.keys())[0] #note that this is a str
        output_quote_text = list(output_quote.values())[0]

        #so it doesn't ping the author every time the quote is displayed
        output_quote_author = self.bot.get_user(int(output_quote_author_id))

        await ctx.send(f'*"{output_quote_text}"\n     -{output_quote_author.name}*')
            



def setup(bot):
    bot.add_cog(quote(bot))