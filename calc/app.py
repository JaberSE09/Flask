from flask import Flask,request
import operations
app=Flask(__name__)

@app.route('/add')
def add():
    a= request.args["a"]
    b= request.args["b"]
    total=operations.add(int(a), int(b))
    return f"total of {a} + {b} = {total}"

@app.route('/sub')
def sub():
    a= request.args["a"]
    b= request.args["b"]
    total=operations.sub(int(a), int(b))
    return f"total of {a} - {b} = {total}"

@app.route('/mult')
def mult():
    a= request.args["a"]
    b= request.args["b"]
    total=operations.mult(int(a), int(b))
    return f"total of {a} * {b} = {total}"

@app.route('/div')
def div():
    a= request.args["a"]
    b= request.args["b"]
    total=operations.div(int(a), int(b))
    return f"total of {a} / {b} = {total}"

@app.route('/math/<operator>')
def math(operator):
    a= request.args["a"]
    b= request.args["b"]
    if operator == "add":
        total=operations.add(int(a), int(b))
        return f"total of {a} + {b} = {total}"
    if operator == "sub":
        total=operations.sub(int(a), int(b))
        return f"total of {a} - {b} = {total}"
    if operator == "mult":
        total=operations.mult(int(a), int(b))
        return f"total of {a} * {b} = {total}"
    if operator == "div":
        total=operations.div(int(a), int(b))
        return f"total of {a} / {b} = {total}"
    