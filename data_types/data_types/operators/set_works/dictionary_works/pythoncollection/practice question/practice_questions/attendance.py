attendence=["p","p","a","a","o","o","h"]
count={}
for status in attendence:
    if status in count:
        count[status]+=1
    else:
        count[status]=1
print(count)