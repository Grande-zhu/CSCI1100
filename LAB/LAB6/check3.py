from lab06_util import *

def ok_to_add(row,column,num,bd):
    row_3x3 =(row-1)//3
    col_3x3 =(column-1)//3
    if bd[row-1][column-1]=='.':
        for i in range (9):
            if bd[row-1][i]==str(num):
                return  False
            elif bd[i][column-1]==str(num):
                return  False
        for k in range(row_3x3*3,row_3x3*3+3):
            for w in range(col_3x3*3,col_3x3*3+3):
                if bd[k][w] == str(num):
                    return  False
    else:
        for i in range (9):
            if (bd[row-1][i]==num)and(i!=column-1):
                return  False
            elif (bd[i][column-1]==num) and(i!=row-1):
                return  False
        for k in range(row_3x3*3,row_3x3*3+3):
            for w in range(col_3x3*3,col_3x3*3+3):
                if bd[k][w] == str(num)and(k!=row-1)and(w!=column-1):
                    return  False        
        
    return True

def verify_board(board):
    i=0
    while i<8:
        j=0
        while j<8:
            if board[i][j]=='.':
                return False
            j+=1
        i+=1
    i=1
    while i<9:
        j=1
        while j<9:
            if not ok_to_add(i,j,board[i-1][j-1],board):
                return False
            j+=1
        i+=1
    return True

def print_board(bd):
    i=0
    while i<7:
        print("-------------------------------")
        for k in range(i,i+3):
            line=""
            j=0
            line= "|"+line
            while j<7:
                for w in range(j,j+3):
                    line=line+" "+str(bd[k][w])+" "
                line = line + "|"
                j = j+3
            print(line)
        i = i+3
    print("-------------------------------")  

ask_filename=input("Enter the filename: ")
print(ask_filename)

board=read_sudoku(ask_filename)   
while(not verify_board(board)):
    print("Unsolved")
    print_board(board)
    ask_row=input("Enter the row: ")
    print(ask_row)
    ask_row=int(ask_row)
    ask_column=input("Enter the column: ")
    print(ask_column)
    ask_column=int(ask_column)
    ask_number=input("Enter the number you want to add: ")
    print(ask_number)
    ask_number=int(ask_number)
    board[ask_row-1][ask_column-1]=ask_number
    
print("Solved!")
print_board(board)