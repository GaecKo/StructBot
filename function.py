from random import randint
import json

def access_json():
    with open("assets/data.json", 'r') as f:
        return json.load(f)

def get_mohem():
    base = "mohem"
    for i in range(randint(0, 100)):
        base += "m"

    if randint(1, 2) == 1:
        base += " frère"
    
    return base

def write_json(data):
    with open("assets/data.json", 'w') as f:
        json.dump(data, f, indent=4)

def get_quote():
	with open("assets/quotes.txt", encoding="utf-8") as f:
		return f.readlines()[randint(0, 29)]

def top_board():
    data = access_json()
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
    data = access_json()
    if pos in data[pseudo]:
        data[pseudo][pos] += 1
    else:
        data[pseudo][pos] = 1
    write_json(data)

def get_points(pseudo):
    data = access_json()
    player_info = data[pseudo]
    points = 0
    for key, value in data[pseudo].items():
        try:
            key = int(key)
            points += value / key
        except:
            continue
    return points 

def update_kill_death_stats(kill, death, pseudo):
    data = access_json()
    if pseudo in data:
        data[pseudo]["kill"] += kill
        data[pseudo]["death"] += death
    elif pseudo not in data:
        data[pseudo] = {
            "kill" : int(kill),
            "death": int(death),
        }
    write_json(data)

def check_pseudo_in_data(pseudo):
    data = access_json()
    if pseudo in data:
        return True
    return False

def show_stats(pseudo):
    data = access_json()
    if pseudo in data:
        if data[pseudo]["death"] != 0:
            k_d = data[pseudo]["kill"] / data[pseudo]["death"]
        else:
            k_d = data[pseudo]["kill"]
        return f"Le joueurs **{pseudo}** a __{data[pseudo]['kill']} kills__ et  __{data[pseudo]['death']} morts__. Son k/d est de {k_d} et ses points mvp sont {get_points(pseudo)}"
    return f"Je n'ai aucune donnée sur {pseudo}. Utilisez $kdstat `kill` `death` `pseudo` pour en ajouter."

def del_user(pseudo):
    data = access_json()
    del data[pseudo]
    write_json(data)
    
def help():
    return """
    __Here are somme command you can use:__
    
    **$help** ⇒ *send you help*
    
    **$quotes** ⇒ *send a gaming quote*
    
    **$kdstat / $kd `pseudo` `kills` `deaths`** ⇒ *Update K/D of a player, kills and deaths must be numbers*
    
    **$stat `pseudo`** ⇒ *shows the stat of a player*
    
    **$delete / $del `pseudo`** ⇒ *deletes all data about a player*
    
    **$mvpstat / $mvp `pseudo` `position`** ⇒ *position must be a number, then add position info of a player*
    
    **$topboard / $top** ⇒ *Shows the general top board with the known stats*
    
    **$git** ⇒ *Send the git repository of this bot*
    
    """

