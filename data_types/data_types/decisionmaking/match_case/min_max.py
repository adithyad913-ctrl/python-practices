num1=int(input("enter number 1...."))
num2=int(input("enter number 2...."))
option=input("enter option min or max")
if option=="min":
    if num1<num2:
        print("minimun is",num1)

    else:
        print("min is",num2)
elif option=="max":
     if num1>num2:
        print("maximum is",num1)

     else:
         print("max is",num2)
else:
    print("invalid")

#this into match case
num1=int(input("enter number 1...."))
num2=int(input("enter number 2...."))
option=input("enter option min or max")
match option:
      case"min":
        if num1>num2:
            print("minimum is num1",num1)
        else:
            print("minimum is num2",num2)  

      case"max":
        if num1>num2:
            print("maximum is num1",num1)
        else:
            print("maximum is num2",num2)
      case _:print("invalid")









