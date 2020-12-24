import requests as reqs
from bs4 import BeautifulSoup

from Repository import ProductsRepository as db

def fetchData(url):
    # tested with --> url = r'https://www.amazon.de/Nintendo-eShop-Card-Guthaben-Download/dp/B07VDM78H4/'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    response = reqs.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    productData = list()

    productData.append({"url": url})
    productData.append({"titel": soup.find(id="productTitle").get_text().strip()})
    productData.append({"currentprice": float(soup.find(id="priceblock_ourprice").get_text().replace(',', '.')[0:5])})

    return productData


def compareData():

    products = db.getAllProducts()

    for product in products:
        currentData = fetchData(product["url"])

        if(product["expectedprice"] >= currentData[2]["currentprice"]):
            print(product)