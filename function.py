from random import randint

def get_quote():
	with open("librairies/quotes.txt", encoding="utf-8") as f:
		return f.readlines()[randint(0, 29)]

def add_kill_death_stats(kill, death, pseudo):
    with open('librairies/temp.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    content.append(f'Pseudo: {pseudo}\n')
    content.append(f'Kills: {kill}\n')
    content.append(f'Deaths: {death}\n\n')
    with open('librairies/temp.txt', 'w', encoding='utf-8') as f:
        f.writelines(content)

def check_pseudo_for_stat(pseudo):
    with open('librairies/temp.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    for i in range(0, len(content), 3):
        try:
            if content[i].split()[1] == pseudo:
                return True
        except:
            pass
    return False

def change_kill_death_stats(kill, death, pseudo):
    with open('librairies/temp.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    for i in range(0, len(content), 3):
        #try:
        if content[i].split()[1] == pseudo:
            content[i] = f"Pseudo: {pseudo}\n"
            content[i+1] = f"Kills: {int(content[i+1].split()[1]) + int(kill)}\n" 
            content[i+2] = f"Kills: {int(content[i+2].split()[1]) + int(death)}\n"
            break
        #except Exception as e:
            #print(e)
            #pass
    with open('librairies/temp.txt', 'w', encoding='utf-8') as f:
        f.writelines(content)

def show_kill_death_stats(pseudo):
    if check_pseudo_for_stat(pseudo):
        pass