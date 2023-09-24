from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)


# Define a route for the default page
@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


# Define a route for the greet function
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


# Run the Flask app
if __name__ == '__main__':
    app.run()
