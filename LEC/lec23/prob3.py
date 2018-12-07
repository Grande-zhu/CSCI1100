
def fib_add(n,i,fn,fn_1,fn_2):
    if n==i:
        return fn

    else:
        fn_2=fn_1
        fn_1=fn
        fn=fn_1+fn_2
        return fib_add(n,i+1,fn,fn_1,fn_2)
    
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib_add(n,2,1,1,0))

    


if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
