# 1. Even numbers
numbers = [3,8,15,22,10,5]
evens = [n for n in numbers if n%2==0]   # [8,22,10]

# 2. Words longer than 5 letters
words = ["apple","watermelon","dog","elephant","cat"]
long_words = [w for w in words if len(w)>5]   # ['watermelon','elephant']

# 3. Positive numbers
numbers = [-10,15,-8,20,5,-2]
positives = [n for n in numbers if n>0]   # [15,20,5]

# 4. Names starting with 'A'
names = ["Alice","Bob","Andrew","Emma","Alex"]
a_names = [n for n in names if n.startswith("A")]   # ['Alice','Andrew','Alex']

# 5. Divisible by 5
numbers = [12,15,20,33,40,51]
div5 = [n for n in numbers if n%5==0]   # [15,20,40]
