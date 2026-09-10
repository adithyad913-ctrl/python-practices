languages=["python","java"]
fw=open("data_types\\file_operation\\languages.txt","w")
for l in languages:
    fw.write(l+"\n")
print("write completed...")