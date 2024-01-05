import pymysql
from src.database.connection import connectionDB as db


class Customer():
    def __init__(self):
        self.connection = db()
        self.cursor = self.connection.cursor()

    def create_customer(self, name, email, phone, address, city, postal_code):
        try:
            sql1 = f"INSERT INTO customers (name, email, phone) VALUES ('{
                name}', '{email}', '{phone}')"
            self.cursor.execute(sql1)
            id_customer = self.cursor.lastrowid
            self.connection.commit()

            sql2 = f"INSERT INTO customer_addresses (id_customer, address, city, postal_code) VALUES ('{
                id_customer}','{address}', '{city}', '{postal_code}')"
            self.cursor.execute(sql2)
            self.connection.commit()
            return True
        except pymysql.Error as e:
            return f'Error: {e}'

    def get_all_customers(self):
        try:
            sql = "SELECT customers.id_customer, customers.name AS customer_name,customers.email, customers.phone, customer_addresses.address AS customer_address, customer_addresses.city AS customer_city, customer_addresses.postal_code AS customer_postal_code FROM customers LEFT JOIN customer_addresses ON customers.id_customer = customer_addresses.id_customer"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def get_single_customer(self, id_customer):
        try:
            self.cursor.execute(
                f"SELECT * FROM customers WHERE id = {id_customer}")
            result = self.cursor.fetchone()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def update_customer(self, id_customer, name, email, phone, address, city, postal_code):
        try:
            sql1 = f"UPDATE customers SET name = '{name}', email = '{
                email}', phone = '{phone}' WHERE id_customer = {id_customer}"
            self.cursor.execute(sql1)
            self.connection.commit()

            sql2 = f"UPDATE customer_addresses SET address = '{address}', city = '{
                city}', postal_code = '{postal_code}' WHERE id_customer = {id_customer}"
            self.cursor.execute(sql2)
            self.connection.commit()
            return True
        except pymysql.Error as e:
            return f'Error: {e}'

    def delete_customer(self, id_customer):
        try:
            sql = f"DELETE FROM customers WHERE id_customer = {id_customer}"
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except pymysql.Error as e:
            return f'Error: {e}'

    def close_connection(self):
        self.connection.close()
        self.cursor.close()
