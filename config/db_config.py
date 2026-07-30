# Database configuration
import mysql.connector

def connect_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mayank",
            database="vehicle_service_db"
        )

        return connection

    except mysql.connector.Error as err:
        print("Database Error :", err)
        return None