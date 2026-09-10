# 1. Squares
numbers = [1,2,3,4,5]
squares = [n**2 for n in numbers]   # [1,4,9,16,25]

# 2. Uppercase names
names = ["john","alice","bob","emma"]
upper_names = [n.upper() for n in names]   # ['JOHN','ALICE','BOB','EMMA']

# 3. Word lengths
words = ["apple","cat","elephant","bat"]
lengths = [len(w) for w in words]   # [5,3,8,3]

# 4. Multiply by 10
numbers = [2,5,8,10]
multiplied = [n*10 for n in numbers]   # [20,50,80,100]

# 5. Add 100 to salary
salary = [1200,1800,1500,2200]
new_salary = [s+100 for s in salary]   # [1300,1900,1600,2300]

 