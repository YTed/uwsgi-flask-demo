from flask import Flask
from ..submodule.hello import say_hello

app = Flask(__name__)

@app.route('/')
def hello():
    greeting = say_hello()
    return greeting

def run(host='127.0.0.1', port=5000, debug=True):
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    run()
