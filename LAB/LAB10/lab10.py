def closest1(L1):
    '''
    closest1(x) returns tuple of closest numbers
    >>> closest1([3.5,4.2,7.8,1.8])
    (3.5, 4.2)
    >>> closest1([5])
    (None, None)
    >>> closest1([-3.5,4.2,-7.8,1.8])
    (4.2, 1.8)
    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (5.4, 4.3)
    '''    
    if len(L1)<2:
        return (None,None)
    cloest_1=9999
    difference_1=9999
    return_x=None
    return_y=None
    for i in range(len(L1)):
        for j in range(i+1,len(L1)):
            if L1[i]>L1[j]:
                difference_1=L1[i]-L1[j]
            elif L1[i]<L1[j]:
                difference_1=L1[j]-L1[i]
            if difference_1<cloest_1:
                cloest_1=difference_1
                return_x=L1[i]
                return_y=L1[j]
    return return_x,return_y

if __name__ == "__main__":
    L1 = [ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ]
    (x,y) = closest1(L1)
    print(x, y)