
# RowBot

We're a group of friends trying to make a discord bot together. We don't expect anyone to use this, but if you want to, it should be pretty easy to get started. You need a minimal knowledge of python, though.

If you would like to use the bot, visit [this link](https://discordapp.com/oauth2/authorize?client_id=669896811632263168&permissions=8&scope=bot) to add it to your server.

## How to install and setup your own instance
You need [python 3](https://www.python.org/downloads/ "Download here") for this program to work properly. 

If you don't have a bot allready, go to the [Discord developer portal](http://discord.com/developers/applications/) and make a new application with a bot user. 

### Terminal way
1. `git clone https://github.com/Samdal/RowBot`
2. `cd RowBot`
3. `pip install $(cat dependencies.txt)`
4. `echo -n "YOUR_TOKEN_HERE" > token.txt`
5. `python3 main.py`
> Step 3 and 3 require an UNIX based system, if you are installing it on Windows, do step 2 and 4 of the GUI way

### GUI way
1. Download the zip file from the "⤓Code" in the top right corner of github, extract the zip file on your pc and enter the directeroy of the folder
2. Install the contents of `dependencies.txt` with `pip install <package>`
3. Make a file called `token.txt` in the same directory as ``main.py``, and paste your own bot token into that file
4. Run `main.py` to start the program
5. "enjoy"
