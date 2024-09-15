import time
from colorama import Fore, Back, Style, init
import os

init(autoreset=True)

# Define the categories
s = "DISCORD | MODERATION BOT"
j = "DISCORD | MUSIC BOT"
q = "DISCORD | GAME BOT"

# Intro
print(Fore.YELLOW + Style.BRIGHT + "HEY, THIS IS DISCOBY. IT WILL HELP YOU TO CODE DISCORD BOTS 10X FASTER")
time.sleep(2)
u = str(input(Style.DIM + "\033[4m               Your Nickname ? :\033[0m "))

time.sleep(2)
print(Style.BRIGHT + "HELLO " + u + "! WELCOME TO DISCOBY | LET'S GET STARTED")
time.sleep(3)
print("clear")
time.sleep(1)
def print_discoby():
    print("==========   ====    ====  ======   ====    ====   ======   ===   ===   ========")
    print("     ==      ====    ====  ==  ==   ====    ====   ==       == == ==       ==")
    print("     ==      == ==  == ==  ==   ==  == ==  == ==   =====    ==  ===        ==")
    print("     ==      ==  ==    ==  ==   ==  ==  ==    ==   ==       ==    ==       ==")
    print("     ==      ==        ==  ======   ==        ==   ======   ==    ==       ==")
    print("     ==      ==        ==  ==       ==        ==        ==  ==    ==       ==")
    print("     ==      ==        ==  ==       ==        ==   ======   ==    ==       ==")
    
print_discoby()

# Loading sequence
print("          ")
print(Fore.BLACK + Style.BRIGHT + "       WHAT TYPE OF BASE MODEL YOU WANT ? | HERE IS THE LIST")
time.sleep(3)
print(Fore.GREEN + "Loading==10%")
time.sleep(3)
print(Fore.GREEN + "Loading=====20%")
time.sleep(3)
print(Fore.GREEN + "Loading==========65%")
time.sleep(3)
print(Fore.GREEN + "Loading=============90%")
time.sleep(3)
print(Fore.GREEN + "Done================100%")
time.sleep(3)

# Display options
print(Fore.WHITE + Style.BRIGHT + "1. " + s)
time.sleep(3)
print(Style.BRIGHT + "2. " + j)
time.sleep(3)
print(Style.BRIGHT + "3. " + q)
time.sleep(3)

# Capture the user's selection
A = str(input("Choose a category (1/2/3): "))

# Function to create and write to a file
def create_file(bot_type, filename, content):
    try:
        # Create or open the file in write mode
        with open(filename, 'w') as file:
            file.write(content)
        # Get absolute path of the file
        file_path = os.path.abspath(filename)
        print(Fore.GREEN + f"File '{filename}' created successfully!")
        print(Fore.CYAN + f"File location: {file_path}")
    except Exception as e:
        print(Fore.RED + f"Error creating file: {e}")

# Function to edit a file
def edit_file(filename):
    try:
        # Open the file for reading and display current content
        with open(filename, 'r') as file:
            content = file.read()
        print(Fore.YELLOW + f"\nCurrent content of {filename}:\n")
        print(content)

        # Ask the user for changes
        print(Fore.CYAN + "\nNow, you can edit the content below. Type the new content (press Enter when done):\n")
        new_content = []
        while True:
            line = input()
            if line == "":  # Stop when the user presses Enter on an empty line
                break
            new_content.append(line)
        new_content = "\n".join(new_content)

        # Write the new content back to the file
        with open(filename, 'w') as file:
            file.write(new_content)

        print(Fore.GREEN + f"\nFile '{filename}' updated successfully!")
    except Exception as e:
        print(Fore.RED + f"Error editing file: {e}")

# Sample bot script template
moderation_bot_script = f"""
# Discord Moderation Bot Template

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

# Ban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {{member.mention}}")

# Kick command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {{member.mention}}")

# Unban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == member.split('#'):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {{user.mention}}")
            return

bot.run("YOUR_DISCORD_BOT_TOKEN")
"""

music_bot_script = f"""
# Discord Music Bot Template (Skeleton)

import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Music bot is ready!")

# Join voice channel command
@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {{channel}}")
    else:
        await ctx.send("You need to be in a voice channel for me to join!")

# Leave voice channel command
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Left the voice channel")
    else:
        await ctx.send("I am not in any voice channel!")

bot.run("YOUR_DISCORD_BOT_TOKEN")
"""

game_bot_script = f"""
# Discord Game Bot Template (Trivia Game)

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Game bot is ready!")

# Simple trivia command
@bot.command()
async def trivia(ctx):
    question = "What is the capital of France?"
    options = "1. Berlin\\n2. London\\n3. Paris\\n4. Madrid"
    correct_answer = 3
    await ctx.send(f"{{question}}\\n{{options}}")

    def check(m):
        return m.author == ctx.author and m.content.isdigit()

    try:
        msg = await bot.wait_for("message", check=check, timeout=15)
        if int(msg.content) == correct_answer:
            await ctx.send("Correct!")
        else:
            await ctx.send("Wrong! The correct answer is Paris.")
    except:
        await ctx.send("You took too long to answer!")

bot.run("YOUR_DISCORD_BOT_TOKEN")
"""

# Process the user's choice and create corresponding files
if A == '1':
    bot_type = "MODERATION BOT"
    filename = "Moderation_Bot.py"
    create_file(bot_type, filename, moderation_bot_script)

elif A == '2':
    bot_type = "MUSIC BOT"
    filename = "Music_Bot.py"
    create_file(bot_type, filename, music_bot_script)

elif A == '3':
    bot_type = "GAME BOT"
    filename = "Game_Bot.py"
    create_file(bot_type, filename, game_bot_script)

else:
    print(Fore.RED + "Invalid choice. Please restart and choose a valid option (1, 2, or 3).")

# Ask if the user wants to edit the file
edit_choice = str(input(Fore.CYAN + "Do you want to edit the file you created? (yes/no): ")).lower()

if edit_choice == 'yes':
    if A == '1':
        edit_file("Moderation_Bot.py")
    elif A == '2':
        edit_file("Music_Bot.py")
    elif A == '3':
        edit_file("Game_Bot.py")
