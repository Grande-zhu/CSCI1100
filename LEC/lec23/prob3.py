
    
def fib(n):
    l=[0,1]
    if n>1:
        for cnj in range(2,n+1):
            l.append(l[cnj-1]+l[cnj-2])
    return l[n]

    


if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
