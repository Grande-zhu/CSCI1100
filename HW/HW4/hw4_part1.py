"""
Minghao Zhu hw4 part1 10/17/2018
This program is to write two fuinctions, together with imported
lifeguard.get_response_time(beach), to get optimal time and stats of
rescued, drowned could save and drowned could not save.
"""
import math
import lifeguard

def get_optimal(beach,interval):
    '''
    This function is to get optimal time by taking in beach and interval,
    which are two tuples containing information for get response time, and
    for time interval changed. Then return a a list containing best time,
    angle and difference with orginal t
    '''
    #from imported lifeguard, call get_response_time to get t
    t = lifeguard.get_response_time(beach)
    #initialize
    angle = interval[0]
    Optimal = [t, beach[5], 0]
    t_min = 99999999
    piece = (interval[1] - interval[0]) / (interval[2] - 1)
    #use a flag to determine make sure the loop exit correctly
    flag1 = 0
    
    #use a loop to find the best time
    while(interval[1] >= angle):
        new_beach = (beach[0], beach[1], beach[2], beach[3], beach[4], angle)
        #from imported lifeguard, call get_response_time to get new t
        t_new = lifeguard.get_response_time(new_beach)
        if(t_new < t_min):
            t_min = t_new
            #update the list after a better time is found
            Optimal = [t_new, angle, t - t_new]
        angle = angle + piece
        if(flag1 == 1):
            break
        if(angle > interval[1]):
            angle = interval[1] 
            flag1 = 1        
    #return a a list containing best time,angle and difference with orginal t
    return Optimal
    
def get_stats(beaches,interval):
    '''
    This function is to get stats of rescued, drowned could save and drowned could not save.
    '''    
    #initialize
    rescued = 0
    drowned_could_save = 0
    drowned_could_not_save = 0
    #use a loop to determine the stats for each case
    for beach in beaches:
        optimal = get_optimal(beach,interval)
        if(optimal[0]+optimal[2])<120:
            rescued += 1
        elif optimal[0]<120:
            drowned_could_save += 1
        else:
            drowned_could_not_save += 1
    #put the result into a tuple and then return it   
    statistics = (rescued,drowned_could_save,drowned_could_not_save)
    return statistics

if __name__ == "__main__": 
    #I love CS!
    print("I love CS!")