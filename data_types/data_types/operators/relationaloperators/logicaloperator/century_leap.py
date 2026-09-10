

"""
scenario:year ending with two zero's and divisible by 400
"""
year=int(input("enter year.."))#200
is_leap=year%100==0 and year%400==0
print(is_leap)

