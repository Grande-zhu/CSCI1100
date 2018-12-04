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
fname_2="allclubs.txt"
fname_1 = fnames_1+".txt"
line1=[]
line2=[]
total=[]
for line in open(fname_1,encoding="utf8"):
    line1=line.split("|")
    club_name_1=line1[0]
    word_get_1=set()
    word_get_1=get_words(line1[1])
for line in open(fname_2):
    line2=line.split("|")
    club_name_2=line2[0]
    word_get_2=set()
    word_get_2=get_words(line2[1])
    
    if not(club_name_1==club_name_2):
        common_set=set()
        common_set=word_get_1.intersection(word_get_2)
        common_num =len(common_set) 
        total.append((common_num,club_name_2))
total.sort(reverse=True)
top=[]
for i in range(5):
    top.append(total[i])
print(top)
