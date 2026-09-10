from
secret_number=7
for attempt in range(1,7):
    number=int(input("guess the number:"))
    if number==secret_number:
        print("congratulations😘")
    if attempt >=5:
        print("bad luck 🤦‍♀️")

