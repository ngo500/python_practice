from flask import Flask     #import flask class from module
#from flask import jsonify  #import JSONify from flask to use JSONify
app = Flask(__name__)       #instantiate an object as your class

#pass in URL path, return HTML in method
@app.route('/')
def hello_world():
    return "<b> Test Flask application </b>"            #return HTML
    #return {"message" : "Hello World Dictionary!"}     #return JSON using dictionary
    #return jsonify(message = "Hello World JSONify!")   #return JSON using JSONify
