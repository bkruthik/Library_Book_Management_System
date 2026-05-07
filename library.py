from database import get_connection
from datetime import date


class Library:

    def issue_book(self, book_id, member_id):
        connection = get_connection()
        cursor = connection.cursor()

        # First check if the book is available
        cursor.execute("SELECT is_available FROM books WHERE id = %s", (book_id,))
        result = cursor.fetchone()

        if not result:
            print("Book not found.")
            cursor.close()
            connection.close()
            return

        if not result[0]:
            print("Sorry, this book is already issued to someone.")
            cursor.close()
            connection.close()
            return

        # Record the transaction with today's date
        cursor.execute(
            "INSERT INTO transactions (book_id, member_id, issue_date) VALUES (%s, %s, %s)",
            (book_id, member_id, date.today())
        )

        # Mark the book as not available
        cursor.execute("UPDATE books SET is_available = FALSE WHERE id = %s", (book_id,))

        connection.commit()
        cursor.close()
        connection.close()
        print(f"Book ID {book_id} issued to Member ID {member_id} on {date.today()}.")

    def return_book(self, book_id):
        connection = get_connection()
        cursor = connection.cursor()

        # Find the open transaction for this book (no return date yet)
        cursor.execute(
            "SELECT id FROM transactions WHERE book_id = %s AND return_date IS NULL",
            (book_id,)
        )
        transaction = cursor.fetchone()

        if not transaction:
            print("No active issue found for this book.")
            cursor.close()
            connection.close()
            return

        # Set the return date to today
        cursor.execute(
            "UPDATE transactions SET return_date = %s WHERE id = %s",
            (date.today(), transaction[0])
        )

        # Mark the book as available again
        cursor.execute("UPDATE books SET is_available = TRUE WHERE id = %s", (book_id,))

        connection.commit()
        cursor.close()
        connection.close()
        print(f"Book ID {book_id} returned successfully on {date.today()}.")

    def view_overdue_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        # Books issued more than 14 days ago and still not returned
        cursor.execute("""
            SELECT b.title, m.name, t.issue_date
            FROM transactions t
            JOIN books b ON t.book_id = b.id
            JOIN members m ON t.member_id = m.id
            WHERE t.return_date IS NULL
            AND DATEDIFF(CURDATE(), t.issue_date) > 14
        """)
        overdue = cursor.fetchall()

        cursor.close()
        connection.close()

        if not overdue:
            print("No overdue books right now.")
            return

        print("\n--- Overdue Books (more than 14 days) ---")
        for row in overdue:
            print(f"Book: {row[0]} | Issued to: {row[1]} | Issue Date: {row[2]}")
