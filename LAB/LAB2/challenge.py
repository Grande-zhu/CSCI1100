word_1 = input("Please enter your first name: ") 
word_2 = input("Please enter your last name: ") +"!"
word_3 = "Hello,"

len_1=len(word_1)
len_2=len(word_2)
len_3=len(word_3)
len_4=max(len_1,len_2,len_3)

space_1l = (len_4 - len_1)//2
space_2l = (len_4 - len_2)//2
space_3l = (len_4 - len_3)//2

space_1r=len_4-space_1l-len_1
space_2r=len_4-space_2l-len_2
space_3r=len_4-space_3l-len_3

print("*" * (len_4+6))
print("*" * 2 + " " * space_3l,word_3 + " " * space_3r,"*" * 2)
print("*" * 2 + " " * space_1l,word_1 + " " * space_1r,"*" * 2)
print("*" * 2 + " " * space_2l,word_2 + " " * space_2r,"*" * 2)
print("*" * (len_4+6))


