






"""

      *      =>6row col=>1 space 6
     * *     =>5row col=>2 space 5
    * * *    =>4row col=>3  space 4       
   * * * *   =>3row col=>4  space 3
  * * * * *  =>2row col=>5   space 2
 * * * * * * =>1row col=>6  space 1

"""

for r in range(6,0,-1):
 for s in range(1,r):
    print(" ",end="")
for col in range(1,(7-r)+1):
   print("* ",end="")
print()
