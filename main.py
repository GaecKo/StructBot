from discord.ext import commands
from function import *
from keep_alive import keep_alive
from dotenv import load_dotenv
import asyncio, sys, os

load_dotenv()

# ------- HELP ------- #
class CustomHelpCommand(commands.HelpCommand):
	def __init__(self):
		super().__init__()
	async def send_bot_help(self, mapping):	
		await self.get_destination().send(help())

	async def send_cog_help(self, cog):	
		await self.get_destination().send(help())

	async def send_group_help(self, group):	
		await self.get_destination().send(help())

	async def send_command_help(self, command):	
		await self.get_destination().send(help())
	
bot = commands.Bot(command_prefix='$', help_command=CustomHelpCommand())
@bot.event
async def on_ready():
	global start
	start = datetime.now()
	print(f'{bot.user} has been logged in. Bot is running.')
	await start_event_check()

async def start_event_check():
	if check_activity():
		time, text, channel = get_list_event()
		for i in range(len(time)):
			await start_event_waiter(time[i], text[i], channel[i])
		
@bot.event
async def on_message(msg):
	if msg.author == bot.user:
		return
	elif "mohem" in msg.content.lower():
		await msg.channel.send(get_mohem())
	await bot.process_commands(msg)

# ------- WORKING TEST ------- #
@bot.command(name='test')
async def test(ctx):
	await ctx.send("Test working!")

# ------- MVP STATS ------- #
@bot.command(name='mvpstat', aliases=["mvp", "statmvp"])
async def mvp(ctx, *, msg):
	try:
		message = msg.split()
		pseudo = message[0]
		pos = message[1]
		if check_pseudo_in_data(pseudo):
			update_mvp(pseudo, pos)
			await ctx.send(f"mvp stat added for {pseudo}.\n ")
		else:
			update_kill_death_stats(0, 0, pseudo)
			update_mvp(pseudo, pos)
			await ctx.send(f"mvp stat added for {pseudo}. Had to create a new player\n ")
	except:
		await ctx.send("Wrong use of the command: \n $mvpstat `pseudo` `pos`\n ")
	
# ------- K/D STATS ------- #
@bot.command(name="kd", aliases=["kdstat"])
async def kill_death(ctx, *, msg):
	try:
		message = msg.split()
		pseudo = message[0]  
		kill = int(message[1])  
		death = int(message[2]) 
		if check_pseudo_in_data(pseudo):
			await ctx.send(f"Stat modified for {pseudo}")
		else:
			await ctx.send(f"Stat added for {pseudo}")
		update_kill_death_stats(kill, death, pseudo)	
	except:
		await ctx.send("Wrong use of the command: \n $kdstat `pseudo` `kills` `deaths`, kills and deaths must be numbers\n ")

# ------- ADD REMINDER ------- #
@bot.command(name='remind', aliases = ["addremind", "addreminder", "reminder"])
async def remind(ctx, *, msg):
	try:
		message = msg.split()
		dat = message[0]
		hour = message[1]
		text = ' '.join(message[2:])
		date = dat + " " + hour
		add_activity(date, text, ctx.channel.id)
		sort_reminder()
		await ctx.send(f"Event has been added successfully, it will be send on `{date.split()[0]} at {date.split()[1]}`.")
		await start_event_check()
		
	except:
		await ctx.send(f"Wrong use of the command: $remind `day/month/year` `hour:min` `text`")

async def start_event_waiter(time_str, text, channel):
	given = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
	channel = bot.get_channel(channel)
	now = datetime.now()
	if now > given:
		await channel.send(f"An event passed while the bot was offline: \nInitial Time: `{time_str}`, \n Text:\n >>> {text}")
		delete_event(text)
	else:
		wait_time = (given-now).total_seconds()
		await asyncio.sleep(wait_time)
		await channel.send(f"__REMINDER__:\n >>> {text}")
		delete_event(text)

# ------- GET STATS ------- #
@bot.command(name='stat', aliases=["getstat"])
async def stat(ctx, *, msg):
	try:
		message = msg.split()
		pseudo = message[0]
		await ctx.send(show_stats(pseudo))
	except:
		await ctx.send("Wrong use of the command: \n $stat `pseudo`\n ")

# ------- LEADERBOARD ------- #
@bot.command(name="top", aliases=["topboard", "board", "leaderboard"])
async def top(ctx):
	await ctx.send(top_board())

# ------- GIT ------- #
@bot.command(name="git", aliases=["github", "repository"])
async def git(ctx):
	await ctx.send(f"The git repo is available here: https://github.com/GaecKo/StructBot")

# ------- QUOTE CITING ------- #
@bot.command(name='quote', aliases=["quotes", "getquote", "getquotes"])
async def quote(ctx):
	await ctx.send("Here is a little quote :) \n\n" + "`" + get_quote() + "`")

# ------- DELETE USER ------- #
@bot.command(name="del", aliases=["delete", "deleteuser"])
async def del_pseudo(ctx, *, msg):
	try:
		message = msg.content.split()
		pseudo = message[1]
		if check_pseudo_in_data(pseudo):
			del_user(pseudo)
			await ctx.send(f"{pseudo} a été supprimé.")
		else:
			await ctx.send(f"Je n'ai aucune information sur {pseudo}, je ne peux donc rien supprimer.")
	except:
		await ctx.send("Wrong use of the command: \n $delete `pseudo`\n ")
	
# ------- CHANGE USERNAME ------- #
@bot.command(name='username', aliases=["changepseudo", "change", "modify"])
async def change_username(ctx, *, msg):
	try:
		old = msg.content.split()[0]
		new = msg.content.split()[1]
		if check_pseudo_in_data(old):
			change_username(old, new)
		else:
			await ctx.send(f"Aucune information sur {old}, êtes vous sûr que cet utilisateur existe?")
	except:
		await ctx.send("Wrong use of the command: \n $change `old` `new`\n ")

# ------- ADD QUOTE ------- #
@bot.command(name='addquote', aliases=["addquotes"])
async def quotes_add(ctx, *, msg):
	try:
		add_quote(msg)
		await ctx.send(f"{msg} \n-> Quote has been added to quotes")
	except:
		await ctx.send(f"Wrong use of the command: \n $addquote `quote`")

# ------- CONTACT ------- #
@bot.command(name="contact", aliases=["contacts", "discord"])
async def contact(ctx):
	await ctx.send("In case of trouble, don't hesitate to contact the creator: GaecKo#7545")

# ------- CONTACT ------- #
@bot.command(name="shutdown")
async def shutdown(ctx):
	maintain_reminder()
	end = datetime.now()
	diff = (end-start).total_seconds()
	await ctx.send(f"{bot.user} is shutting down...\nTotal run: {round(diff, 2)} seconds")

	sys.exit()

keep_alive()
bot.run(os.getenv("TOKEN")) 