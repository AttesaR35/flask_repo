from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addi():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = add(a,b)
    return str(res)

@app.route('/sub')
def subt():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = sub(a,b)
    return str(res)

@app.route('/mult')
def multi():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = mult(a,b)
    return str(res)

@app.route('/div')
def divi():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    res = div(a,b)
    return str(res)