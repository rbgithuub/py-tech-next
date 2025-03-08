"""Import the flask package"""
from flask import Flask

"""Instantiate Flask object and assign it to a variable"""
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()