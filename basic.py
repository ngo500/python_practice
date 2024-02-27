from flask import Flask     #import flask class from module
app = Flask(__name__)       #instantiate an object as your class

#pass in URL path, return HTML in method
@app.route('/')
def hello_world():
    return "<b> Test Flask application </b>"
