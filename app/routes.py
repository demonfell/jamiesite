from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    fortune_text = "You are special."
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Exeter!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Hamilton movie was so cool!'
        }
    ]
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
    return render_template('index.html', title='The Homepage of Jamie', fortune_text=fortune_text, albums=albums, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)