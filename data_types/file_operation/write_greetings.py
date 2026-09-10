
wishes=["good morning","good afternoon","good evening","good night"]
fw =open("data_types\\file_operation\\greetings.txt","w")

for m in wishes:
    fw.write(m+"\n")