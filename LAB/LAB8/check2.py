def get_words(str1):
    word=[]
    word_count = 0
    word_set=set()
    str2=str1.replace("."," ")
    str3=str2.replace(","," ")
    str4=str3.replace("("," ")
    str5=str4.replace(")"," ")
    str6=str5.replace('"'," ")
    str7=str6.lower()
    word=str7.split(" ")

    for i in range(len(word)):
        if (len(word[i])>3)and(word[i].isalpha()):
            word_count = word_count+1
            word_set.add(word[i])

    return(word_set)

fnames_1=input("please type in the first filename=> ")
fnames_2=input("please type in the second filename=> ")
fname_1 = fnames_1+".txt"
fname_2 = fnames_2+".txt"
line1=[]
line2=[]
for line in open(fname_1):
    line1=line.split("|")
    word_get_1=set()
    word_get_1=get_words(line1[1])
for line in open(fname_2):
    line2=line.split("|")
    word_get_2=set()
    word_get_2=get_words(line2[1])
print("Comparing clubs {} and {}:".format(fnames_1,fnames_2))

common_set=set()
common_set=word_get_1.intersection(word_get_2)
print("same words:" ,common_set)
unique_1=word_get_1.difference(word_get_2)
unique_2=word_get_2.difference(word_get_1)
print("Unique to {}:".format(fnames_1),unique_1)
print("\nUnique to {}:".format(fnames_2),unique_2)