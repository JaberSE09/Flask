from flask import Flask

app=Flask(__name__)
@app.route('/welcome')
def welcome():
    return "Welcome"
@app.route('/welcome/<name>')
def welcomeName(name):
    return f"Welcome {name}"