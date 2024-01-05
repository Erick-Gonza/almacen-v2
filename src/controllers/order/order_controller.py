import pymysql
from src.database.connection import connectionDB as db


class Order():
    def __init__(self):
        self.connection = db()
        self.cursor = self.connection.cursor()

    def get_profit(self):
        sql = """
        SELECT SUM(order_details.quantity * products.price) AS profit
        FROM orders JOIN order_details ON orders.id_order = order_details.id_order
        JOIN products ON order_details.id_product = products.id_product;"""
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def get_all_orders(self):
        sql = """
        SELECT orders.id_order, orders.date, orders.return_status, customers.name AS customer_name, customer_addresses.address AS customer_address, customer_addresses.city AS customer_city, customer_addresses.postal_code AS customer_postal_code, order_details.id_order_detail, order_details.quantity, products.id_product, products.name AS product_name
        FROM orders JOIN customers ON orders.id_customer = customers.id_customer
        LEFT JOIN customer_addresses ON orders.id_customer = customer_addresses.id_customer
        LEFT JOIN order_details ON orders.id_order = order_details.id_order
        LEFT JOIN products ON order_details.id_product = products.id_product;"""
        # LEFT JOIN product_movements ON products.id_product = product_movements.id_product;
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def get_single_order(self, id_order):
        try:
            self.cursor.execute(
                f"SELECT * FROM orders WHERE id = {id_order}")
            result = self.cursor.fetchall()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def update_order(self, id_order, id_customer, return_status, id_order_detail, id_product, quantity):
        try:
            sql = f"UPDATE orders SET id_customer = {id_customer}, return_status = '{
                return_status}' WHERE id_order = {id_order}"
            self.cursor.execute(sql)
            self.connection.commit()
            sql2 = f"UPDATE order_details SET id_product = {id_product}, quantity = {
                quantity} WHERE id_order_detail = {id_order_detail}"
            self.cursor.execute(sql2)
            self.connection.commit()
            return True
        except pymysql.Error as e:
            return f'Error: {e}'

    def delete_order(self, id_order):
        try:
            sql = f"DELETE FROM order_details WHERE id_order = {id_order}"
            self.cursor.execute(sql)
            self.connection.commit()
            sql2 = f"DELETE FROM orders WHERE id_order = {id_order}"
            self.cursor.execute(sql2)
            self.connection.commit()
            return True
        except pymysql.Error as e:
            return f'Error: {e}'

    def close_connection(self):
        self.connection.close()
        self.cursor.close()
