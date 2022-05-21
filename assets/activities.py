from random import randint
import json
from threading import Thread
from datetime import date, time, datetime 
import time

def access_activities() 
    with open("assets/files/activities.json", 'r') as f:
        return json.load(f)

def write_activities(data):
    with open("assets/files/activities.json", 'w') as f:
        json.dump(data, f, indent=4)