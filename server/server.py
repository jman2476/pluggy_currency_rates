# import statements
from flask import Flask
from bs4 import BeautifulSoup
import requests

# tuple containing the websites to scrape
sites_to_scrape = ('https://www.ambito.com/contenidos/dolar.html', 
                   'https://www.dolarhoy.com', 
                   'https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB')

# list to contain the requested webpages
scrapings = (requests.get(sites_to_scrape[i]) for i in range(3))
# scrapings = [requests.get(sites_to_scrape[0]),
#              requests.get(sites_to_scrape[1]),
#              requests.get(sites_to_scrape[2])]

# make it into soup, ideally beautiful
soups = [BeautifulSoup(scrapings[j], 'html.parser') for j in range(3)]

# initialize the flask application?
app = Flask(__name__)

# makes the default route for the api
@app.route('/') # this line defines the route where the api can be accessed
def hello(): # this line defines the function that will run when the path is accessed
    print(scrapings)
    print(soups)
    return 'scrapings'

if __name__ == '__main__':
    app.run(port=5000)