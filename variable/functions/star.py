"""
    * =>4space 1col row5 (6-row=6-5=1+1)(6-row)+1
   ** =>3space 2col row4 (6-row=6-4
  *** =>2space 3col row3
 **** =>1space 4col row2
***** =>0space 5col row1
"""
#row
#space
#colum
for r in range(5,0,-1):
    for sp in range(1, 6-r):
        print(" ",end="")
for col in range(1,(6-r)+1):
    print("*",end="")
print()


