 # 1. Names age >=18
people = [("John",18),("Alice",22),("Bob",16),("Emma",25)]
adults = [name for name,age in people if age>=18]   # ['John','Alice','Emma']
print(adults)

# 2. Double even numbers
numbers = [2,3,6,7,10]
double_even = [n*2 if n%2==0 else n for n in numbers]   # [4,3,12,7,20]
print(double_even)

# 3. Create usernames
names = ["John","Alice","Bob","Emma"]
emails = [n.lower()+"@gmail.com" for n in names]   # ['john@gmail.com','alice@gmail.com','bob@gmail.com','emma@gmail.com']
print(emails)

# 4. Add 18% GST
prices = [100,250,500,800]
gst_prices = [p*1.18 for p in prices]   # [118.0,295.0,590.0,944.0]
print(gst_prices)

# 5. Classify temperatures
temps = [18,22,35,28,15]
classified = ["Cold" if t<20 else "Warm" if t<30 else "Hot" for t in temps]
# ['Cold','Warm','Hot','Warm','Cold']
print(classified)

attendence=[1,-1,0,1,-1,1,-1,0,0]
#1=>p
#-1=>o
#0=>h
result=["p"if a==1 else "o" if a== -1 else"h" for a in attendence ]
print(result)
