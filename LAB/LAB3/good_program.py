"""
This is an example of a well structured and error free program.
You can use this as a template for your programs.

Have a single three quoted area in the top to explain what
your program does like we did above. Also have an author.

Author: Sibel Adali and Wes Turner
Version: 1
"""

## put all your import statements first, this way you can quickly
## find what modules are needed to run this code

import math


### next define all your functions, no variable or other code is
### present before function definitions.

def entropy(x, y):
    ### Entropy of two values, highest when x and y are equal.
    ### If either x or y is 0, a very small value is added to avoid log(0)
    ### Requires import math
    x = float(x)
    y = float(y)
    if x==0.0 and y==0.0:
        p = 0.5
    elif x==0.0 and y!=0.0:
        p = (x+1)/(x+y+1)
    elif x!=0.0 and y==0.0:
        p = x/(x+y+1)
    else:
        p = x/(x+y)
    return -p * math.log(p) - (1-p) * math.log(1-p)

## we can write complex print statements once in a function and use them
def pretty_print(x, y, e):
    print ("Entropy({0:.2f},{1:.2f}) = {2:.2f}".format(x,y,e))


### Now, your program starts. You will define variables and read input, etc.
### This part of your code may call the functions you defined above.

### Most programs will start with input. put all your input
### statements early. Of course, you might need to compute some and
### then use input again. That's ok.

print ("Please enter two values...")
val1 = input("First => ")
val1 = float(val1)

val2 = input("Second => ")
val2 = float(val2)

## Do some processing

## Calling a function that returns something. Always assign the result to a variable
e = entropy(val1, val2)

## Two types of output, printing and calling a function to print. Sometimes this
## will need to be embedded in the processing above.

print ("Just finished computing entropy for", val1, "and", val2, "and found value", e)

## Calling a function that returns nothing. No need to assign it to a variable
pretty_print(val1, val2, e)
