words=["hai","hello","hai","hai","hai"]

count={}

for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)