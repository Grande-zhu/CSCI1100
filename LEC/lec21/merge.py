def merge(L1,L2):
    '''
    Merge the contents of two lists, each of which is already sorted
    into a single sorted list.
    '''
    i1 = 0
    i2 = 0
    L = []

    '''
    Repeated choose the smallest remaining item from the lists until one
    list has no more items that have not been merged.
    '''
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            L.append( L1[i1] )
            i1 += 1
        else:
            L.append( L2[i2] )
            i2 += 1
    L.extend(L1[i1:])   #  copy remaining items from L1, if any
    L.extend(L2[i2:])   #  copy remaining items from L2, if any
    L=set(L)
    L=list(L)
    L=sorted(L)
    return L

if __name__ == "__main__":
    L1 = [ 2, 7, 9, 12, 17, 18, 22, 25 ]
    L2 = [ 1, 5, 6, 8, 13, 14, 15, 18, 19, 23, 25 ]

    merged_L = merge(L1, L2)
    
    print(merged_L)
