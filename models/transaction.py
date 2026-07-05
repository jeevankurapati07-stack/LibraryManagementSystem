# models/transaction.py
from database import get_connection
from datetime import datetime

class Transaction:
    @staticmethod
    def issue_book(book_id, member_id):
        """Handles real-world validation to issue a book."""
        conn = get_connection()
        if not conn: return

        cursor = conn.cursor()
        
        # Validation Check: Check if book exists and is available
        cursor.execute("SELECT available_quantity FROM books WHERE book_id = ?", (book_id,))
        book = cursor.fetchone()
        
        if not book:
            print("[ERROR] Book ID not found.")
            conn.close()
            return
        
        if book[0] <= 0:
            print("[ERROR] Out of Stock! This book is currently unavailable.")
            conn.close()
            return
        
        # Issue Logic
        issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO transactions (book_id, member_id, issue_date) VALUES (?, ?, ?)", 
                       (book_id, member_id, issue_date))
        
        # Update book availability status
        cursor.execute("UPDATE books SET available_quantity = available_quantity - 1 WHERE book_id = ?", (book_id,))
        
        conn.commit()
        conn.close()
        print(f"[SUCCESS] Book ID {book_id} issued successfully to Member ID {member_id}.")

    @staticmethod
    def return_book(transaction_id):
        """Processes a book return."""
        conn = get_connection()
        if not conn: return

        cursor = conn.cursor()
        cursor.execute("SELECT book_id, status FROM transactions WHERE transaction_id = ?", (transaction_id,))
        tx = cursor.fetchone()

        if not tx:
            print("[ERROR] Transaction Record ID not found.")
            conn.close()
            return
        
        if tx[1] == 'Returned':
            print("[WARNING] This book has already been returned.")
            conn.close()
            return

        book_id = tx[0]
        return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Update Transaction Status
        cursor.execute("UPDATE transactions SET return_date = ?, status = 'Returned' WHERE transaction_id = ?", 
                       (return_date, transaction_id))
        # Update Book Inventory
        cursor.execute("UPDATE books SET available_quantity = available_quantity + 1 WHERE book_id = ?", (book_id,))
        
        conn.commit()
        conn.close()
        print(f"[SUCCESS] Transaction ID {transaction_id} marked as Returned successfully.")