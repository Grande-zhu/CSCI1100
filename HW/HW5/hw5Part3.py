"""
Minghao Zhu hw5 part3 10/30/2018
This program is to write some fuinctions to do a complete grid based on several
random simulations and then print out the grid and some stats afterward
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

def run_one_simulation( grid, prob ):
    '''
    runs the simulation and keeps track of the number of pokemon caught
    or missed based on prob
    return the number of turns for each simulations
    '''
    #initialize variables
    turn = 0
    num_true = 1
    num_false = 3
    row = len(grid)//2
    col = len(grid)//2
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
                col += 1
            elif direction == "S":
                row += 1
            elif direction == "W":
                col -= 1    
            #check if a pokemon can be caught based on probabality and that
            #random number            
            if seen < probability:
                catch = throw_pokeball(num_false, num_true)
                if(catch):
                    #increment num_true and grid[row][col]
                    num_true += 1
                    grid[row][col] += 1
                else:
                    grid[row][col] -= 1
            #check if reached boundry
            if (row <=0 ) or (col <=0 ) or (row >= len(grid)-1) or (col >= len(grid)-1):
                return turn
            #increment turn
            turn +=1   
    else:#leave in the first turn if trainer reached the boundry before any move
        return turn
        
def print_grid(grid):
    '''
    A function to print out the grid
    '''
    print()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print("{:5d}".format(grid[i][j]),end = '')
        print()

if __name__ == '__main__': 
    #Taking user's input
    grid_size = int(input("Enter the integer grid size => "))
    print(grid_size)
    probability = input("Enter a probability (0.0 - 1.0) => ")
    print(probability)    
    probability = float(probability)
    simulations = int(input("Enter the number of simulations to run => "))
    print(simulations)
    #setting up random seed
    seed_value = 10 * grid_size + grid_size
    random.seed(seed_value) 
    #initialize variables
    grid = []
    turn = []
    max_turn = 1
    min_turn = 1
    #build the grid
    for i in range(grid_size):
        grid.append( [0] * grid_size )
    #run the first simulation
    this_turn = run_one_simulation( grid, probability )
    turn.append(this_turn)
    #run the rest simulations
    for i in range(2,simulations+1):
        this_turn = run_one_simulation( grid, probability )
        #find max turn
        if this_turn > max(turn):
            max_turn = i
        #find min turn
        if this_turn < min(turn):
            min_turn = i        
        turn.append(this_turn)
    #print grid
    print_grid(grid)
    max_gird = 0
    min_gird = 0
    #find max and min num in grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > max_gird:
                max_gird = grid[i][j]
            if grid[i][j] < min_gird:
                min_gird = grid[i][j]              
    #out put stats        
    print("Average number of turns in a simulation was {:.2f}".format(sum(turn)/len(turn)))
    print("Maximum number of turns was {} in simulation {}".format(max(turn),max_turn))
    print("Minimum number of turns was {} in simulation {}".format(min(turn),min_turn))
    print("Best net missed pokemon versus caught pokemon is {}".format(max_gird))
    print("Worst net missed pokemon versus caught pokemon is {}".format(min_gird))   