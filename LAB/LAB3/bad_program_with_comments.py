"""
This is an example of a program that has many problems.  Even though
this program runs and produces more or less the same result, it would
be very difficult to fix and bugs it might have.

Here are the comments of what is wrong in the following program. We
put the comment at the exact point while reading this program that we
discovered a problem.

"""

print ("Please enter two values...")
val1 = input("First => ")

## Problem 1:
## This function definition should come before any other program
## statement like print, input, etc. 

def pretty_print(x, y, e):
    print ("Entropy({0:.2f},{1:.2f}) = {2:.2f}".format(float(x),float(y),e))

val2 = input("Second => ")

## Problem 2:
## import should come before function definition and any other code.
import math

## Problem 1 repeated:
## This function definition should have come before the input
## statements and any variable declarations.



## This entropy function will fail for either x or y is zero, but I
## did not include that one as a problem and concentrated on other
## problems. But you can give yourself bonus kudos if you caught that
## extra one.

def entropy(x):
    x = float(x)
    ## Problem 3 (VERY SERIOUS):
    ## val2 is not a parameter of this function and is referencing a global variable
    ## This is not allowed in many programming languages and is the main cause of
    ## programs that are hard to read and hard to debug. Do not do this.
    y = float(val2)
    p = x/(x+y)
    return -p * math.log(p) - (1-p) * math.log(1-p)

## Problem 4 (minor but still): The values from input are read as
## strings and are converted to float in multiple places. This is
## unnecessary repetition and you must remember to do this every
## time. Instead, why not just convert them to float once, e.g. val1 =
## float(val1)

e = entropy(val1)

print ("Just finished computing entropy for", val1, "and", val2, "and found value", e)

## Problem 5 (VERY SERIOUS):
## You are using a function that returns nothing, so you must not assign it to a variable
## More importantly you must not print that value, because x's value is nothing (since
## function returns nothing. So, print(x) will print None. print(pretty_print(val1, val2, e))
## is equally as problematic.

x = pretty_print(val1, val2, e)
print (x)
