from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Rachael Glazner in 3308'
