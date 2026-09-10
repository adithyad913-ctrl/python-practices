#---
gcd of two numbers num1,num2 # type: ignore
#set   gcd  as 1
#repeat for i from 1 to minimum of num1,num2
#   chk if num1%1==0 and num2%1==0 then
#    update gcd as  i
#display gcd
# ---


def gcd_of_two(num1,num2):
 gcd=1
 for i in range(1,min(num1,num2)+1):
     if  num1%i==0 and num2%i==0:
      gcd=i
 print(gcd)

 gcd_of_two(18,24)
 gcd_of_two(12,24)

 #logic
