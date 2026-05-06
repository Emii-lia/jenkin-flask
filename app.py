#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'
@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Hello %s!\n' % username

@app.route('/feature/<name>')
def feature_name(name):
    return f"{name} feature"
if __name__ == '__main__':
    app.run(host='0.0.0.0') # open for everyone
