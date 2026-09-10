import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="bookdb"
)

cursor = db.cursor()


# 1. INSERT BOOK
def insert_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    year = int(input("Enter published year: "))

    sql = """
    INSERT INTO books (title, author, price, published_year)
    VALUES (%s, %s, %s, %s)
    """

    values = (title, author, price, year)

    cursor.execute(sql, values)
    db.commit()

    print("Book inserted successfully.")


# 2. LIST ALL BOOKS
def list_books():
    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    print("\nID | Title | Author | Price | Year")
    print("----------------------------------------")

    for book in books:
        print(book)


# 3. RETRIEVE BOOK
def retrieve_book():
    book_id = int(input("Enter book ID: "))

    sql = "SELECT * FROM books WHERE id = %s"

    cursor.execute(sql, (book_id,))

    book = cursor.fetchone()

    if book:
        print("\nBook Details")
        print("ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Price:", book[3])
        print("Published Year:", book[4])
    else:
        print("Book not found.")


# 4. UPDATE BOOK
def update_book():
    book_id = int(input("Enter book ID to update: "))

    title = input("Enter new title: ")
    author = input("Enter new author: ")
    price = float(input("Enter new price: "))
    year = int(input("Enter new published year: "))

    sql = """
    UPDATE books
    SET title = %s,
        author = %s,
        price = %s,
        published_year = %s
    WHERE id = %s
    """

    values = (title, author, price, year, book_id)

    cursor.execute(sql, values)
    db.commit()

    if cursor.rowcount > 0:
        print("Book updated successfully.")
    else:
        print("Book not found.")


# 5. DELETE BOOK
def delete_book():
    book_id = int(input("Enter book ID to delete: "))

    sql = "DELETE FROM books WHERE id = %s"

    cursor.execute(sql, (book_id,))
    db.commit()

    if cursor.rowcount > 0:
        print("Book deleted successfully.")
    else:
        print("Book not found.")


# MENU
while True:

    print("\n===== BOOK CRUD =====")
    print("1. Insert Book")
    print("2. List Books")
    print("3. Retrieve Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        insert_book()

    elif choice == "2":
        list_books()

    elif choice == "3":
        retrieve_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")


# Close connection
cursor.close()
db.close()
