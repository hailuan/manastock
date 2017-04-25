import sqlite3

conn = sqlite3.connect('stock.db')
cursor = conn.cursor()

# Products
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    code TEXT,
    name TEXT,
    adr TEXT,
    tel INTEGER,
    desc TEXT,
    price_purchase INTERGER,
    price_sale INTEGER
)
""")

# Providers
cursor.execute("""
CREATE TABLE IF NOT EXISTS Providers(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    adr TEXT,
    tel INTEGER,
    desc TEXT
)
""")

# ProviderToProduct
cursor.execute("""
CREATE TABLE IF NOT EXISTS ProviderToProduct(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    idproduct INTEGER,
    idprovider INTEGER,
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Products(id),
    CONSTRAINT f_idprovider FOREIGN KEY (idprovider) REFERENCES Providers(id)
)
""")

# PriceHistory
cursor.execute("""
CREATE TABLE IF NOT EXISTS PriceHistory(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    date DATETIME,
    idproduct INTEGER,
    idprovider INTEGER,
    amount INTEGER,
    price INTEGER,
    desc TEXT,
    CONSTRAINT f_idprovider FOREIGN KEY (idprovider) REFERENCES Providers(id),
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Products(id)
)
""")

# Stock
cursor.execute("""
CREATE TABLE IF NOT EXISTS Stock(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    location VARCHAR(100),
    desc TEXT
)
""")

# ManagerStock
cursor.execute("""
CREATE TABLE IF NOT EXISTS ManagerStock(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    idstock INTEGER,
    quantity INTEGER,
    price INTEGER,
    status VARCHAR(10),
    CONSTRAINT f_idstock FOREIGN KEY (idstock) REFERENCES Stock(id),
    CONSTRAINT check_status CHECK(status IN ('in','out','return'))
)
""")

# Clients
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    adr TEXT,
    tel INTEGER,
    desc TEXT
)
""")

# OrdersClient
cursor.execute("""
CREATE TABLE IF NOT EXISTS OrdersClient(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    idproduct INTEGER,
    idclient INTEGER,
    adress_delive TEXT,
    quantity INTEGER,
    price_total INTEGER,
    date_order DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    date_delivery DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    status TEXT,
    shipper TEXT,
    desc TEXT,
    CONSTRAINT check_status CHECK(status IN ('delived','treating','cancel')),
    CONSTRAINT f_idclient FOREIGN KEY (idclient) REFERENCES Clients(id),
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Product(id),
    CONSTRAINT check_date CHECK (date_delivery >= date_order)
)
""")

# MyOrder
cursor.execute("""
CREATE TABLE IF NOT EXISTS OrdersClient(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    idproduct INTEGER,
    idprovider INTEGER,
    quantity INTEGER,
    price_total INTEGER,
    date_order DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    date_delivery DATETIME DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    status TEXT,
    desc TEXT
    CONSTRAINT check_status CHECK(status IN ('delived','treating','cancel')),
    CONSTRAINT f_idprovider FOREIGN KEY (idprovider) REFERENCES Provider(id),
    CONSTRAINT f_idproduct FOREIGN KEY (idproduct) REFERENCES Product(id),
    CONSTRAINT check_date CHECK (date_delivery >= date_order)
)
""")

cursor.execute("""
INSERT INTO Clients(name, desc) VALUES('special', 'client non fidélité, Khách lẻ')
""")

conn.commit()
conn.close()
