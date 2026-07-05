# models/book.py
from database import get_connection

class Book:
    def __init__(self, title, author, isbn, quantity, book_id=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.available_quantity = quantity

    def add_book(self):
        """Adds a new book record to the database."""
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO books (title, author, isbn, quantity, available_quantity) VALUES (?, ?, ?, ?, ?)"
                cursor.execute(query, (self.title, self.author, self.isbn, self.quantity, self.available_quantity))
                conn.commit()
                print(f"[SUCCESS] Book '{self.title}' added successfully!")
            except Exception as e:
                print(f"[ERROR] Failed to add book: {e}")
            finally:
                conn.close()

    @staticmethod
    def view_all_books():
        """Fetches and displays all books."""
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            conn.close()
            
            print("\n--- Book Inventory ---")
            for b in books:
                print(f"ID: {b[0]} | Title: {b[1]} | Author: {b[2]} | Available: {b[5]}/{b[4]}")