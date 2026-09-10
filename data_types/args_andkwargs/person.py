

def display_person(**kwargs):


    print(kwargs)
    

display_person(eid=101,name="hari",dept="hr",salary=25000,job_location="ekm",n_place="tsr")




""""

define a calculator function accept any number and operation

calculater(10,20,30,40,operation="+")return sum
calculater(10,20,30,operation="+")return product of numbers

"""

def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)
    
    elif kwargs.get("operation")=="*":

        result = 1

        for num in args:

            result = result * num

        return result

print(calculator(10,20,30,40,operation="+"))
#calculator(10,20,30,operation="*")