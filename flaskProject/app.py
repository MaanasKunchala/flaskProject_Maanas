from flask import Flask

app = Flask(__name__)


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/convert/<celsius>')
def convert(celsius=0):
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    return f""" 
    <p>Celsius: {celsius}</p>  
    <p> Fahrenheit: {fahrenheit}</p> 
    """


if __name__ == '__main__':
    app.run()
