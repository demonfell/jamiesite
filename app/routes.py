from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)