"""
HW2 Minghao Zhu
This program is to use function from track, and then take user's input 
to select track and caculate speed and than output result base on it.
"""
import track

def calculate_curve(track, speed):
    '''
    a function to caculte speed of curve track
    
    '''
    bend=track.count("b")+track_lower.count("e")+track_lower.count("n")+track_lower.count("d")
    distance = bend * 0.25
    time = distance / speed
    
    return (distance,time)
    
def calculate_straight(track, speed):
    '''
    a function to caculte speed of straight track
    '''   
    straight=track_lower.count("s")+track_lower.count("t")+track_lower.count("r")+\
        track_lower.count("a")+track_lower.count("i")+track_lower.count("g")+\
        track_lower.count("h")    
    distance = straight * 0.25
    time = distance / speed
    
    return (distance,time)

#Use function from track.py      
track_range= track.get_number_of_tracks()

#Take user's input  
track_num=input("Select a track between 1 and {} => ".format(track_range))
print(track_num)
speed_curve=input("Speed on curved segments (MPH) => ")
print(speed_curve)
speed_straight=input("Speed on straight segments (MPH) => ")
print(speed_straight)

#Convert to right unit
speed_curve = float(speed_curve)
speed_straight = float(speed_straight)
track_num = int(track_num)

#Use function from track.py
track = track.get_track(track_num)

#caculate length of each track
track_lower = track.lower()

#use writen functions to caculate distance and time
curve_track = calculate_curve(track_lower, speed_curve)
straight_track = calculate_straight(track_lower, speed_straight)

#calculate total length and time, and average speed
total_length=curve_track[0]+straight_track[0]
total_time=curve_track[1]+straight_track[1]
total_time_second=total_time*3600
avg_speed = total_length/total_time

#output result based on avg speed
if(avg_speed<60):
    critique= "Kind of slow."
elif(avg_speed>=120):
    critique= "Wow, quite the car!"
else:
    critique= "Getting there."

print("\nTrack:")
print(track)

print("is {:.2f} miles long. You raced it in {:.2f} seconds at an average speed of {:.2f} MPH\n\
{}".format(total_length,total_time_second,avg_speed,critique))