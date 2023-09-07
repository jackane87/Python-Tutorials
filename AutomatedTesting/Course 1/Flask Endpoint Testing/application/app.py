#import jsonify because we cannot return a dictionary from an endpoint, so jsonify converts the dictionary string.
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')  # http://mysite.com/
def home():
    return jsonify({'message': 'Hello, world!'})

#This makes sure the app is only run when the app.py file is run. So when we import app.py into our tests, the name will not be __main__, so the app will not be run.
if __name__ == '__main__':
    app.run()