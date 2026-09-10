
arr=[1,2,3,4,6]
max_num=max(arr)
total=0
for num in range(1,max_num+1):
    total+= num
cur_arrr_sum=sum(arr)

difference=total-cur_arrr_sum

print(difference)
""""""

arr.sort()
for p in range(0,len(arr)-1):
    c=p+1
    difference=arr[c]-arr[p]
    if difference!=1:
        print(arr[p]+1,"is missing")
        break