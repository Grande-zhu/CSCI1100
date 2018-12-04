def get_words(str1):
    word=[]
    word_count = 0
    word_set=set()
    str1=str1.replace("."," ")
    str1=str1.replace(","," ")
    str1=str1.replace("("," ")
    str1=str1.replace(")"," ")
    str1=str1.replace('"'," ")
    str1=str1.lower()
    words=str1.split(" ")
    for i in range(len(words)):
        if (len(words[i])>=4)and(words[i].isalpha()):
            word_count = word_count+1
            word_set.add(words[i])

    print("File {} {}words".format(fname,word_count)) 
    print(word_set)

fname=input("please type in the filename=> ")
line1=[]
for line in open(fname):
    line1=line.split("|")
    get_words(line1[1])