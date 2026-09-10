

"""
two pair sum
arr=[2.3,4,5,11]
target=9
"""
arr=[2.3,4,5,11]
target=16
for n in arr:
    difference=target-n
    if difference in arr and difference!=n:
        print(difference,n)
        break
