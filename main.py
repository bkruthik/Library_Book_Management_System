from database import setup_database
from book import Book
from member import Member
from library import Library


def main():
    # Set up the database and tables when the program starts
    setup_database()
    book = Book()
    member = Member()
    library = Library()

    
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Add Member")
        print("5. View All Members")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. View Overdue Books")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book.add_book(title, author)

        elif choice == "2":
            book.view_all_books()

        elif choice == "3":
            keyword = input("Search by title or author: ")
            book.search_book(keyword)

        elif choice == "4":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            member.add_member(name, email)

        elif choice == "5":
            member.view_all_members()

        elif choice == "6":
            book.view_all_books()
            book_id = int(input("Enter Book ID to issue: "))
            member.view_all_members()
            member_id = int(input("Enter Member ID: "))
            library.issue_book(book_id, member_id)

        elif choice == "7":
            book.view_all_books()
            book_id = int(input("Enter Book ID to return: "))
            library.return_book(book_id)

        elif choice == "8":
            library.view_overdue_books()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
