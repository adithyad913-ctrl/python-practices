x1,y1=10,12
x2,y2=12,14
x3,y3=14,16
slop_one=(y2-y1)/(x2-x1)
slop_two=(y3-y2)/(x3-x2)
if slop_one==slop_two:
    print("points can form a straight line")
else:
    print("points can't form a straight line")