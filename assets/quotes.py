from random import randint

def add_quote(quote):
    with open("files/quotes.txt", "a") as f:
        f.write(f"\n{quote}")

def get_mohem():
    base = "mohem"
    for i in range(randint(0, 100)):
        base += "m"
    if randint(1, 2) == 1:
        base += " frère"
    return base

def get_quote():
	with open("files/quotes.txt", encoding="utf-8") as f:
		return f.readlines()[randint(0, len(f.readlines()))]