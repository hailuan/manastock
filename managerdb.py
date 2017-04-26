import sqlite3


class ManagerDB():
    def __enter__(self):
        """Enter a ``with`` block"""
        return self

    def __init__(self, db):
        """
        open a database sqlite

        :param db: string, path to database
        """
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def insert(self, table, list_attrs, list_values):
        values = '(' + ','.join(["'" + i + "'" for i in list_values]) + ')'
        attrs = '(' + ','.join(list_attrs) + ')'
        r = "INSERT INTO " + table + attrs + " VALUES" + values
        self.cursor(r)
        self.conn.commit()

    def update(self, table, key, key_value, list_attrs, list_values):
        set_values = ",".join(
            [a + '=' + "'" + v + "'" for a, v in zip(list_attrs, list_values)])
        r = "UPDATE " + table + \
            " SET " + set_values + \
            " WHERE " + key + "='" + key_value + "'"
        self.cursor(r)
        self.conn.commit()

    def filtertable(self, table, list_condition=None, order=None):
        cur = self.conn.cursor()
        r = "SELECT * FROM " + table
        if list_condition is not None:
            r += " WHERE " + " AND ".join(list_condition)
        if order is not None:
            r += " ORDER BY " + ",".join(order)
        return cur.execute(r)

    def update_product_price(self, idproduct, quantity, price_total):
        cur_stock = self.conn.cursor()
        cur_stock.execute("SELECT SUM(quantity) "
                          "FROM ManagerStock "
                          "WHERE idproduct = ? "
                          "GROUP BY idproduct"
                          , str(idproduct))
        old_quantity = cur_stock.fetchone()[0]

        cur_price = self.conn.cursor()
        cur_stock.execute("SELECT price_purchase FROM Products WHERE id = ?", str(idproduct))
        old_price = cur_price.fetchone()[0]

        price_purchase = (price_total + (old_price * old_quantity)) \
                         / (old_quantity + quantity)
        new_price = price_total / quantity
        self.cursor.execute("UPDATE Products SET price_purchase=:pp,price_new=:np"
                            " WHERE id=:i ",
                            {"pp": price_purchase, "np": new_price, "i": idproduct})
        self.conn.commit()

    def detail_orderclient(self, idorder):
        cur_detail = self.conn.cursor()


    def close(self):
        self.conn.close()

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        """"Exit a ``with`` block."""
        self.close()

if __name__ == "__main__":
    manager = ManagerDB('/home/nguyen/PycharmProjects/manastock/stock.db')
