class Customer:
    pass
from database import Database

class Customer:
    def __init__(self):
        self.db = Database()

    def add_customer(self, name, phone, address):
        query = """
        INSERT INTO customers (name, phone, address)
        VALUES (%s, %s, %s)
        """
        values = (name, phone, address)
        return self.db.execute(query, values)

    def get_all_customers(self):
        query = "SELECT * FROM customers"
        return self.db.fetch(query)

    def search_customer(self, phone):
        query = "SELECT * FROM customers WHERE phone=%s"
        return self.db.fetch(query, (phone,))

    def update_customer(self, customer_id, name, phone, address):
        query = """
        UPDATE customers
        SET name=%s, phone=%s, address=%s
        WHERE customer_id=%s
        """
        values = (name, phone, address, customer_id)
        return self.db.execute(query, values)

    def delete_customer(self, customer_id):
        query = "DELETE FROM customers WHERE customer_id=%s"
        return self.db.execute(query, (customer_id,))