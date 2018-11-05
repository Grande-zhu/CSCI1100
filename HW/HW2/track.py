'''
This is a short module to manage the available racetracks.

Author: Wesley Turner
Date: 9/26/2018
'''

def get_number_of_tracks():
    '''
    Return the number of different tracks provided by this module.
    '''
    return 3

def get_track(number):
    '''
    Given an integer between 1 and 3, return a specific race track configuration.
    For numbers less than 0 or greater than 3, return the empty string.
    '''
    if number == 1:
        track = '''
 E
B n
 d
 '''
    elif number == 2:
        track = '''
sTRaight
'''
    elif number == 3:
        track = '''
  sTRaiiGht
 D         B
n           e
e          N
 b        d
  thGiartS
'''
    else:
        track = ''
    return track

        