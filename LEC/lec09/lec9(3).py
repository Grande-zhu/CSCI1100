total = 0
number = 0
x = 0
x_min = 1000000000000000000000000000
x_max = 0
end_found = False
list0=[]
while not end_found:
    x = int( input("Enter a value (0 to end): "))
    print(x)
    if x == 0:
        end_found = True
    else:
        total = total + x
        number = number +1
        if  x > x_max:
            x_max = x
        elif x< x_min:
            x_min = x
            
print("Min:",x_min)
print("Max:",x_max)
print("Avg:", round(total/number,1))
        
