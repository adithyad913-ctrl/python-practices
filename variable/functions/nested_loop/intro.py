"""
3 x 4 * pattern

* * * *
* * * *
* * * *


"""

for r in range(1,4):

    for c in range(1,5):

        print("*",end="\t")

    print()

"""
5x3@

@ @ @
@ @ @
@ @ @
@ @ @
@ @ @
"""
def five_by_three_pattern():
 for r in range(1,6):
  for c in range(1,4):
    print("@",end="\t")
  print()

five_by_three_pattern()
"""
*
* *
* * * 
* * * *
"""  
def left_half():
  for r in range(1,5):
    for c in range(1,r+1):
       print("*",end="\t")
    print() 

left_half() 
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

""" 
def left_half():
  for r in range(1,6):
    for c in range(1,r+1):
       print(r,end="\t")
    print() 
left_half()
"""
* * * * *
* * * *
* * *
* * 
*

"""
print("inverted")

for r in range(6,1,-1):
    for c in range(1,r):
      print("*",end="\t")
    print()

"""
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
"""





""""
5 5 5 5 5 
4 4 4 4 
3 3 3
2 2
1

"""
#row
#space
#colum
"""
     * =>row1 4space 1col
    ** =>row2 3space 2col
   *** =>row3 2space 3col
  **** =>row4 1space 4col
 ***** =>row5 0space 5col
"""
for r in range(5,0,-1):
  for sp in range(1,r):
    print(" ",end="")
  for col in range(1,(6-r)+1):
    print("*",end="")
  print()


  """"

      *
     **
    ***
   ****
  *****
 ******        
  
  """
for r in range(7,0,-1):
  for sp in range(1,r):
    print(" ",end="")
  for col in range(1,(7-r)+1):
    print("*",end="")
  print()


#pyramid
"""
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *                    
"""
for r in range(6,0,-1):
  for sp in range(1,r):
    print(" ",end="")
  for col in range(1,(7-r)+1):
    print("*",end=" ")
  print()