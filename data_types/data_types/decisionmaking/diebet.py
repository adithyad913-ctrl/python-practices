sugar_level=int(input("enter sugar level"))
if sugar_level>300:
    print("vry high")

elif sugar_level>140 and sugar_level<=200:
    print("high")
elif sugar_level>90 and sugar_level<=140:
    print("normal")
elif sugar_level>80 and sugar_level<=90:
    print("low")
else:
    print("very low")