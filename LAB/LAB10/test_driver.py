'''
This is code to test your functions in this lab.  It is driven by a
Python module called 'doctest', which has been imported here.  

We assume the test program is called example_program.py, and we import 
all the functions in your program. When you develop your own lab10 
modules, make sure any other code in your lab10.py file is under the 

     if __name__ == "__main__":
line.

The doctest testing module is actually relative simple.

To understand it, start by looking at the code in the addone file. 
The code includes testing examples embedded in the 'addone(x)'
comments. When you run 'test_driver.py', it imports 'example_program' 
including the addone function definition and tests. It also imports 
'doctest' and then runs the 'doctest.testmod()' function on the 
addone module code. The 'testmod()' function searches out lines 
beginning with '>>>' in your function comments and uses those 
lines and the expected return values to test your code.

Now try a few more things. 

First, comment out the line 
'doctest.testmod(example_program)' and uncomment the line 
'doctest.testmod(example_program, verbose=True)' underneath it. 
This enables verbose mode and will print out something
even if your tests pass. 

Next restore the original line and change one of the 
return values encoded in the addtest() comments to a bad 
value and see how errors are normally reported. You will need
to restart your Python shell to force your changed file to be
reimported.

Now you are ready to write your code. Remove the addone()
function and replace it with the code for this lab including 
comments and test examples. Running this file will
now test the new code instead of our addone() function.
'''
import check2
import lab10
import example_program
import doctest

if __name__ == "__main__":
    #doctest.testmod(example_program)
    #doctest.testmod(example_program, verbose=True)
    doctest.testmod(check2, verbose=True)
    doctest.testmod(lab10, verbose=True)
    