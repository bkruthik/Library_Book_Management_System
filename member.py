from database import get_connection


class Member:

    def add_member(self, name, email):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO members (name, email) VALUES (%s, %s)",
            (name, email)
        )

        connection.commit()
        cursor.close()
        connection.close()
        print(f'Member "{name}" added successfully.')

    def view_all_members(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, name, email FROM members")
        members = cursor.fetchall()

        cursor.close()
        connection.close()

        if not members:
            print("No members registered yet.")
            return

        print("\n--- All Members ---")
        for member in members:
            print(f"ID: {member[0]} | Name: {member[1]} | Email: {member[2]}")
