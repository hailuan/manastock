import sqlite3

class ManagerDB():
    def __init__(self, user = 'admin'):
        pass

    def conect_database(self):
        return sqlite3.connect('stock.db')


