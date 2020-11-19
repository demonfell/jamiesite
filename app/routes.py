from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    fortune_text = "You are special."
    albums = [
        {
            'artist': 'Landmine Marathon',
            'title': 'Sovereign Descent'
        },
        {
            'artist': 'Panopticon',
            'title': 'Live Migration'
        },
        {
            'artist': 'Cable',
            'title': 'It Cost Me Everything'
        },
        {
            'artist': 'Zozobra',
            'title': 'Birds of Prey'
        },
    ]
    return render_template('index.html', title='The Homepage of Jamie', fortune_text=fortune_text, albums=albums)
    # return "Hello, whirled."