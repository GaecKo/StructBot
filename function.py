from random import randint
import json

def access_json():
    with open("assets/data.json", 'r') as f:
        return json.load(f)



def write_json(data):
    with open("assets/data.json", 'w') as f:
        json.dump(data, f, indent=4)

def get_quote():
	with open("assets/quotes.txt", encoding="utf-8") as f:
		return f.readlines()[randint(0, 29)]

def top_board():
    data = access_json()
    result = []
    for pseudo, stats in data.items():
        for key, value in stats.items():
            if result == []:
                result.append()
            pass


def update_kill_death_stats(kill, death, pseudo):
    data = access_json()
    if pseudo in data:
        data[pseudo]["kill"] += int(kill)
        data[pseudo]["death"] += int(death)
    elif pseudo not in data:
        data[pseudo] = {
            "kill" : int(kill),
            "death": int(death),
            "points": 0
        }
    write_json(data)

def check_pseudo_in_data(pseudo):
    data = access_json()
    if pseudo in data:
        return True
    return False

def show_kill_death_stats(pseudo):
    data = access_json()
    if pseudo in data:
        return f"Le joueurs **{pseudo}** a __{data[pseudo]['kill']} kills__ et  __{data[pseudo]['death']} morts__."
    return f"Je n'ai aucune donnée sur {pseudo}. Utilisez $kdstat `kill` `death` `pseudo` pour en ajouter."

def help():
    return """
    Here are somme command you can use:
    $help -> send you help
    $quotes -> send a gaming quote
    $kdstat `pseudo` `kills` `deaths`-> Update K/D of a player
    $git -> send the git repository of this bot
    """

