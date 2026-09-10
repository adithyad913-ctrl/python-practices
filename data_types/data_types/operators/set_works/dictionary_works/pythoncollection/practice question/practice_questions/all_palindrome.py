

words= ["madam","adam","tan","ant","racecar","malayalam"]

# palindrome_words=[]"madam","racecar","malayalam"
""" 
step set palindrome_words
"""


words=[ "madam","adam","tan","ant","racecar","malayalam"]

palindrome_list=[]

for w in words:
  if  w ==w[::-1]:
    palindrome_list.append(w)
print(palindrome_list)
       