"""
This is an example of a program that has many problems.  Even though
this program runs and produces more or less the same result, it would
be very difficult to fix any bugs it might have.

Find all that is wrong here in terms of style. There are 5 errors. You
can see what they are in the program with comments. Try to locate them
yourself first.

"""

print ("Please enter two values...")
val1 = input("First => ")

def pretty_print(x, y, e):
    print ("Entropy({0:.2f},{1:.2f}) = {2:.2f}".format(float(x),float(y),e))

val2 = input("Second => ")

import math

def entropy(x):
    x = float(x)
    y = float(val2)
    p = x/(x+y)
    return -p * math.log(p) - (1-p) * math.log(1-p)

e = entropy(val1)

print ("Just finished computing entropy for", val1, "and", val2, "and found value", e)

x = pretty_print(val1, val2, e)
print (x)
