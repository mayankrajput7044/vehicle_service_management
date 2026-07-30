class Service:
    pass
from database import Database

class Service:
    def __init__(self):
        self.db = Database()

    # Add Service Record
    def add_service(self, vehicle_id, service_date,
                    service_type, mechanic_name,
                    service_cost, next_service_date,
                    status):

        query = """
        INSERT INTO services
        (vehicle_id, service_date, service_type,
         mechanic_name, service_cost,
         next_service_date, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            vehicle_id,
            service_date,
            service_type,
            mechanic_name,
            service_cost,
            next_service_date,
            status
        )

        return self.db.execute(query, values)

    # Get All Service Records
    def get_all_services(self):

        query = """
        SELECT
            s.service_id,
            v.vehicle_no,
            s.service_date,
            s.service_type,
            s.mechanic_name,
            s.service_cost,
            s.next_service_date,
            s.status
        FROM services s
        JOIN vehicles v
        ON s.vehicle_id = v.vehicle_id
        ORDER BY s.service_date DESC
        """

        return self.db.fetch(query)

    # Search Service By Vehicle Number
    def search_service(self, vehicle_no):

        query = """
        SELECT
            s.service_id,
            v.vehicle_no,
            s.service_date,
            s.service_type,
            s.mechanic_name,
            s.service_cost,
            s.next_service_date,
            s.status
        FROM services s
        JOIN vehicles v
        ON s.vehicle_id = v.vehicle_id
        WHERE v.vehicle_no = %s
        """

        return self.db.fetch(query, (vehicle_no,))

    # Update Service
    def update_service(self, service_id,
                       service_type,
                       mechanic_name,
                       service_cost,
                       next_service_date,
                       status):

        query = """
        UPDATE services
        SET service_type=%s,
            mechanic_name=%s,
            service_cost=%s,
            next_service_date=%s,
            status=%s
        WHERE service_id=%s
        """

        values = (
            service_type,
            mechanic_name,
            service_cost,
            next_service_date,
            status,
            service_id
        )

        return self.db.execute(query, values)

    # Delete Service
    def delete_service(self, service_id):

        query = """
        DELETE FROM services
        WHERE service_id=%s
        """

        return self.db.execute(query, (service_id,))