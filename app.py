from flask import Flask, render_template
import random
from phrases import lyrics_raffa

app = Flask(__name__)

phrases = lyrics_raffa()

@app.route('/')
def index():
    random_phrases = random.choice(phrases)
    return render_template('index.html', quote=random_phrases)


@app.route('/')
def reload():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
