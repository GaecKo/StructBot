import discord
import os
from function import *
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(msg):
    if msg.author == client.user:
	    return 
    if msg.content.startswith('$test'):
        await msg.channel.send("Test working!")
    elif msg.content.startswith('$quotes'):
        await msg.channel.send(str("Here is a little quote :) \n\n" + "`" + get_quote() + "`"))
    elif msg.content.startswith('bite'):
        await msg.channel.send("tg frr")
    for i in ["salope", "pute", "connard", "salaud", "tg", "bot de merde", 'merde', 'enculé']:
        if i.lower() in msg.content.lower():
            await msg.channel.send(f"{i}, sérieusement {msg.author}? nan mais t'as quoi dans la tête? Ptite merde va")
	

client.run(os.environ['TOKEN'])
