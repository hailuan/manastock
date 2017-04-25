import sqlite3

def conect_database():
    return sqlite3.connect('stock.db')

