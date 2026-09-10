

for r in range(1,8):
    for c in range(1,8):
      if r==1 or c==7 or c==r or c==1 or r+c==8 or r==7:
         print("*",end="")
      else: 
        print("",end=" ")  
    print()    