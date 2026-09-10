import mysql.connector

class BookCRUD:
    def __init__(self):
        # Connect to MySQL database
        self.conn = mysql.connector.connect(
            host="localhost",       # Change if needed
            user="root",            # Your MySQL username
            password="password",    # Your MySQL password
            database="book_db"      # Database name
        )
        self.cursor = self.conn.cursor()

    # Insert
    def insert_book(self, title, author, year, genre, rating):
        sql = "INSERT INTO books (title, author, year, genre, rating) VALUES (%s, %s, %s, %s, %s)"
        values = (title, author, year, genre, rating)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("✅ Book inserted successfully.")

    # List all
    def list_books(self):
        self.cursor.execute("SELECT * FROM books")
        for row in self.cursor.fetchall():
            print(row)

    # Retrieve one
    def retrieve_book(self, book_id):
        sql = "SELECT * FROM books WHERE id = %s"
        self.cursor.execute(sql, (book_id,))
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("⚠️ No book found with id:", book_id)

    # Update
    def update_book(self, book_id, title=None, author=None, year=None, genre=None, rating=None):
        sql = "UPDATE books SET title=%s, author=%s, year=%s, genre=%s, rating=%s WHERE id=%s"
        values = (title, author, year, genre, rating, book_id)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print("🔄 Book updated successfully.")

    # Delete
    def delete_book(self, book_id):
        sql = "DELETE FROM books WHERE id = %s"
        self.cursor.execute(sql, (book_id,))
        self.conn.commit()
        print("🗑️ Book deleted successfully.")

    def __del__(self):
        self.cursor.close()
        self.conn.close()


# Example usage
if __name__ == "__main__":
    app = BookCRUD()

    # Insert
    app.insert_book("The Alchemist", "Paulo Coelho", 1988, "Fiction", 4.5)

    # List
    app.list_books()

    # Retrieve
    app.retrieve_book(1)

    # Update
    app.update_book(1, "The Alchemist (Updated)", "Paulo Coelho", 1988, "Fiction", 4.7)

    # Delete
    app.delete_book(1)
