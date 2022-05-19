from random import randint
import json
from threading import Thread
from datetime import date, time, datetime 
import time

def test_channel(channel):
    data = {"channel": channel}
    write_reminder(data)
    data = access_reminder()
    return data["channel"]
        
def access_reminder():
    with open("assets/reminder.json", 'r') as f:
        return json.load(f)

def write_reminder(data):
    with open("assets/reminder.json", 'w') as f:
        json.dump(data, f, indent=4)

def access_data():
    with open("assets/data.json", 'r') as f:
        return json.load(f)

def write_data(data):
    with open("assets/data.json", 'w') as f:
        json.dump(data, f, indent=4)

def add_quote(quote):
    with open("assets/quotes.txt", "a") as f:
        f.write(f"\n{quote}")

def check_activity():
    data = access_reminder()
    if data == {}:
        return False
    return True

def delete_event(text):
    data = access_reminder()
    for key, info in data.items():
        if info["text"] == text:
            del data[key]
            write_reminder(data)
            return

def get_list_event():
    data = access_reminder()
    time, text, channel = [], [], []
    for key, info in data.items():
        if info["in_memory"] == True:
            continue
        time.append(key)
        text.append(info["text"])
        channel.append(info["channel"])
        data[key]["in_memory"] = True
    write_reminder(data)
    return time, text, channel

def add_activity(date, text, channel):
    data = access_reminder()
    if len(date.split()[0].split("/")[2]) == 4:
        rem = datetime.strptime(date, "%d/%m/%Y %H:%M")
    else:
        rem = datetime.strptime(date, "%d/%m/%y %H:%M")
    data[str(rem)] = {"text": text, "channel": channel, "in_memory": False}
    write_reminder(data)

def maintain_reminder():
    data = access_reminder()
    for key, value in data.items():
        value["in_memory"] = False
    write_reminder(data)  

def get_mohem():
    base = "mohem"
    for i in range(randint(0, 100)):
        base += "m"

    if randint(1, 2) == 1:
        base += " frère"
    
    return base

def get_quote():
	with open("assets/quotes.txt", encoding="utf-8") as f:
		return f.readlines()[randint(0, 29)]

def top_board():
    data = access_data()
    kills = []
    kill_death = []
    death = []
    points = []
    for pseudo, values in data.items():
        kills.append([pseudo, values["kill"]])
        if values["death"] == 0:
            kill_death.append([pseudo, values["kill"]])
        else:
            kill_death.append([pseudo, values["kill"] / values["death"]])
        death.append([pseudo, values["death"]])
        points.append([pseudo, get_points(pseudo)])

    for i in range(len(kills)):
        kills.sort(key=lambda x: x[1], reverse=True)
        kill_death.sort(key=lambda x: x[1], reverse=True)
        death.sort(key=lambda x: x[1], reverse=True)
        points.sort(key=lambda x: x[1], reverse=True)

    top_board_text = "**__BEST K/D__ :bar_chart: ** :\n"
    for i in range(len(kill_death)):
        top_board_text += f"\t | {i+1}) *{kill_death[i][0]}*: {kill_death[i][1]} of k/d ratio \n"

    top_board_text += "\n\n**__MOST MVP POINTS__ :video_game: ** :\n"
    for i in range(len(points)):
        top_board_text += f"\t | {i+1}) *{points[i][0]}*: {points[i][1]} mvp points \n"
    
    top_board_text += "\n\n**__MOST KILLS__ :chart_with_upwards_trend: ** :\n"
    for i in range(len(kills)):
        top_board_text += f"\t | {i+1}) *{kills[i][0]}*: {kills[i][1]} kills \n"
    
    top_board_text += "\n\n**__MOST DEATHS__ :skull_crossbones: ** :\n"
    for i in range(len(death)):
        top_board_text += f"\t | {i+1}) *{death[i][0]}*: {death[i][1]} death \n"
    
    return top_board_text

def update_mvp(pseudo, pos):
    data = access_data()
    if pos in data[pseudo]:
        data[pseudo][pos] += 1
    else:
        data[pseudo][pos] = 1
    write_data(data)

def get_points(pseudo):
    data = access_data()
    player_info = data[pseudo]
    points = 0
    for key, value in data[pseudo].items():
        try:
            key = int(key)
            points += value / key
        except:
            continue
    return round(points, 2) 

def update_kill_death_stats(kill, death, pseudo):
    data = access_data()
    if pseudo in data:
        data[pseudo]["kill"] += kill
        data[pseudo]["death"] += death
    elif pseudo not in data:
        data[pseudo] = {
            "kill" : int(kill),
            "death": int(death),
        }
    write_data(data)

def check_pseudo_in_data(pseudo):
    data = access_data()
    if pseudo in data:
        return True
    return False

def show_stats(pseudo):
    data = access_data()
    if pseudo in data:
        if data[pseudo]["death"] != 0:
            k_d = data[pseudo]["kill"] / data[pseudo]["death"]
        else:
            k_d = data[pseudo]["kill"]
        return f"Le joueurs **{pseudo}** a __{data[pseudo]['kill']} kills__ et  __{data[pseudo]['death']} morts__. Son k/d est de {k_d} et ses points mvp sont {get_points(pseudo)}"
    return f"Je n'ai aucune donnée sur {pseudo}. Utilisez $kdstat `kill` `death` `pseudo` pour en ajouter."

def del_user(pseudo):
    data = access_data()
    del data[pseudo]
    write_data(data)
    
def help():
    return """
__Here are some command you can use:__

1) __Easy Start-up__:
    
    **$test** ⇒ *Check if the bot is running*

    **$help** ⇒ *Send you help*
    
2) __Stats__:

    **$kdstat / $kd `pseudo` `kills` `deaths`** ⇒ *Update K/D of a player, kills and deaths must be numbers*
    
    **$mvpstat / $mvp `pseudo` `position`** ⇒ *Position must be a number, then add position info of a player*

    **$stat `pseudo`** ⇒ *Shows the stat of a player*

    **$topboard / $top** ⇒ *Shows the general top board with the known stats*
    
3) __Reminder__:

    **$remind  `day/month/year` `hour:min` `text to send`** ⇒ *Add a reminder at that date, it will send the given text*

4) __User Management__:

    **$delete / $del `pseudo`** ⇒ *Deletes all data about a player*

    **$username `old` `new`** ⇒ *Change the old username by the new one in the data* 
    
5) __Quotes__:

    **$quotes** ⇒ *Send a gaming quote*
    
    **$addquote `quote`** ⇒ *Add the quote in the quotes list*

6) __Others__:

    **$git** ⇒ *Send the git repository of this bot*
    
    **$contact** ⇒ *Send contact if needed of the creator*

    """

def change_username(old, new):
    data = access_data()
    to_change = data[old]
    data[new] = to_change
    del data[old]
    write_data(data)