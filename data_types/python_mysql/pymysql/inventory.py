import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",  
    database="inventory_db"
)
cursor = conn.cursor()

# CRUD Functions
def insert_product():
    sku = input("Enter SKU: ").strip()
    name = input("Enter Name: ").strip()
    category = input("Enter Category: ").strip()

    try:
        price = float(input("Enter Price: ").strip())
    except ValueError:
        print("❌ Invalid price. Please enter a number.")
        return

    try:
        stock = int(input("Enter Stock: ").strip())
    except ValueError:
        print("❌ Invalid stock. Please enter an integer.")
        return

    try:
        reorder_threshold = int(input("Enter Reorder Threshold: ").strip())
    except ValueError:
        print("❌ Invalid threshold. Please enter an integer.")
        return

    warehouse_zone = input("Enter Warehouse Zone: ").strip()

    query = """INSERT INTO product (sku, name, category, price, stock, reorder_threshold, warehouse_zone)
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (sku, name, category, price, stock, reorder_threshold, warehouse_zone)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Product inserted successfully!")


def list_products():
    cursor.execute("SELECT * FROM product")
    for row in cursor.fetchall():
        print(row)

def get_product():
    sku = input("Enter SKU: ")
    cursor.execute("SELECT * FROM product WHERE sku=%s", (sku,))
    product = cursor.fetchone()
    print(product if product else "❌ Product not found.")

def update_stock():
    sku = input("Enter SKU: ")
    new_stock = int(input("Enter new stock: "))
    cursor.execute("UPDATE product SET stock=%s WHERE sku=%s", (new_stock, sku))
    conn.commit()
    print("✅ Stock updated successfully!")

def delete_product():
    sku = input("Enter SKU: ")
    cursor.execute("DELETE FROM product WHERE sku=%s", (sku,))
    conn.commit()
    print("✅ Product deleted successfully!")

def filter_by_category():
    category = input("Enter category: ")
    cursor.execute("SELECT * FROM product WHERE category=%s", (category,))
    for row in cursor.fetchall():
        print(row)

def search_by_name():
    name = input("Enter product name keyword: ")
    cursor.execute("SELECT * FROM product WHERE name LIKE %s", ("%"+name+"%",))
    for row in cursor.fetchall():
        print(row)

def inventory_statistics():
    cursor.execute("SELECT COUNT(*), SUM(stock), SUM(price*stock) FROM product")
    stats = cursor.fetchone()
    print(f"📊 Total Products: {stats[0]}")
    print(f"📦 Total Stock Units: {stats[1]}")
    print(f"💰 Inventory Valuation: {stats[2]}")

# Menu
def menu():
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Insert Product")
        print("2. List All Products")
        print("3. Get Product Details")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Filter by Category")
        print("7. Search by Name")
        print("8. Inventory Statistics")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            insert_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            get_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            filter_by_category()
        elif choice == "7":
            search_by_name()
        elif choice == "8":
            inventory_statistics()
        elif choice == "9":
            print("👋 Exiting system...")
            break
        else:
            print("❌ Invalid choice, try again.")

menu()
