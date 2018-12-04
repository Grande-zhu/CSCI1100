"""
Minghao Zhu hw7 part1 11/12/2018
This program is to take in three file, and compare words from one file to another 
file. Four methods,"drop","insert",swap","replace" are used.
Find the best 3 mathes and ouput.
"""
def ischange(word_f2):
    """
    A function to figure out if an alternate word is find from four kinds of method
    """
    if isdrop(word_f2)or(isswap(word_f2))or(isreplace(word_f2)>0)or\
       (isinsert(word_f2)>0):
        return True
    
def find_change(word_f2):
    """
    A function to figure out number of alternate words are find from 
    four kinds of method. Return the numbers in a tuple
    """
    change_num=0
    drop_num=0
    swap_num=0
    replace_num=0
    insert_num = 0
    if isdrop(word_f2):
        change_num=change_num+1
        drop_num=drop_num+1
    if isswap(word_f2):
        change_num=change_num+1
        swap_num=swap_num+1
    if isreplace(word_f2)>0:
        change_num=change_num+isreplace(word_f2)
        replace_num=replace_num+isreplace(word_f2)  
    if isreplace(word_f2)>0:
        change_num=change_num+isinsert(word_f2)
        replace_num=replace_num+isinsert(word_f2)
    
    return change_num,drop_num,swap_num,replace_num,insert_num


def isdrop(word_f2):
    """
    A function to check if there an alternate word can be found by "drop" menthod
    Consider two cases, the target letter is the last letter in the word or not
    """
    for i in range(len(word_f2)-1):
        word_drop=word_f2[:i]+word_f2[i+1:] 
        if word_drop in word_dict:
            return True
    word_drop_1=word_f2[:len(word_f2)-1]
    if word_drop_1 in word_dict:
            return True

def worddrop(word_f2):
    """
    A function to actually return new word by drop a letter from the word,
    where new words should appear in the dictionary file
    """
    word_drop_dict=dict()
    for i in range(len(word_f2)-1):
        word_drop=word_f2[:i]+word_f2[i+1:] 
        if word_drop in word_dict:
            word_drop_dict[word_drop]=word_dict[word_drop]
            
    word_drop_1=word_f2[:len(word_f2)-1]
    if word_drop_1 in word_dict:
            word_drop_dict[word_drop_1]=word_dict[word_drop_1]
    return word_drop_dict

def isswap(word_f2):
    """
    A function to check if there an alternate word can be found by "swap" menthod
    Consider two cases, the target letter is the last letter in the word or not
    """   
    for i in range(len(word_f2)-2):    
        word_swap=word_f2[:i]+word_f2[i+1]+word_f2[i]+word_f2[i+2:]
        if word_swap in word_dict:
            return True
    word_swap_1=word_f2[:len(word_f2)-2]+word_f2[len(word_f2)-1]+word_f2[len(word_f2)-2]
    if word_swap_1 in word_dict:
        return True    

def wordswap(word_f2):
    """
    A function to actually return new word by swap a letter from the word,
    where new words should appear in the dictionary file
    """   
    word_swap_dict=dict()
    for i in range(len(word_f2)-2):    
        word_swap=word_f2[:i]+word_f2[i+1]+word_f2[i]+word_f2[i+2:]
        if word_swap in word_dict:
            word_swap_dict[word_swap]=word_dict[word_swap]
            
    word_swap_1=word_f2[:len(word_f2)-2]+word_f2[len(word_f2)-1]+word_f2[len(word_f2)-2]
    if word_swap_1 in word_dict:
        word_swap_dict[word_swap_1]=word_dict[word_swap_1]
        
    return word_swap_dict

def isreplace(word_f2):
    """
    A function to check if there an alternate word can be found by "replace" method
    Consider two cases, the target letter is the last letter in the word or not
    return number of word can be changed from this method
    """   
    replace_num=0
    for i in range(len(word_f2)-1):                  
        for j in range(len(key_dict[word_f2[i]])):
            word_replace=word_f2[:i]+key_dict[word_f2[i]][j]+word_f2[i+1:]
            if word_replace in word_dict:   
                replace_num=replace_num+1

    if (word_f2[len(word_f2)-1]!=" "):
        for m in range(len(key_dict[word_f2[len(word_f2)-1]])):
            word_replace_1=word_f2[:len(word_f2)-1]+key_dict[word_f2[len(word_f2)-1]][m]
            if word_replace_1 in word_dict:   
                replace_num=replace_num+1            
                               
    return replace_num
    
