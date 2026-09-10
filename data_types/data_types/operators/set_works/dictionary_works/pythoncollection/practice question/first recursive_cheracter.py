

text="AABCBAB"
unique_words=[]
for ch in text:

   if ch in unique_words:
      print(ch,"is the first recursive cherater")
      break
   else:
      unique_words.append(ch)


""""""
text="APCBAB"
char_count={}
for ch in text:
   if ch in char_count:
      print(ch,"is first recursive")
      break
   else:
      char_count[ch]=1
