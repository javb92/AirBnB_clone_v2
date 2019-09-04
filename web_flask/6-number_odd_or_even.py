#!/usr/bin/python3
# task 0
"""module web_flask
"""
from flask import Flask, escape, render_template
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


@app.route('/python/<text>')
def hello4(text):
    text = text.replace("_", " ")
    return 'Python %s' % escape(text)


@app.route('/python/')
def hello5():
    text = "is cool"
    text = text.replace("_", " ")
    return 'Python %s' % escape(text)


@app.route('/number/<int:n>')
def hello6(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def hello7(n):
    return render_template('5-number.html', name=n)


@app.route('/number_odd_or_even/<int:n>')
def hello8(n):
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
