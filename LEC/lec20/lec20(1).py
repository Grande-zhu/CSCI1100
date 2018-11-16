def linear_search( x, L ):
    if (x>L[0])and(x<L[len(L)-1]):
        for i in range (1,len(L)-1):
            if (L[i-1]<x)and(L[i]>=x):
                return i
    elif(x<L[0]):
        return (0)   
    elif(x>L[len(L)-1]):
        return (len(L))


if __name__ == "__main__":
    #  Get the name of the file containing data
    fname = input('Enter the name of the data file => ')
    print(fname)

    #  Open and read the data values
    in_file = open(fname,'r')
    values = []
    for line in in_file:
        v = float(line)
        values.append(v)

    #  Search for each value requested by the user until -1 is entered
    x = 0
    while x != -1:
        x = float(input("Enter a value to search for ==> "))
        print(x)
        if x != -1:
            loc = linear_search(x, values )
            print(loc)
