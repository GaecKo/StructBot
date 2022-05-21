from random import randint
import json
from threading import Thread
from datetime import date, time, datetime 
import time

def add_quote(quote):
    with open("assets/files/quotes.txt", "a") as f:
        f.write(f"\n{quote}")

def get_mohem():
    base = "mohem"
    for i in range(randint(0, 100)):
        base += "m"
    if randint(1, 2) == 1:
        base += " frère"
    return base

def get_quote():
	with open("assets/quotes.txt", encoding="utf-8") as f:
		return f.readlines()[randint(0, len(f.readlines()))]