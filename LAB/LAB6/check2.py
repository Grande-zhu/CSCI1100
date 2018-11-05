bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]


def ok_to_add(row,column,num):
    row_3x3 =(row-1)//3
    col_3x3 =(column-1)//3
    if bd[row-1][column-1]=='.':
        for i in range (9):
            if bd[row-1][i]==str(num):
                return  False
            if bd[i][column-1]==str(num):
                return  False
        for k in range(row_3x3*3,row_3x3*3+3):
            for w in range(col_3x3*3,col_3x3*3+3):
                if bd[k][w] == str(num):
                    return  False   
        
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
    
print_board(bd)
row = int(input("Please type in the row to add => "))
col = int(input("Please type in the column to add => "))    
num = int(input("Please type in the number to add =>  "))

if(ok_to_add(row,col,num)):
    print("This number can be added")
    bd[row-1][col-1]=num
    print_board(bd)
    
else:
    print("This number cannot be added")