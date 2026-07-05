# main.py
import sys
from database import initialize_database
from models.book import Book
from models.member import Member
from models.transaction import Transaction

def main_dashboard():
    while True:
        print("\n================================")
        print("    LIBRARY MANAGEMENT SYSTEM   ")
        print("================================")
        print("1. Add New Book")
        print("2. View Book Inventory")
        print("3. Register New Member")
        print("4. Issue a Book (With Validation)")
        print("5. Return a Book")
        print("6. Exit")
        print("================================")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Book Title: ")
            author = input("Author: ")
            isbn = input("ISBN Code: ")
            qty = int(input("Total Quantity: "))
            b = Book(title, author, isbn, qty)
            b.add_book()
            
        elif choice == '2':
            Book.view_all_books()
            
        elif choice == '3':
            name = input("Member Name: ")
            email = input("Email Address: ")
            phone = input("Phone Number: ")
            m = Member(name, email, phone)
            m.register_member()
            
        elif choice == '4':
            book_id = int(input("Enter Book ID to Issue: "))
            member_id = int(input("Enter Member ID: "))
            Transaction.issue_book(book_id, member_id)
            
        elif choice == '5':
            tx_id = int(input("Enter Transaction ID to Return: "))
            Transaction.return_book(tx_id)
            
        elif choice == '6':
            print("Exiting Library System. Goodbye!")
            sys.exit()
        else:
            print("[INVALID] Please select a valid option from 1 to 6.")

if __name__ == "__main__":
    # Bootstraps tables and structure
    initialize_database()
    # Runs UI Loop
    main_dashboard()