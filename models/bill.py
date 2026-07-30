class Bill:
    pass
from database import Database

class Billing:
    def __init__(self):
        self.db = Database()

    # Generate Bill
    def generate_bill(self, service_id, subtotal, gst, discount, payment_status):

        total_amount = subtotal + gst - discount

        query = """
        INSERT INTO bills
        (service_id, subtotal, gst, discount,
         total_amount, payment_status)
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (
            service_id,
            subtotal,
            gst,
            discount,
            total_amount,
            payment_status
        )

        return self.db.execute(query, values)

    # Get All Bills
    def get_all_bills(self):

        query = """
        SELECT
            b.bill_id,
            v.vehicle_no,
            s.service_type,
            b.subtotal,
            b.gst,
            b.discount,
            b.total_amount,
            b.payment_status
        FROM bills b
        JOIN services s
            ON b.service_id = s.service_id
        JOIN vehicles v
            ON s.vehicle_id = v.vehicle_id
        ORDER BY b.bill_id DESC
        """

        return self.db.fetch(query)

    # Search Bill
    def search_bill(self, bill_id):

        query = """
        SELECT *
        FROM bills
        WHERE bill_id=%s
        """

        return self.db.fetch(query, (bill_id,))

    # Update Payment Status
    def update_payment(self, bill_id, status):

        query = """
        UPDATE bills
        SET payment_status=%s
        WHERE bill_id=%s
        """

        return self.db.execute(query, (status, bill_id))

    # Delete Bill
    def delete_bill(self, bill_id):

        query = """
        DELETE FROM bills
        WHERE bill_id=%s
        """

        return self.db.execute(query, (bill_id,))