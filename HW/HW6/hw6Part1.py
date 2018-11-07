"""
Minghao Zhu hw6 part1 11/6/2018
This program is to take in two file, and compare words from one file to another 
file. Three functions are written to check if "drop,swap,replace"method is used
Another three functions are written to actually select the right word that fit most
Output result in the end
"""
def isdrop(word_f2):
    """
    A function to check if there an alternate word can be found by "drop" menthod
    Consider two cases, the target letter is the last letter in the word or not
    """
    for i in range(len(word_f2) - 1):
        word_drop = word_f2[:i] + word_f2[i + 1:] 
        if word_drop in words_set:
            return True
    word_drop_1 = word_f2[:len(word_f2) - 1]
    if word_drop_1 in words_set:
            return True

def worddrop(word_f2):
    """
    A function to actually return new word by drop a letter from the word,
    where new words should appear in the dictionary file
    """
    drop_set = set()
    for i in range(len(word_f2)-1):
        word_drop = word_f2[:i] + word_f2[i + 1:] 
        if word_drop in words_set:
            drop_set.add(word_drop)
    word_drop_1 = word_f2[:len(word_f2) - 1]
    if word_drop_1 in words_set:
        drop_set.add(word_drop_1)
    #return the first letter in the sorted set    
    return sorted(drop_set)[0]
        
def isswap(word_f2):
    """
    A function to check if there an alternate word can be found by "swap" menthod
    Consider two cases, the target letter is the last letter in the word or not
    """   
    for i in range(len(word_f2)-2):    
        word_swap = word_f2[:i] + word_f2[i+1] + word_f2[i] + word_f2[i+2:]
        if word_swap in words_set:
            return True
    word_swap_1 = word_f2[:len(word_f2)-2] + word_f2[len(word_f2)-1] + word_f2[len(word_f2)-2]
    if word_swap_1 in words_set:
        return True

def wordswap(word_f2):
    """
    A function to actually return new word by swap a letter from the word,
    where new words should appear in the dictionary file
    """    
    swap_set = set()
    for i in range(len(word_f2)-2):    
        word_swap = word_f2[:i] + word_f2[i+1] + word_f2[i] + word_f2[i+2:]
        if word_swap in words_set:
            swap_set.add(word_swap)
    word_swap_1 = word_f2[:len(word_f2)-2] + word_f2[len(word_f2)-1] + word_f2[len(word_f2)-2]
    if word_swap_1 in words_set:
        swap_set.add(word_swap_1)
    #return the first letter in the sorted set 
    return sorted(swap_set)[0]

def isreplace(word_f2):
    """
    A function to check if there an alternate word can be found by "replace" menthod
    Consider two cases, the target letter is the last letter in the word or not
    """   
    for i in range(len(word_f2)-1):                  
        for j in range(len(letters)):
            word_replace = word_f2[:i] + letters[j] + word_f2[i+1:]
            if word_replace in words_set:   
                return True
    for j in range(len(letters)): 
        word_replace_1 = word_f2[:len(word_f2) - 1] + letters[j]
        if word_replace_1 in words_set:
            return True        
    
def wordreplace(word_f2):
    """
    A function to actually return new word by replace a letter to a~z from the word,
    where new words should appear in the dictionary file
    """  
    replace_set = set()
    for i in range(len(word_f2) - 1):                  
        for j in range(len(letters)):       
            word_replace = word_f2[:i] + letters[j] + word_f2[i + 1:]
            if word_replace in words_set:   
                replace_set.add(word_replace)
    for j in range(len(letters)): 
        word_replace_1 = word_f2[:len(word_f2)-1]+letters[j]
        if word_replace_1 in words_set:
            replace_set.add(word_replace_1)        
    #return the first letter in the sorted set
    return sorted(replace_set)[0]

if __name__ == '__main__':
    #Taking in two file names
    fname_1 = input("Dictionary file => ")
    print(fname_1)
    fname_2 = input("Input file => ")
    print(fname_2)
    #initize variable
    words_set = set()
    #define letters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']
    #read in files
    for lines in open(fname_1):
        word_f1 = lines.strip("\n")
        words_set.add(word_f1)
    #start comparing words
    for lines in open(fname_2):
        word_f2 = lines.strip("\n")
        #if word appeared in dictionary file, just print found
        if(word_f2 in words_set):
            print("{:<15} -> {:<15} :FOUND".format(word_f2, word_f2))
        #if word can be found though "drop", call the function to get the new word     
        elif(isdrop(word_f2)):
            word_drop = worddrop(word_f2)
            print("{:<15} -> {:<15} :DROP".format(word_f2, word_drop))
        #if word can be found though "swap", call the function to get the new word
        elif(isswap(word_f2)):
            word_swap = wordswap(word_f2)
            print("{:<15} -> {:<15} :SWAP".format(word_f2, word_swap))
        #if word can be found though "replace", call the function to get the new word
        elif(isreplace(word_f2)):
            word_replace = wordreplace(word_f2)
            print("{:<15} -> {:<15} :REPLACE".format(word_f2, word_replace))
        #if word can not match though any processes, just print no match    
        else:           
            print("{:<15} -> {:<15} :NO MATCH".format(word_f2, word_f2))