def wordreplace(word_f2):
    """
    A function to actually return new word by replace a letter according to the
    key board file from the word, where new words should appear in the 
    dictionary file
    """  
    word_replace_dict=dict()
    for i in range(len(word_f2)-1): 
        for j in range(len(key_dict[word_f2[i]])):
            word_replace=word_f2[:i]+key_dict[word_f2[i]][j]+word_f2[i+1:]
            if word_replace in word_dict:
                word_replace_dict[word_replace]=word_dict[word_replace]
                
    if (word_f2[len(word_f2)-1]!=" "):
        for m in range(len(key_dict[word_f2[len(word_f2)-1]])):
            word_replace_1=word_f2[:len(word_f2)-1]+key_dict[word_f2[len(word_f2)-1]][m]
            if word_replace_1 in word_dict:
                word_replace_dict[word_replace_1]=word_dict[word_replace_1]
            
    return word_replace_dict

def isinsert(word_f2):
    """
    A function to check if there an alternate word can be found by "insert" method
    return number of word can be changed from this method
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']      

    insert_num=0  
    for i in range(len(word_f2)):                  
        for j in range(len(letters)):
            word_insert=word_f2[:i]+letters[j]+word_f2[i:]          
            if word_insert in word_dict:   
                insert_num = insert_num+1
    
    return insert_num
    
def wordinsert(word_f2):
    """
    A function to actually return new word by insert a letter to the word,
    where new words should appear in the dictionary file
    """  
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']      
    #method to gte the word if it "replace"
    word_insert_dict=dict()
    for i in range(len(word_f2)): 
        for j in range(len(letters)):
            word_insert=word_f2[:i]+letters[j]+word_f2[i:]
            if word_insert in word_dict:
                word_insert_dict[word_insert]=word_dict[word_insert]       
    return word_insert_dict

def ssort(s):
    """
    A function to do the sorting for dictionary
    """
    dic= sorted(s.items(), key=lambda d:d[1], reverse = True)
    i=1
    while i< len(dic):
        if(dic[i][1]==dic[i-1][1]):
            temp=(dic[i-1])
            dic[i-1]=dic[i]
            dic[i]=temp
            i+=1
        else:
            i+=1
    return dic    

if __name__ == "__main__":
    #Take user's input
    fname_1=input("Dictionary file => ")
    print(fname_1)
    fname_2=input("Input file => ")
    print(fname_2)
    fname_3=input("Keyboard file => ")
    print(fname_3)
    word_dict=dict()
    word_f1_list=[]
    for lines in open(fname_1):
        #get data from file 1
        word_f1=lines.strip("\n")
        word_f1_list=word_f1.split(",")
        word_dict[word_f1_list[0]]=word_f1_list[1]
     
    key_dict=dict()
    for letters in open(fname_3):
        #get data from file 3
        letter=letters.strip("\n")
        line1=letter.split(" ")
        key_dict[line1[0]]=line1
    
    sorted_dict=[]
    for lines in open(fname_2): 
        #for each words in file 2
        word_f2=lines.strip("\n")
        if(word_f2[len(word_f2)-1]==" "):
            word_f2=word_f2[:len(word_f2)-1]
        if (word_f2 in word_dict):
            #do print if it "found"
            print("{:<15} -> {:<15} :FOUND".format(word_f2,word_f2))
            
        elif(ischange(word_f2)):
            #create a dictionary to put all words in it
            all_change_dict=dict() 
            change_num,drop_num,swap_num,replace_num,insert_num = find_change(word_f2)
            #put words in though different method
            if(isdrop(word_f2)): 
                word_drop_dict= worddrop(word_f2)
                
                for key,values in word_drop_dict.items():
                    all_change_dict[key]=values
            
            if(isswap(word_f2)): 
                word_swap_dict= wordswap(word_f2)
                
                for key,values in word_swap_dict.items():
                    all_change_dict[key]=values
                
            if(isreplace(word_f2)>0):
                word_replace_dict= wordreplace(word_f2)
                for key,values in word_replace_dict.items():
                    all_change_dict[key]=values
    
            if(isinsert(word_f2)>0):
                word_insert_dict= wordinsert(word_f2)
                for key,values in word_insert_dict.items():
                    all_change_dict[key]=values  
            #call ssort to do the sorting   
            sorted_dict=ssort(all_change_dict)
    
            #do print if it match    
            if len(sorted_dict)==1:
                print("{:<15} -> {:<15} :MATCH 1".format(word_f2,sorted_dict[0][0]))
            elif(len(sorted_dict)==2):
                print("{:<15} -> {:<15} :MATCH 1".format(word_f2,sorted_dict[0][0]))
                print("{:<15} -> {:<15} :MATCH 2".format(word_f2,sorted_dict[1][0]))
            elif(len(sorted_dict)>=3):
                print("{:<15} -> {:<15} :MATCH 1".format(word_f2,sorted_dict[0][0]))
    
                print("{:<15} -> {:<15} :MATCH 2".format(word_f2,sorted_dict[1][0])) 
    
                print("{:<15} -> {:<15} :MATCH 3".format(word_f2,sorted_dict[2][0]))
        else: 
            #do print if it doesn't match
            print("{:<15} -> {:<15} :NO MATCH".format(word_f2,word_f2))