import discord
import os
from function import *
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has been logged in. Bot is running.')

@client.event
async def on_message(msg):
    if msg.author == client.user:
	    return 
# ------- Vérificateur de fonctionnement ------- #
    if msg.content.startswith('$test'):
        await msg.channel.send("Test working!")

# ------- Envoyeur de citations ------- #
    elif msg.content.startswith('$quotes'):
        await msg.channel.send(str("Here is a little quote :) \n\n" + "`" + get_quote() + "`"))

# ------- Ajout de stats kill/mort ------- #
    elif msg.content.startswith('$kdstat'):
        # try
        message = msg.content.split()
        pseudo = message[1]  
        kill = message[2]  
        death = message[3] 
        if not check_pseudo_for_stat(pseudo):
            add_kill_death_stats(kill, death, pseudo)
            await msg.channel.send(f"Stat added for {pseudo}.")
        else:
            change_kill_death_stats(kill, death, pseudo)
            await msg.channel.send(f"Stat modified for {pseudo}.")
        #except
            #await msg.channel.send("Wrong use of the command: \n $kdstat `pseudo` `kills` `deaths`\n ")
        
# ------- Vérificateur de langages ------- #
    for i in ["salope", "pute", "connard", "salaud", "tg", "bot de merde", 'merde', 'enculé']:
        if i.lower() in msg.content.lower():
            await msg.channel.send(f"{i}, sérieusement {msg.author}? nan mais t'as quoi dans la tête? Ptite merde va")
    
	

client.run(os.environ['TOKEN'])
