#!/usr/bin/env python3
from os import getenv
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(
    __name__,
    template_folder='templates',
)


@app.get('/')
def index():
    return render_template('index.html.jinja')


is_development = getenv('APP_ENVIRONMENT') == 'development'
if is_development and __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
