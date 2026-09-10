from mysql import connector

class ExpenseListCreateReteieveUpdateDelete:
    def __init__(self,user=None,password=None):
        self.connection=connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="tripwise_db"

        )

        self.cursor=self.connection.cursor()



exp_instance=ExpenseListCreateReteieveUpdateDelete(user="root",password="Password@123")

print(exp_instance.connection)