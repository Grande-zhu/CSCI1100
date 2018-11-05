height = 12.5
r = 3.4
pi = 3.14159
base_area = pi * r * r
volume = (1/3) * height * base_area
print("Volume of a cone with")
print("height", height)
print("radius", r)

'''
The following uses formatting for the string prior to passing to the
print function call.  This is correct and creates nicely formatted
output accurate to two decimal points.  It will be explained in
Lecture 4.
'''
print("is {:.2f} cubic units".format(volume))
