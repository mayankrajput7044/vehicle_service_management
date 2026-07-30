from tkinter import Tk
from config.db_config import connect_database

def main():
    # Check database connection
    conn = connect_database()

    if conn:
        print("Database Connected Successfully")

    root = Tk()
    root.title("Vehicle Service Management System")
    root.geometry("900x600")
    root.mainloop()

if __name__ == "__main__":
    main()