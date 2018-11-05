'''
Write a program to output inputt words and display a * diagram with input row 
and column numbers.

HW1  Minghao Zhu 09/19/2018
'''
#Take the input words,columns and rows
word=input("Word => ")
print(word)
columns=int(input("#columns => "))
print(columns)
row=int(input("#rows => "))
print(row)
print("Your word is:", word)
print("")

#Part (a)
print("(a)")
columns_1 = ("*** " * (columns-1) + "***" + "\n")
print(columns_1 * row)

#Part (b)
print("(b)")
columns_1 = ("*** " * (columns-1) + "***" + "\n")
midline = ("*** " * ((columns-1)//2) + "CS1" + " " + "*** " * 
           (((columns-1)//2)-1) + "***" + "\n")
print((columns_1 * ((row-1)//2)) + midline + (columns_1 * ((row-1)//2)))

#Part (c)
#Set up for first,mid and last line, then fill in normal lines
print('(c)')
mid_number=int((row-1)/2)
left_column=int((columns-1)/2)
#since we don't need a space after each line, meaning if the mid lines ends with
#"|" or"\" or"/" would be a space less then we having the line ends with"*"
#So I use max and min to make sure thee flag number is between 0 and 1
#Since we are not allowed to use any if, for or while, I use a list and sort to
#determine if the line ends with "/","|","\" or ends with "*"
right_column=max(int((columns-1)/2)-1,0)
list_1=[0,right_column]
list_1=sorted(list_1,reverse=True)
flag_num=min(list_1[0],1)

row_1='*** '*left_column+' ^ '+' ***'*(left_column)+"\n"
row_2='*** '*(left_column-1)+' / '+' *** '+' \\'+'  ***'*(flag_num)+' ***'*(right_column-1)+"\n"
row_3=('*** '*(left_column-1)+' | '+' *** '+' |'+'  ***'*(flag_num)+' ***'*(right_column-1)+"\n")*((mid_number-2))
row_mid=('*** '*(left_column-1)+' |'+'  CS1 '+' |'+'  ***'*(flag_num)+' ***'*(right_column-1)+"\n")
row__2='*** '*(left_column-1)+' \ '+' *** '+' /'+'  ***'*(flag_num)+' ***'*(right_column-1)+"\n"
row__1='*** '*left_column+' v '+' ***'*left_column
print(row_1+row_2+row_3+row_mid+row_3+row__2+row__1)

