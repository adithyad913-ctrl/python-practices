from mysql import connector

class TicketCreateListRetriveUpdateDelete:
    def __init__(self, user=None, password=None):
        if user == None or password == None:
            raise Exception("username and password required")

        self.connection = connector.connect(
        user=user,
        password=password,
        host="localhost",
        database="customer_support_db"
      )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):

        db_cols=("customer_name","email","subject","description","priority","status","assigned_to")

        col_str = ",".join(db_cols)

        query=f"insert into support_ticket ({col_str}) values(%s,%s,%s,%s,%s,%s,%s)"

        values =list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print("ticket has been added.....")

        
ticket =TicketCreateListRetriveUpdateDelete(user="root",password="Password@123")

ticket.post(
             customer_name="arun",
             email="arundani1.com",
             subject="Payment deducted but order pending",
             description="I made the payment yesterday but my order is still showing pending.",
             category="payment",
             priority="high",
             status="open",
             assigned_to="open"
          )


