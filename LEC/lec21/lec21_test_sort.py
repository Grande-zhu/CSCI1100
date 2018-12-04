'''
Testing code for Computer Science 1, Lecture 21 on sorting. This
assumes that the sort functions are all in file lec21_sorts.py, each taking
one list as its only argument, and that their names are sel_sort
ins_sort merge_sort

All tests are based on random permutations of integers.

. In most of our tests, these permutations are completely random,
  meaning that a value is equally likely to end up anywhere in the
  list.

. In the final test we will explore the implications of working
  with lists that are "almost sorted" by only moving values a small
  distance from the correct location.  You can see that insertion sort
  is very fast in this case by removing the # char in front of
  generate_local_perm
'''

import lec21_sorts as sorts
import time
import random


def run_and_time(name, sort_fcn, v, known_v):
    '''
    Run the function passed as sort_fcn, timing its performance and
    double-checking if it correct.  The correctness check is probably
    not necessary.
    '''
    print("Testing " + name)
    t0 = time.time()
    sort_fcn(v)
    t1 = time.time()
    print("Time: {:.4f} seconds".format(t1-t0))
    # print("Is correct?", v==known_v
    print()



def generate_local_perm(v,max_shift):
    '''
    This function modifies a list so values are only a small amount
    out of order.  Each one  Generate a local permutation by randomly moving each
    value up to max_shift locations in the list.
    '''
    for i in range(len(v)):
        min_i = max(0,i-max_shift)
        max_i = min(len(v)-1, i+max_shift)
        new_i = random.randint( min_i, max_i )
        v[i], v[new_i] = v[new_i], v[i]


####################################################

if __name__ == '__main__':
    n = int(input("Enter the number of values ==> "))
    print("----------")
    print("Running on {:d} values".format(n))
    print("----------")

    v = list(range(n))
    v1 = v[:]
    random.shuffle(v1)
    # generate_local_perm(v1, 10)
    v2 = v1[:]
    v3 = v1[:]
    v4 = v1[:]

    run_and_time("merge sort", sorts.merge_sort, v3, v )   # passing functions as an arg to a fcn
    run_and_time("python sort", list.sort, v4, v )
    run_and_time("selection sort", sorts.sel_sort, v1, v )
    run_and_time("insertion sort", sorts.ins_sort, v2, v )

