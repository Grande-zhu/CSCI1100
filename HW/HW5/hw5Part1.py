"""
Minghao Zhu hw5 part1 10/30/2018
This program is to write two fuinctions to do a simple random test
print out slected directions and selected booleans based on given random seed
"""
import random

def move_trainer():
    '''
    A function to choose a direction randomly
    '''
    directions = ['N', 'E', 'S', 'W']
    direction = random.choice(directions) 
    value = random.random()
    print("Directions: ['N', 'E', 'S', 'W']")
    print("Selected {}, value {:.2f}".format(direction,value))
    
def throw_pokeball(num_false, num_true):
    '''
    A function to choose a Boolean from a list randomly
    '''    
    Booleans = [False]*num_false+[True]*num_true
    print("Booleans: {}".format(Booleans))
    choice = random.choice(Booleans)
    print("Selected {}".format(choice))


if __name__ == '__main__':
    #Taking user's input
    grid_size = int(input("Enter the integer grid size => "))
    print(grid_size)
    num_false = int(input("Enter the integer number of Falses => "))
    print(num_false)
    num_true = int(input("Enter the integer number of Trues => "))
    print(num_true)
    #set up random seed
    random_seed = 11 * grid_size
    random.seed ( random_seed )
    print("Setting seed to {}".format(random_seed))
    #run move_trainer and throw_pokeball 5 times
    i = 0
    while i < 5:
        move_trainer()
        i += 1
    i = 0
    while i < 5:
        throw_pokeball(num_false, num_true)
        i += 1