def recursive_add_impl( L, i ):
    
    
    if i == len(L)-1:
        return L[i-1]
    else:
        L[i]=L[i]+L[i-1]
        return (recursive_add_impl(L,i+1))



def recursive_add(L):
    if len(L) == 0:
        return 0    
    else:
        return recursive_add_impl(L, 0)

if __name__ == "__main__":
    L1 = [ 5 ]
    print(recursive_add(L1))
    L2 = [ 24, 23.1, 12, 15, 1 ]
    print(recursive_add(L2))
    print(recursive_add([ ]))
