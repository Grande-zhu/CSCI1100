"""
HW2 Minghao Zhu
This prigram is to take user's input, calculate informations about the gum ball
machine, and output details about the machine and waste space filling the ball
"""
import math

def find_sphere_volume(radius):
    '''
    a function to caculate the sphere volume
    '''
    sphere_volume = (4/3) * math.pi * radius ** 3
    return sphere_volume

def find_cube_volume(side):
    '''
    a function to caculate the cube volume
    '''
    cube_volume = side ** 3
    return cube_volume

#Take user inputs fpr radius and weekly sale
radius = input("Enter the gum ball radius (in.) => ")
print(radius)
weekly_sale = input("Enter the weekly sales => ")
print(weekly_sale)
print()

#convert input to right unit
radius = float(radius)
weekly_sale = int(weekly_sale)

#Calculate some variables ready to be used
number_of_balls = math.ceil(weekly_sale*1.25)
side_length = math.ceil(math.pow(number_of_balls, 1/3))*(radius*2)
volume_of_the_cube = find_cube_volume(side_length)
volume_of_the_gum_balls = number_of_balls * find_sphere_volume(radius)
ball_num_edge = math.ceil(number_of_balls**(1/3)) 
actual_ball_num = ball_num_edge**3
extra_ball = actual_ball_num-number_of_balls
volume_of_actual_gum_balls = actual_ball_num * find_sphere_volume(radius)
waste_space_1 = volume_of_the_cube-volume_of_the_gum_balls
waste_space_2 = volume_of_the_cube-volume_of_actual_gum_balls

#Output the result
print("The machine needs to hold {} gum balls along each edge.".format(ball_num_edge))
print("Total edge length is {:.2f} inches.".format(side_length))
print("Target sales were {}, but the machine will hold {} extra gum balls.".format(number_of_balls, extra_ball))
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,\n\
or {:.2f} cubic inches if you fill up the machine.".format(waste_space_1, waste_space_2))

