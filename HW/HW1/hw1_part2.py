'''
Write a program to use constitution class to adjust the text, find the index and
substring, and count the word appearence.

HW1  Minghao Zhu 09/19/2018
'''
import constitution 

#Get all text
all_text = constitution.get_all_text()

#Recover the original text
all_text = all_text.replace("#","\n\n")
all_text = all_text.replace("^","\n")
all_text = all_text.replace("@"," ")

#Output the text
num_line = all_text.count("\n")
num_character = len(all_text)
average_character = int((num_character-num_line)/num_line)
print("*"*average_character)
print(all_text)
print("*"*average_character)
num_article=all_text.count("\nArticle")
num_section=all_text.count("Section.")
print("\nThere are {} articles and {} sections in the United States Constitution"
      .format(num_article,num_section))

#find the begining and ending position of Article 1
beg_num=all_text.find("Article. I.")
end_num=all_text.find("Article. II.")-1

#Using substring to find the front and back position of the first and last word
article1_text=constitution.substring(all_text, beg_num, end_num-beg_num)
first_word_f=all_text.find("\n\n",beg_num)+2
first_word_b=all_text.find(" ",first_word_f)
last_word_f=all_text.rfind(" ",beg_num,end_num)+1
last_word_b=end_num-1

#Using substring to find out first and last letter, first and last word
first_letter=constitution.substring(all_text, first_word_f,1)
last_letter=constitution.substring(all_text, last_word_b-1,1)

first_word=constitution.substring(all_text, first_word_f, first_word_b-first_word_f)
last_word=constitution.substring(all_text, last_word_f, last_word_b-last_word_f)

#print out result
print('\nText of Article I starts at position {} (character \'{}\') with the word "{}"'
      .format(first_word_f,first_letter,first_word))
print('Text of Article I ends at position {} (character \'{}\') with the word "{}"'
      .format(last_word_b-1,last_letter,last_word))

#Read an input word and count number of appearence
input_word=input("\nEnter the word to count in the Constitution => ")
print(input_word)
all_text=all_text.upper()
appearence_num=all_text.count(input_word.upper())
print('Word "{}" appears {} times (without regard to case) in the text of the \
United States Constitution'.format(input_word.upper(),appearence_num))
