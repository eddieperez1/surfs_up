from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/hola')
def hola_mundo():
    return 'Hola el mundo'