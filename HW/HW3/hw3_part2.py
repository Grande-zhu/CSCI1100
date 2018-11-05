"""
Hw3 Part2 Minghao Zhu
This program is to take user's input and then move pokemon based on user's input
direction, and the pokemen would meet other pokemen based on user's input of how
often they will meet. Out put the result in the end.
"""
def move_pokemon(coordinate, direction, steps):
    """
    a funtion to move pokemon by taking in coordinate, directions and steps
    made every time, then return the new coordinate
    """
    (row,column)=coordinate
    if(direction == "n"):
        row = row - steps;
    elif(direction == "s"):
        row = row + steps
    elif(direction == "e"):
        column = column + steps
    elif(direction == "w"):
        column = column - steps   
    
    row = min(150, row)
    row = max(0, row)
    column = min(150, column)
    column = max(0, column)
    
    return(row, column)

#Take user's input
turns = input("How many turns? => ")
print(turns)
name = input("What is the name of your pikachu? => ")
print(name)
often = input("How often do we see a Pokemon (turns)? => ")
print(often)

#convert to right units
turns = int(turns)
often = int(often)

#initialize variable
row = 75
column =75
turn = 1
record = []

#start simulation
print("\nStarting simulation, turn {} {} at ({}, {})".format(turn, name, row, column))
while (turns != 0):
    direction = input("What direction does {} walk? => ".format(name))
    print(direction)
    direction = direction.lower()
    #move pokemen
    coordinate = (row, column)
    coordinate = move_pokemon(coordinate, direction, 5)
    (row,column) = coordinate   
    #meet other pokemen if turns is divisible by often
    if (turn%often == 0):
        print("Turn {}, {} at ({}, {})".format(turn, name, row, column))
        type_pokemen = input("What type of pokemon do you meet (W)ater, (G)round? => ")
        print(type_pokemen)
        type_pokemen = type_pokemen.lower()
        #if it is g then lose, and go backward
        if(type_pokemen=="g"):
            coordinate = (row, column)
            coordinate = move_pokemon(coordinate, direction, -10)
            (row,column) = coordinate            
            print("{} runs away to ({}, {})".format(name,row,column))
            record.append('Lose')
        #if it is w then win, and go forward
        elif(type_pokemen=="w"):
            coordinate = (row, column)
            coordinate = move_pokemon(coordinate, direction, 1)
            (row,column) = coordinate            
            print("{} wins and moves to ({}, {})".format(name,row,column))
            record.append('Win') 
        else:
            record.append('No Pokemon')
    #incremrnt for turn        
    turn = turn + 1
    #check if end the loop
    if(turn>turns):
        break
#output the result    
print("{} ends up at ({}, {}), Record: {}".format(name,row,column,record))
    

