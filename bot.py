import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix = '-')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are.")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
	await bot.change_presence(game=discord.Game(name="YOUR GAME"))

bot.run("NTE1OTcyMjg4NzY4NjM4OTc5.Dtwg6A.4Leor8E6t3wMOIL9f7mBiWKA8qE")
