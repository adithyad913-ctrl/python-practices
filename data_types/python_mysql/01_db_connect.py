from mysql import connector

connection=connector.connect(
    user="root",
    password="Password@123",
    host="localhost"
)
print(connection)