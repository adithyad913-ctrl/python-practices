

angle_1=int(input("enter angle1"))

angle_2=int(input("enter angle2")) 

angle_3=int(input("enter angle3"))

if angle_1>0 and angle_2>0 and angle_3>0:

    if angle_1+angle_2+angle_3==180:
   
     print("it can be a triangle")

    else:

      print("it can't be triangle")
else:

   print("angle should be greater than zero")