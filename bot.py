from datetime import date, datetime
import os
import datetime 
import discord
import json
from discord.ext import commands

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix= get_prefix)
#Remove default HELP command
bot.remove_command('help')

@bot.event
async def on_ready():
    #Wake up message
    cur_time = datetime.datetime.now().strftime("%#I:%M %p")
    guild_ammount = len(bot.guilds)

    if datetime.datetime.now().hour < 10:
        print(f"Good Morning! It is currently {cur_time}, and I'm currently connected to {guild_ammount} servers!")
    elif datetime.datetime.now().hour < 17:
        print(f"Good Afternoon! It is currently {cur_time}, and I'm currently connected to {guild_ammount} servers!")
    elif datetime.datetime.now().hour < 24:
        print(f"Good Evening! It is currently {cur_time}, and I'm currently connected to {guild_ammount} servers!")  

    #Bot status
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="out for Ruka!"))

@bot.event
async def on_guild_join(guild):
    #Adds prefix on guild join
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '>'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    #Removes prefix on guild leave
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

#Simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')        

#Prefix setting command
@bot.command()
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print(f"Loaded {filename} cog!")
        bot.load_extension(f'cogs.{filename[:-3]}')



#Reads token and runs bot
with open('token.txt') as f:
    token = f.read()

bot.run(token)