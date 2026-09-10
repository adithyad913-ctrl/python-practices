

#words=["run","car","madam","dam","tight"]
# create a new collection that contain revesed version of all words
#o/p= reversed_words=["nur","rac","madam","mad","thgit",...]
"""
step:set reversed_words as an empty list
step:repeat for each w in words:
step: set reversed as w[::-1]
step:append reversed to reversed_words
step: dipaly reversed_words
"""






words=["run","car","madam","dam","tight"]

revrsed_words=[]

for w in words:
    reverse=w[::-1] 
    revrsed_words.append(reverse)
print(revrsed_words)