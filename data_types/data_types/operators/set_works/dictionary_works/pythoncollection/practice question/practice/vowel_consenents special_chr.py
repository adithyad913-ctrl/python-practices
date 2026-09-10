



# create a different list that contain vowels,consonants,special_characters


"""
step create new empty lists vowels,consonants,specials
step: repeat for each char in text:
     
    
    chk if chr not in vowels and chr is alphabet then add char to consonantes
      chk if chr in "aeiou" then add char to vowels
     else add char to specials
     display vowels,conso,specials

"""

text="hello$world#"

vowels=[]

consonants=[]

specials=[]

for ch in text:
    if ch.lower() in"aeiou":
        vowels.append(ch)

