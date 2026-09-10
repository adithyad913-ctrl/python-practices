
#arr=[3,7,4,10,9,11,12,13]write a program to create a new  collection that contain
# only prime numbers

"""
step1 set prime_numbers as empty list
step2: repeat for each num in arr:
step:repeat for i from 2 to  num-1:  
   chk if num %i==0: then exit 

step: else append num to prime_ numbers
step: display prime_numbers

"""
arr=[3,7,4,10,9,11,12,13]

prime_numbers=[]

for num in arr:
    for i in range(2,num):
        if num%i==0:break
    else:
        prime_numbers.append(num)
print(prime_numbers)