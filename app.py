from flask import Flask 

app=Flask(__name__)
@app.route("/")
def index():
    return "hello"
@app.route("/home")
def home():
    return "Welcome"
@app.route("/About")
def about():
    return"Welcome to my about page"
if(__name__=="__main__"):
    app.run()
