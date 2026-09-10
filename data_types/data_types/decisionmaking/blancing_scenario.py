

dp_pin=456

dp_balance=56000

pin=int(input("enter pin...."))

if dp_pin==pin:

    amount=int(input("enter amount..."))

    if amount <= dp_balance:

       print("transaction completed...")

    else:

     print("insufficient balance")
else:
       print("invalid pin")



