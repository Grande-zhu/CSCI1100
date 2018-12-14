def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1


def mult(m,n):
    if n==1:
        return m
    elif n==0:
        return 0
    else:
        return add(mult(m,n-1),m)
    
def power(m,n):
    if n==0:
        return 1
    elif n==1:
        return m
    else:
        return mult(power(m,n-1),m)
    
    

if __name__ == "__main__":
    print("\nadd(5,3)={}\n".format(add(5,3)))
    mul_1=int(input("multiply num 1 => "))
    mul_2=int(input("multiply num 2 => "))   
    print("{} * {} = {}\n".format(mul_1,mul_2,mult(mul_1,mul_2)))   
    pow_1=int(input("power num 1 => "))
    pow_2=int(input("power num 2 => "))
    print("{} ^ {} = {}".format(pow_1,pow_2,power(pow_1,pow_2)))