fr=open("data_types\\file_operation\\news.txt","r",encoding="utf-8")
words=[]
for line in fr:

    line=line.rstrip("\n")

    for w in line.split(" "):
        words.append(w)
word_count={w:words.count(w)for w in words}
print(words)
print(word_count)
