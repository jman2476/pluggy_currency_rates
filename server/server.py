# import statements
from flask import Flask

app = Flask(__name__)

# makes the default route for the api
@app.route('/') # this line defines the route where the api can be accessed
def hello(): # this line defines the function that will run when the path is accessed
    print('hello console!')
    return "Hellow browser!"

if __name__ == '__main__':
    app.run(port=5000)