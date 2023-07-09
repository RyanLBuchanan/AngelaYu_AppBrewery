from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/wsup')
def say_wsup():
    return "Wasssssuuuuuup?!"


if __name__ == '__main__':
    app.run()

