from random import randint

def get_quote():
	with open("librairies/quotes.txt", encoding="utf-8") as f:
		return f.readlines()[randint(0, 30)]