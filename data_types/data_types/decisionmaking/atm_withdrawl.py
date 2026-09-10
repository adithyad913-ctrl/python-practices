

dp_pin=1234
dp_amount=2500
pin=int(input("enter pin:"))
if pin==dp_pin:
    amt=int(input("enter amount:"))
    if amt<= dp_amount:
        print("widrawal sucessful")
    else:
        print("insufficient amount")
else:
    print("incorrect pin")
