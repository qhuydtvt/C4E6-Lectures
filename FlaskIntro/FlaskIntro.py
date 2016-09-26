from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello C4E6'

@app.route('/index')
def index():
    return "Welcome to C4E"

@app.route('/trong')
def hello_trong():
    return "Hello Trong xinh"

@app.route('/<name>')
def hello(name):
    return "hello " + name


@app.route("/sum/<int:num1>/<int:num2>")
def sum(num1, num2):
    return "{0}".format(num1 + num2)

if __name__ == '__main__':
    app.run()

