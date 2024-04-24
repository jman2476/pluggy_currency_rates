# import statements
from flask import Flask
from bs4 import BeautifulSoup
import requests

# tuple containing the websites to scrape
sites_to_scrape = ('https://www.ambito.com/contenidos/dolar.html', 
                   'https://www.dolarhoy.com', 
                   'https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB')

# list to contain the requested webpages


# initialize the flask application?
app = Flask(__name__)

# makes the default route for the api
@app.route('/') # this line defines the route where the api can be accessed
def hello(): # this line defines the function that will run when the path is accessed
    print('hello console!')
    return "Hellow browser!"

if __name__ == '__main__':
    app.run(port=5000)