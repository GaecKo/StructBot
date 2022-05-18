import discord
import os
from function import *
from dotenv import load_dotenv
from threading import Thread

load_dotenv()
client = discord.Client()


@client.event
async def on_ready():
	global t
	t = Thread(target=maintain_check_reminder())
	
	print(f'{client.user} has been logged in. Bot is running.')


@client.event
async def on_message(msg):
	if msg.author == client.user:
		return
# ------- Vérificateur de fonctionnement ------- #
	elif msg.content.startswith('$test'):
		await msg.channel.send("Test working!")

	elif "mohem" in msg.content.lower():
		await msg.channel.send(get_mohem())

# ------- Ajout de stats MVP ------- #
	elif msg.content.startswith("$mvpstat") or msg.content.startswith("$mvp"):
		try:
			message = msg.content.split()
			pseudo = message[1]
			pos = message[2]
			if check_pseudo_in_data(pseudo):
				update_mvp(pseudo, pos)
				await msg.channel.send(f"mvp stat added for {pseudo}.\n ")
			else:
				update_kill_death_stats(0, 0, pseudo)
				update_mvp(pseudo, pos)
				await msg.channel.send(f"mvp stat added for {pseudo}. Had to create a new player\n ")
		except:
			await msg.channel.send("Wrong use of the command: \n $mvpstat `pseudo` `pos`\n ")
# ------- Help ------- #
	elif msg.content.startswith("$help"):
		await msg.channel.send(help())

# ------- Stats ------- #
	elif msg.content.startswith("$remind"):
		try:
			message = msg.content.split()
			dat = message[1]
			hour = message[2]
			text = message[3]
			add_activity(dat + " " + hour, text, msg.channel)
		except:
			await msg.channel.send(f"Wrong use of the command: $remind `day/month/year` `hour:min` `text`")

# ------- Stats ------- #
	elif msg.content.startswith("$stat"):
		try:
			message = msg.content.split()
			pseudo = message[1]
			await msg.channel.send(show_stats(pseudo))
		except:
			await msg.channel.send("Wrong use of the command: \n $stat `pseudo`\n ")

# ------- LEADERBOARD ------- #
	elif msg.content.startswith("$topboard") or msg.content.startswith("$top"):
		await msg.channel.send(top_board())

# ------- Git ------- #
	elif msg.content.startswith("$git"):
		await msg.channel.send(f"The git repo is available here: https://github.com/GaecKo/StructBot")

# ------- Envoyeur de citations ------- #
	elif msg.content.startswith('$quotes'):
		await msg.channel.send("Here is a little quote :) \n\n" + "`" + get_quote() + "`")

# ------- Ajout de stats kill/mort ------- #
	elif msg.content.startswith('$kdstat') or msg.content.startswith("$kd"):
		try:
			message = msg.content.split()
			pseudo = message[1]  
			kill = int(message[2])  
			death = int(message[3]) 
			if check_pseudo_in_data(pseudo):
				await msg.channel.send(f"Stat modified for {pseudo}")
			else:
				await msg.channel.send(f"Stat added for {pseudo}")
			update_kill_death_stats(kill, death, pseudo)	
		except:
			await msg.channel.send("Wrong use of the command: \n $kdstat `pseudo` `kills` `deaths`, kills and deaths must be numbers\n ")
	
# ------- Delete pseudo ------- #
	elif msg.content.startswith('$delete') or msg.content.startswith("$del"):
		try:
			message = msg.content.split()
			pseudo = message[1]
			if check_pseudo_in_data(pseudo):
				del_user(pseudo)
				await msg.channel.send(f"{pseudo} a été supprimé.")
			else:
				await msg.channel.send(f"Je n'ai aucune information sur {pseudo}, je ne peux donc rien supprimer.")
		except:
			await msg.channel.send("Wrong use of the command: \n $delete `pseudo`\n ")
	
# ------- Command not found ------- #
	elif msg.content.startswith('$contact'):
		await msg.channel.send("En cas de problème, merci de contacter GaecKo#7545 sur discord ou ")

# ------- Command not found ------- #
	elif msg.content.startswith('$'):
		await msg.channel.send(f"Command {msg.content} not known, type `$help` if needed.")
		
client.run(os.getenv("TOKEN")) 

