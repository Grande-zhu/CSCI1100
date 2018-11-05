first = input("Enter the first number: ")
print(first)

second= input("Enter the second number: ")
print(second)
first=float(first)
second=float(second)
if (first > 10) and (second> 10):
    print("Both are above 10.")
elif (first < 10) and (second < 10):
    print("Both are below 10.")

average = round((first + second)/2,2)
print("Average is", average) 