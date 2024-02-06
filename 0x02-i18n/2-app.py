#!/usr/bin/env python3
"""flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """config for babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """gets a local for language to load"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """home"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)