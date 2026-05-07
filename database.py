import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",         # change to your MySQL username
        password="",         # change to your MySQL password
        database="library_db"
    )
    return connection


def setup_database():
    # Connect without selecting a database first, so we can create it
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
    cursor.execute("USE library_db")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(200),
            author VARCHAR(100),
            is_available BOOLEAN DEFAULT TRUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)

    # transactions links a book and a member together
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            book_id INT,
            member_id INT,
            issue_date DATE,
            return_date DATE,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (member_id) REFERENCES members(id)
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("Database and tables are ready.")
