# models/member.py
from database import get_connection

class Member:
    def __init__(self, name, email, phone, member_id=None):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def register_member(self):
        """Registers a new library member."""
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO members (name, email, phone) VALUES (?, ?, ?)"
                cursor.execute(query, (self.name, self.email, self.phone))
                conn.commit()
                print(f"[SUCCESS] Member '{self.name}' registered successfully!")
            except Exception as e:
                print(f"[ERROR] Registration failed: {e}")
            finally:
                conn.close()