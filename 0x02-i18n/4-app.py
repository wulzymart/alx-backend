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
def get_locale() -> str:
    """gets a local for language to load"""
    locale = request.args.get("locale")

    return locale if locale in app.config['LANGUAGES'] else\
        request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """home"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
