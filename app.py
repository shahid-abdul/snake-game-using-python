# app.py
from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_game')
def start_game():
    subprocess.Popen(["python", "game.py"])
    return "Game Started!"

if __name__ == "__main__":
    app.run(debug=True)
