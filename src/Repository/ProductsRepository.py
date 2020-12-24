import sqlite3

conn = sqlite3.connect('./amazon.db')

def initDatabase():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products (titel text, url text, currentPrice decimal, expectedPrice decimal)''')
    conn.commit()

def insertNewProduct(titel, url, currentPrice, expectedPrice):
    sql = "INSERT INTO Products VALUES(?, ?, ?, ?)"
    args = (titel, url, currentPrice, expectedPrice)
    cursor = conn.execute(sql, args)
    conn.commit()

def getAllProducts():
    products = list()
    c = conn.cursor()

    for r in c.execute('SELECT * FROM Products'):
        products.append({"titel": r[0], "url": r[1], "currentprice": float(r[2]), "expectedprice": float(r[3])})

    return products

def testDatabase():
    c = conn.cursor()

    for r in c.execute('SELECT * FROM Products'):
        print(r)