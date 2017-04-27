"""Creeate a empty database at installation
This use module sqlite3
"""

import sqlite3

conn = sqlite3.connect('stock.db')
cursor = conn.cursor()

# Products
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT,
    name TEXT,
    desc TEXT,
    image BLOB,
    price_purchase INTEGER,
    price_new INTEGER,
    price_sale INTEGER
)
""")

# MyDiscount
cursor.execute("""
CREATE TABLE IF NOT EXISTS MyDiscount(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idproduct INTEGER,
    quantity INTEGER,
    discount REAL,
    CONSTRAINT unique_discount UNIQUE (idproduct,quantity)
)
""")

# Providers
cursor.execute("""
CREATE TABLE IF NOT EXISTS Providers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    adr TEXT,
    tel INTEGER,
    desc TEXT
)
""")

# ProductFromProvider
cursor.execute("""
CREATE TABLE IF NOT EXISTS ProductFromProvider(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idproduct INTEGER,
    idprovider INTEGER,
    amount INTEGER,
    price INTEGER,
    desc TEXT,
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Products(id),
    CONSTRAINT f_idprovider FOREIGN KEY (idprovider) REFERENCES Providers(id)
)
""")

# Stock
cursor.execute("""
CREATE TABLE IF NOT EXISTS Stock(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location VARCHAR(100),
    desc TEXT
)
""")

# ManagerStock
cursor.execute("""
CREATE TABLE IF NOT EXISTS ManagerStock(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idstock INTEGER,
    idproduct INTEGER,
    quantity INTEGER,
    CONSTRAINT f_idstock FOREIGN KEY (idstock) REFERENCES Stock(id),
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Products(id)
)
""")

# Clients
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    adr TEXT,
    tel INTEGER,
    desc TEXT
)
""")



# OrderClient
cursor.execute("""
CREATE TABLE IF NOT EXISTS OrderClient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT,
    idclient INTEGER,
    adress_delive TEXT,
    date_order DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    date_delivery DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    price_total INTEGER,
    status TEXT,
    desc TEXT,
    CONSTRAINT check_status CHECK(status IN ('delived','treating','cancel','partial')),
    CONSTRAINT f_idclient FOREIGN KEY (idclient) REFERENCES Clients(id),
    CONSTRAINT check_date CHECK (date_delivery >= date_order)
)
""")

# DetailOrderClient
cursor.execute("""
CREATE TABLE IF NOT EXISTS DetailOrderClient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idorder INTEGER,
    idproduct INTEGER,
    quantity INTEGER,
    price INTEGER,
    desc TEXT,
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Products(id),
    CONSTRAINT f_idorder FOREIGN KEY (idorder) REFERENCES OrderClient(id)
)
""")

# DeliveryClient
cursor.execute("""
CREATE TABLE IF NOT EXISTS DeliveryClient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shipper TEXT,
    idorder INTEGER,
    date_delivery DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    desc TEXT,
    CONSTRAINT f_idorder FOREIGN KEY (idorder) REFERENCES OrderClient(id)
)
""")

# DetailDelyreyClient
cursor.execute("""
CREATE TABLE IF NOT EXISTS DetailDeliveryClient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    iddelivery,
    idorder INTEGER,
    idproduct INTEGER,
    quantity INTEGER,
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Products(id),
    CONSTRAINT f_idelivery FOREIGN KEY (iddelivery) REFERENCES DeliveryClient(id)
)
""")

# MyOrders
cursor.execute("""
CREATE TABLE IF NOT EXISTS MyOrders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT,
    idprovider INTEGER,
    price_total INTEGER,
    date_order DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    date_delivery DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    status TEXT,
    desc TEXT,
    CONSTRAINT check_status CHECK(status IN ('delived','treating','cancel')),
    CONSTRAINT f_idprovider FOREIGN KEY (idprovider) REFERENCES Providers(id),
    CONSTRAINT check_date CHECK (date_delivery >= date_order)
)
""")

# DetailMyOrders
cursor.execute("""
CREATE TABLE IF NOT EXISTS DetailMyOrders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idorder INTEGER,
    idproduct INTEGER,
    quantity INTEGER,
    price INTEGER,
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Products(id),
    CONSTRAINT f_idorder FOREIGN KEY (idorder) REFERENCES MyOrders(id)
)
""")

cursor.execute("""
INSERT INTO Clients(name, desc) VALUES('special', 'client non fidélité, Khách lẻ')
""")

conn.commit()
conn.close()
