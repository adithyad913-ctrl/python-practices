# 1. Replace odd with "Odd"
numbers = [2,5,8,7,10]
result = ["odd" if num%2==0 else num for num in numbers]   # [2,"Odd",8,"Odd",10]
print(result)

# 2. Negative to 0
numbers = [-5,10,-3,20,15]
neg_to_zero = [n if n>=0 else 0 for n in numbers]   # [0,10,0,20,15]
print(neg_to_zero)

# 3. Pass or Fail (>=50 is Pass)
marks = [35,70,90,48,55]
result = ["Pass" if m>=50 else "Fail" for m in marks]   # ['Fail','Pass','Pass','Fail','Pass']


# 4. Replace empty string with "Unknown"
names = ["John","","Alice","","David"]
fixed_names = [n if n!="" else "Unknown" for n in names]   # ['John','Unknown','Alice','Unknown','David']
print(fixed_names)

# 5. Label numbers (>=100 High else Low)
numbers = [50,120,80,200,95]
labels = ["High" if n>=100 else "Low" for n in numbers]   # ['Low','High','Low','High','Low']
print(labels)

"""
input :["John","","Alice","","David"]

"""
names = ["John","","Alice","","David"]
result=["unkown"]