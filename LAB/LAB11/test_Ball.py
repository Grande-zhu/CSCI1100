'''
This is code to test your implement of the Ball class.  It is driven
by a Python module called doctest, which has been imported here.  doctest is
actually relative simple.

To understand it, start by looking at the comments under the function test_ball.
Lines starting with '>>>' correspond to commands that we can execute to test
our code. Lines following a '>>>' line that do not have '>>>' are expected
output. The function call doctest.testmod() causes doctest to the lines
marked '>>>' in sequence, looking for the expected output when it exists. The
verbose flag tells doctest to give more data on the tests including reporting 
when all tests pass. Once you get your code working, remove the verbose flag 
and see the difference in the output. Play around with the input and expected 
output to see the behavior of doctest when tests pass and fail.

Note that in our previous lab on testing, we embedded these tests directly 
in our module. We can do that in this case as well if we want.
'''

import doctest
from Ball import *

def test_ball():
    '''
    # test move 1
    >>> b = Ball(100,150,20,-15,10,'red')
    >>> b.move()
    >>> (x,y) = b.position()
    >>> x
    120
    >>> y
    135
    
    # test move 2
    >>> b = Ball(190,100,-10,18,25,'green')
    >>> b.move()
    >>> b.position()
    (180, 118)
    >>> b.get_color()
    'green'
        
    # test box 1
    >>> b = Ball(190,100,-10,18,25,'green')
    >>> b.bounding_box()
    (165, 75, 215, 125)
        
    # test inside 1
    >>> b = Ball(190,100,-10,18,25,'green')
    >>> b.some_inside(170,90)
    True
        
    # test inside 2
    b = Ball(190,100,-10,18,25,'green')
    >>> b.some_inside(164,190)
    False

    # test check_and_reverse
    b = Ball(190,100,-10,18,25,'green')
    >>> b.check_and_reverse(164,190)
    'x'
    
    # test check_and_reverse 2
    b = Ball(0,100,-10,18,25,'green')
    >>> b.check_and_reverse(100,190)
    'x'
    '''
    
if __name__ == "__main__":
    doctest.testmod(verbose=True)
