from database import get_connection

class Book:

    def add_book(self, title, author):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO books (title, author) VALUES (%s, %s)",
            (title, author)
        )

        connection.commit()
        cursor.close()
        connection.close()
        print(f'Book "{title}" by {author} added successfully.')

    def view_all_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, title, author, is_available FROM books")
        books = cursor.fetchall()

        cursor.close()
        connection.close()

        if not books:
            print("No books in the library yet.")
            return

        print("\n--- All Books ---")
        for book in books:
            status = "Available" if book[3] else "Issued"
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {status}")

    def search_book(self, keyword):
        connection = get_connection()
        cursor = connection.cursor()

        # Search by title or author using LIKE
        cursor.execute(
            "SELECT id, title, author, is_available FROM books WHERE title LIKE %s OR author LIKE %s",
            (f"%{keyword}%", f"%{keyword}%")
        )
        books = cursor.fetchall()

        cursor.close()
        connection.close()

        if not books:
            print("No books found.")
            return

        print("\n--- Search Results ---")
        for book in books:
            status = "Available" if book[3] else "Issued"
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {status}")
