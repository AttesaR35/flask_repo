from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    page = """
    <h1>Welcome</h1>
    """
    return page

@app.route('/welcome/home')
def welhome():
    page = """
    <h1>Welcome Home</h1>
    """
    return page

@app.route('/welcome/back')
def welback():
    page = """
    <h1>Welcome Back</h1>
    """
    return page
