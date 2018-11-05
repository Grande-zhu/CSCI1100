'''
Write a program to take input from users, deal with input datas, then output the results

HW1  Minghao Zhu 09/19/2018
'''
import math

#Take in all inputs
d1 = input("Enter the shortest distance from the lifeguard to water, d1 (yards) => ")
print(d1)
d2 = input("Enter the shortest distance from the swimmer to the shore, d2 (feet) => ")
print(d2)
h = input("Enter the lateral displacement between the lifeguard and the swimmer, h (yards) => ")
print(h)
vsand = input("Enter the lifeguard's running speed on sand, v_sand (MPH) => ")
print(vsand)
n = input("Enter the lifeguard's swimming slowdown factor, n => ")
print(n)
theta1 = input("Enter the direction of lifeguard's running on sand, theta1 (degrees) => ")
print(theta1)

#Convert to float and same unit
d1 = float(d1)*3
d2 = float(d2)
h = float(h)*3
vsand = float(vsand)*5280/3600
vswim = vsand/float(n)
x = math.tan(float(theta1)/180*math.pi)*d1
n = float(n)
theta1 = int(round(float(theta1),0))

#Calculate L1 and L2
L1 = math.sqrt(x**2+d1**2)
L2 = math.sqrt((h-x)**2+d2**2)
t = 1/vsand*(L1+n*L2)

print("If the lifeguard starts by running in the direction with theta1 of {:0d} degrees,".format(theta1))
print("they will reach the swimmer in {:.1f} seconds".format(t))



