


def add(*args):#args (10,20,30,40)
    return sum(args)

#add,fetch,remove,update
print(add(10,20,30,40))
print(add(10,20,30))

def product(*args):
    result=1
    for num in args:
        result=result*num

    return result

print(product(1,2,3,4))
print(product(5,6,7))
"""
define a fuction product that return product of all numbers
CRUD =>
C=> CREATE
R=>READ
U=>UPDATE
D=>DELETE
"""