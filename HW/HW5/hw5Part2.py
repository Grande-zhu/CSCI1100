"""
Minghao Zhu hw5 part2 10/30/2018
This program is to write two fuinctions to do a simple random simulation
return slected directions and selected booleans based on given random seed
ouput result in main after simulations
"""
import random

def move_trainer():
    '''
    return a tuple of seleted direction and a random number between 0.0 and 1.0
    that determines if a pokemon is seen.
    '''
    directions = ['N', 'E', 'S', 'W']
    direction = random.choice(directions) 
    seen = random.random()
    return(direction,seen)   
    
    
def throw_pokeball(num_false, num_true):
    '''
    Taking in num_false and num_true  to build a catch list
    return a True or a False randomly chosen from the list.
    '''
    Booleans = [False]*num_false+[True]*num_true
    choice = random.choice(Booleans)
    return choice 

if __name__ == '__main__': 
    #Taking user's input
    grid_size = int(input("Enter the integer grid size => "))
    print(grid_size)
    probability = input("Enter a probability (0.0 - 1.0) => ")
    print(probability)
    probability = float(probability)
    #setting up random seed
    seed_value = 10 * grid_size + grid_size
    random.seed(seed_value)
    #initialize variables
    turn = 0
    num_true = 1
    num_false = 3
    num_seen = 0
    num_captured = 0
    row = grid_size//2
    column = grid_size//2 
    #start simluation
    if grid_size > 2:
        #ready to do the first turn if trainer did't reach the boundry
        turn = turn +1
        while True:
            #using move_trainer() to do a move and get direction and a random number
            (direction,seen) = move_trainer()
            if direction == "N":
                row -= 1
            elif direction == "E":
                column += 1
            elif direction == "S":
                row += 1
            elif direction == "W":
                column -= 1      
            #check if a pokemon can be caught based on probabality and that
            #random number
            if seen < probability:
                print("Saw a pokemon at turn {}, location ({}, {})".format(turn, row, column))
                catch = throw_pokeball(num_false, num_true)
                #increment num_seen
                num_seen += 1
                if(catch):
                    #increment num_true and num_captured
                    num_true += 1
                    num_captured += 1
                    print("Caught it!")
                else:
                    print("Missed ...")
            #check if reached boundry
            if (row <=0 ) or (column <=0 ) or (row >= grid_size-1) or (column >= grid_size-1):
                print("Trainer left the field at turn {}, location ({}, {}).".format(turn, row, column))
                print("{} pokemon were seen, {} of which were captured.".format(num_seen, num_captured))
                break
            #increment turn
            turn += 1
    else:#leave in the first turn if trainer reached the boundry before any move
        print("Trainer left the field at turn {}, location ({}, {}).".\
              format(turn, row, column))
        print("{} pokemon were seen, {} of which were captured.".\
              format(num_seen, num_captured))        