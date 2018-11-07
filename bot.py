import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Watching ROKA'))
    print('NastyCore') 


@client.event
async def on_message(message):
    if message.content == ':ping':
        await client.send_message(message.channel,'Pong!')
    if message.content == ':creator':
        await client.send_message(message.channel,'The creator of ``NastyCore`` is NastyAimed.')
    if message.content.startswith(':pingme'):
        await client.send_message(message.channel,'okay you need to die <@%s>'  %(message.author.id))
client.run('NDUxMTU3NDM3ODY5OTgxNzEw.DsR3Lw.7O3JLAfFkaUXFurMbkWig06noPI')
