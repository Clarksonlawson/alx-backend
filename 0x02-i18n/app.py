#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from pytz import timezone, exceptions
from datetime import datetime
import pytz

class Config:
    """Configuration for supported languages and Babel settings"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """Return user dictionary or None if user not found"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

@app.before_request
def before_request():
    """Set g.user to the logged-in user or None"""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """Select the best match language for the user"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """Determine the correct timezone for the user"""
    try:
        tzname = request.args.get('timezone')
        if tzname:
            return timezone(tzname)
        if g.user:
            return timezone(g.user['timezone'])
    except exceptions.UnknownTimeZoneError:
        return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])
    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])

@app.route('/')
def index():
    """Route for the index page"""
    tz = get_timezone()
    current_time = datetime.now(tz).strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
