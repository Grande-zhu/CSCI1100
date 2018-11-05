#! /usr/bin/env pytho/n 
#-*- coding:utf-8 -*-
"""
This program is to simulate a dartboard. It askes user's input for building
that board, and then check if the board is valid by a function. Then, use
another function to get the score based on different conditions. Finally,
output the result.
"""
def is_board_valid(configuration):
    #a function to check if the board is valid
    for config in configuration:
        if (config <=0.0):
            #check if all configs are positive
            return False
    if configuration[2] < configuration[1]:
        #check if the outer bull’s eye is larger than inner bull’s eye
        return False
    if configuration[2] >= configuration[4]-configuration[3]:
        #check if the triple ring is outside of the outer bull’s eye
        return False
    if configuration[4] >= configuration[6]-configuration[5]:
        #check if the double ring is outside of the triple ring
        return False
    if configuration[0] < configuration[6]:
        #check if the double ring does not extend beyond the size of the board
        return False
    
    return True
    
def get_score(configuration, position):
       
    if position[0] < 0:
        #invalid if distance is negative
        points = 0
        return points
    elif position[0] < (configuration[1]/2):
        #if it is inside the inner bull's eye
        points = 50
        return points        
    elif position[0] == (configuration[1]/2):
        #if it is exactly at the boundary
        points = 0
        return points    
    elif position[0] < (configuration[2]/2):
        #if it is inside the outer bull's eye
        points = 25
        return points     
    elif position[0] == (configuration[2]/2):
        #if it is exactly at the boundary
        points = 0
        return points
    elif position[0] < (configuration[4]-configuration[3]):
        #if it is outside the triple ring but closer to the center
        bonus = 1
    elif position[0] == (configuration[4]-configuration[3]):
        #if it is exactly at the boundary
        points = 0
        return points 
    elif position[0] < (configuration[4]):
        #if it is inside the triple ring
        bonus = 3        
    elif position[0] == (configuration[4]):
        #if it is exactly at the boundary
        points = 0
        return points
    elif position[0] < (configuration[6]-configuration[5]):
        #if it is outside the triple ring but isn't closer to the center
        bonus = 1
    elif position[0] == (configuration[6]-configuration[5]):
        #if it is exactly at the boundary
        points = 0
        return points
    elif position[0] < (configuration[6]):
        #if it is inside the double ring
        bonus = 2
    else:#if it is exactly at the boundary or outside the board
        print(position[0])
        points = 0
        return points        
    
    #for conditions that inside the board and outside the outer bull's eye
    this_angle = position[1]
    if this_angle % 18 == 0:
        points = 0
        return points
        
    #change the angel to start with 1 and to the range of 0 - 360
    this_angle = this_angle - 81
    this_angle = this_angle % 360
    points = (20 - this_angle // 18) * bonus
    return points
         
#Take users input
print("Please enter dart board parameters below.")
board_diameter = input("Board diameter => ")
print(board_diameter)
inner_bulls_diameter = input("Inner bull's eye diameter => ")
print(inner_bulls_diameter)
outer_bulls_diameter = input("Outer bull's eye diameter => ")
print(outer_bulls_diameter)
triple_ring_width = input("Triple ring width => ")
print(triple_ring_width)
triple_ring_distance = input("Distance from the center to the outside edge of the triple ring => ")
print(triple_ring_distance)
double_ring_width = input("Double ring width => ")
print(double_ring_width)
double_ring_distance = input("Distance from the center to the outside edge of the double ring => ")
print(double_ring_distance)

distance = input("Enter the radial coordinate (r) of the point where the dart landed => ")
print(distance)
angle = input("Enter the angular coordinate (phi) of the point where the dart landed => ")
print(angle)

#convert to right units
board_diameter = float(board_diameter)                  #[0]
inner_bulls_diameter = float(inner_bulls_diameter)      #[1]
outer_bulls_diameter = float(outer_bulls_diameter)      #[2]
triple_ring_width = float(triple_ring_width)            #[3]
triple_ring_distance = float(triple_ring_distance)      #[4]
double_ring_width = float(double_ring_width)            #[5]
double_ring_distance = float(double_ring_distance)      #[6]

distance = float(distance)
angle = float(angle)

#put elements into the configuration
configuration = (board_diameter, inner_bulls_diameter, outer_bulls_diameter, \
                 triple_ring_width, triple_ring_distance, double_ring_width, \
                 double_ring_distance)
position = (distance, angle)

#check if the board is valid
valid = is_board_valid(configuration)
if valid:
    scores = get_score(configuration, position)
    print("This throw scored {:.0f}.".format(scores))
else:
    print("Invalid dartboard parameter(s) specified.")
