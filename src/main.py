from Repository import ProductsRepository as db
from Logic import RequestLogic as rl

def addNewProduct():
    url = input('URL:')
    price = float(input('Expected Price:'))

    productdata = rl.fetchData(url)
    productdata.append({"expectedprice": price})

    db.insertNewProduct(productdata[1]['titel'], productdata[0]['url'], float(productdata[2]['currentprice']), float(productdata[3]['expectedprice']))

def main():
    db.initDatabase()
    # db.testDatabase()

    while 1 == 1:
        print('Please select what you want to do:')
        print('1. Add a new URL and expected Price')
        print('2. Fetch data from URL')
        menu = int(input('?: '))

        if(menu == 1):
            addNewProduct()
        if(menu == 2):
            rl.compareData()

main()



