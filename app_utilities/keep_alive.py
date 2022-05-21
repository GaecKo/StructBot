from flask import Flask 
from threading import Thread

app = Flask("StructBot")

@app.route("/")
def main():
    return "StrucBot Keep_alive Page, nothing to see here bro :)"

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()