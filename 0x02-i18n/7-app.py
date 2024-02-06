#!/usr/bin/env python3
"""flask app"""


from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: int = None):
    """mock login function"""
    if not login_as or login_as not in users:
        return None
    return users[login_as]


class Config():
    """config for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """gets a local for language to load"""
    locale = request.args.get("locale")
    locale = locale if locale else g.user.get("locale") if g.get("user")\
        else None
    locale = locale if locale else request.headers.get("locale")

    return locale if locale and locale in app.config['LANGUAGES'] else\
        request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """get timezone"""

    tz = request.args.get('timezone')
    try:
        if tz:
            return timezone(tz).zone
        tz = g.user.get('timezone') if g.user else None
        if tz:
            return timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request() -> None:
    """before request"""
    login_as = request.args.get("login_as")
    try:
        login_as = int(login_as)
        g.user = get_user(login_as)
    except Exception as e:
        g.user = None


@app.route('/')
def index() -> str:
    """home"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
