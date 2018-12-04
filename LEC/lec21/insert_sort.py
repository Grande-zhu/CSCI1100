'''
Insertion sort of Lecture 21, exercise 1.
'''

def ins_sort( v ):
    '''
    The Insertion Sort algorithm
    '''
    for i in range(1,len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and v[j] > x:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x
        print("i = {}, j = {}, sorted = {}".format(i,j, v[:i+1]))

if __name__ == "__main__":
    v = [ 6.4, 18.5, 5.7, 18.8, 9.4 ]
    ins_sort(v)

