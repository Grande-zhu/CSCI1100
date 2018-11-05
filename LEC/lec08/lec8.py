values = [ 14, 10, 8, 19, 7, 13 ]
int1=int(input("Enter a value: "))
print(int1)
values.append(int1)
int2=int(input("Enter another value: "))
print(int2)
values.insert(2,int2)
print(values[3],values[-1])
print("Difference: {}".format(max(values)-min(values)))
print("Average: {:.1f}".format(sum(values)/len(values)))
values=sorted(values)
median=(values[len(values)//2-1]+values[len(values)//2])/2
print("Median: {:.1f}".format(median))