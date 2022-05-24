import json

def access_activities():
    with open("files/activities.json", 'r') as f:
        return json.load(f)

def write_activities(data):
    with open("files/activities.json", 'w') as f:
        json.dump(data, f, indent=4)

def add_match(result: str, team: str, note=None):
    data = access_activities()
    


