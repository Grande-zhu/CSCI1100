def closest1(L1):
    '''
    closest1(x) returns tuple of closest numbers
    >>> closest1([3.5,4.2,7.8,1.8])
    (3.5, 4.2)
    >>> closest1([5])
    (None, None)
    >>> closest1([-3.5,4.2,-7.8,1.8])
    (1.8, 4.2)
    >>> closest1([ 15.1, -12.1, 5.4, 11.8, 17.4, 4.3, 6.9 ])
    (4.3, 5.4)
    '''     
    L2 = sorted(L1)
    cloest_1=9999
    difference_1=9999
    return_x=None
    return_y=None
    for i in range(0,len(L2) - 1):
        difference_1=L2[i+1]-L2[i]
        if difference_1<cloest_1:
            cloest_1=difference_1
            return_x=L2[i]
            return_y=L2[i+1]
    return return_x,return_y
            
    
    
if __name__ == "__main__":
    L1 =[3.5,4.2,7.8,1.8]
    (x,y) = closest1(L1)
    print(x, y)
    print(L1)
    L3=[5]
    (x1,y1) = closest1(L3)
    print(x1, y1)
    print(L3)