# Library Book Management System

A command-line application built with **Python** and **MySQL** to manage a library's books, members, and borrowing records.

---

## What This Project Does

- Add books and members to the library
- Issue a book to a member
- Return a book
- Search books by title or author
- View overdue books (not returned within 14 days)

---

## Project Structure

```
library-management-system/
│
├── main.py          → Entry point, shows the menu
├── book.py          → Book class (add, view, search)
├── member.py        → Member class (add, view)
├── library.py       → Library class (issue, return, overdue)
├── database.py      → Database connection and table setup
└── requirements.txt → Python packages needed
```

---

## Tech Stack

- **Python 3**
- **MySQL**
- **mysql-connector-python** (connects Python to MySQL)
- **OOP** (each feature is a separate class)

---

## How to Run This Project

### Step 1 — Install MySQL
Make sure MySQL is installed and running on your machine.

### Step 2 — Clone this repository
```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

### Step 3 — Install the required Python package
```bash
pip install -r requirements.txt
```

### Step 4 — Update your MySQL credentials
Open `database.py` and update these lines with your MySQL username and password:
```python
user="root",      # your MySQL username
password="",      # your MySQL password
```

### Step 5 — Run the program
```bash
python main.py
```

The program will automatically create the database and tables on first run.

---

## Database Design

### `books` table
| Column       | Type    | Description                  |
|--------------|---------|------------------------------|
| id           | INT     | Auto-generated unique ID     |
| title        | VARCHAR | Book title                   |
| author       | VARCHAR | Author name                  |
| is_available | BOOLEAN | TRUE = available, FALSE = issued |

### `members` table
| Column | Type    | Description              |
|--------|---------|--------------------------|
| id     | INT     | Auto-generated unique ID |
| name   | VARCHAR | Member name              |
| email  | VARCHAR | Member email             |

### `transactions` table
| Column      | Type | Description                          |
|-------------|------|--------------------------------------|
| id          | INT  | Auto-generated unique ID             |
| book_id     | INT  | Foreign key → books.id               |
| member_id   | INT  | Foreign key → members.id             |
| issue_date  | DATE | Date the book was issued             |
| return_date | DATE | Date returned (NULL if not returned) |

---

## Sample Menu

```
===== Library Management System =====
1. Add Book
2. View All Books
3. Search Book
4. Add Member
5. View All Members
6. Issue Book
7. Return Book
8. View Overdue Books
9. Exit
```

---

## Concepts Used

| Concept | Where it's used |
|--------|-----------------|
| OOP (Classes) | Book, Member, Library each have their own class |
| MySQL CRUD | INSERT, SELECT, UPDATE across all operations |
| Foreign Keys | transactions table links books and members |
| JOIN queries | Used to fetch overdue book + member details together |
| LIKE query | Used in book search by title or author |

---

## Author

**Balusu Kruthik**  
B.Tech Computer Science — Sreyas Institute of Engineering and Technology, Hyderabad
