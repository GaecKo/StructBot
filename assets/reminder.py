import json
from datetime import datetime 

def access_reminder():
    with open("files/reminder.json", 'r') as f:
        return json.load(f)

def write_reminder(data):
    with open("files/reminder.json", 'w') as f:
        json.dump(data, f, indent=4)

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
    raise ValueError

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

def sort_reminder():
    event = []
    data = access_reminder()
    for key, value in data.items():
        date = datetime.strptime(key, "%Y-%m-%d %H:%M:%S")
        event.append([date, value])
    event.sort(key=lambda x: x[0], reverse=False)
    new_data = {}
    for i in range(len(event)):
        new_data[str(event[i][0])] = event[i][1]
    write_reminder(new_data)