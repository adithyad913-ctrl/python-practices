#nested if program
#LOGIN SYSTEM
dp_username="adhi"
dp_password="1234"
username=input("enter username...")
if username==dp_username:
    password=int(input("enter password"))
    if password==dp_password:
        print("login system")
    else:
       print("invalid password")

else: 
    print("invalid username")