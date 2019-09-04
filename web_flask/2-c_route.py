#!/usr/bin/python3
# task 0
"""module web_flask
"""
from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello2():
    return 'HBNB'


@app.route('/c/<text>')
def hello3(text):
    text = text.replace("_", " ")
    return 'C %s' % escape(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
