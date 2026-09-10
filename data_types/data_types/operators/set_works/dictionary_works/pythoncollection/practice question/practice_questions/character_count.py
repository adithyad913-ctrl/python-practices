

word="python programming is simple"

count={}

for ch in word:
    if ch!=" ":
        if ch in count:
            count[ch]+= 1
        else:
            count[ch]=1
print(count)