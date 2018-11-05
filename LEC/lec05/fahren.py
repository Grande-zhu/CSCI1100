def convert2fahren(c):
    Fahrenheit = 32 + c * 1.8
    return  Fahrenheit

Celsius1 = 0
Celsius2 = 32
Celsius3 = 100

Fahrenheit1 = convert2fahren(Celsius1)
Fahrenheit2 = convert2fahren(Celsius2)
Fahrenheit3 = convert2fahren(Celsius3)

print(Celsius1,"->",Fahrenheit1)
print(Celsius2,"->",Fahrenheit2)
print(Celsius3,"->",Fahrenheit3)
