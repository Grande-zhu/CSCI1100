"""
Minghao Zhu hw8 12/08/2018
This program is to take in one files and usefour classes to do an simulation of 
maximun 100 steps. People in different universe may pick up a reward in its universe,
or meet aather individuals and lose his/her rewards, or even meet a portal and get 
to another universe.
"""

from Person import *
from Universe import *
import json
import math

class Rewards(object):
    '''
    Rewards class is to keep track of each rewards, and store its info in its
    attributes
    '''
    def __init__( self, name = "", universe = "", x = 0, y = 0, points = 0):
        #initialization
        self.name = name
        self.universe=universe
        self.x=x
        self.y=y
        self.owner=None
        self.points=points
        
    def __str__(self):
        #to string
        return("at (" + str(self.x) + "," + str(self.y) + ") for " +\
               str(self.points) +" points: "+self.name)
        
class Portals(object):
    '''
    Portals class is to keep track of each portals, and store its info in its
    attributes
    '''
    def __init__( self, fromx = 0, fromy = 0, to_universe = None, to_x = 0,\
                  to_y = 0, universe = None):
        #initialization
        self.fromx = fromx
        self.fromy = fromy
        self.to_universe = to_universe
        self.to_x = float(to_x)
        self.to_y = float(to_y )
        self.universe = universe
        
    def __str__(self):
        #to string
        return(self.universe + ":("+ str(self.fromx) + "," + str(self.fromy) + \
               ") -> " + self.to_universe + ":(" + "{:.0f}".format(self.to_x)+ \
               "," + "{:.0f}".format(self.to_y) + ")")

    
if __name__ == "__main__":
    #take in inputs file
    fname = input("Input file => ")
    print(fname)
    data = json.loads(open(fname).read())
    
    #read universe related information
    universes = []
    for i in range(len(data)):
        universe = (data[i])['universe_name']
        universe = Universe(None, None, universe)
        universes.append(universe)

    #read reward lated information
    rewards = []
    for j in range(len(data)):
        for i in range(len((data[j])['rewards'])):
            reward = (data[j])['rewards'][i]
            reward = Rewards(reward[3], (data[j])['universe_name'], reward[0], \
                             reward[1], reward[2])  
            rewards.append(reward)
    if rewards == []:
        rewards = None
        
    #read portals related information    
    portals = [] 
    for j in range(len(data)):
        for i in range(len((data[j])['portals'])):
            portal = (data[j])['portals'][i]
            portal = Portals(portal[0], portal[1], portal[2], portal[3], portal[4],\
                             (data[j])['universe_name'])
            portals.append(portal)
    if portals == []:
        portals = None
 
    #put reward and portal inside universes1       
    universes1 = []
    for universe in universes:
        rewards_num = 0
        portals_num = 0
        if rewards == None:
            rewards_num = 0
        else:
            for reward in rewards:
                if reward.universe == universe.name:
                    rewards_num = rewards_num + 1
        
        if portals == None:
            portals_num = 0
        else:
            for portal in portals:
                if portal.universe == universe.name:
                    portals_num = portals_num + 1
        universe_name = universe.name   
        universe = Universe(rewards_num, portals_num, universe_name)
        universes1.append(universe)

    #read person related information
    persons = []
    for j in range(len(data)):
        individuals = (data[j])['individuals']
        for i in range(len(individuals)):
            person = Person(individuals[i][0], individuals[i][1], \
                            (data[j])['universe_name'], individuals[i][2], \
                            individuals[i][3], individuals[i][4], individuals[i][5], \
                            (data[j])['universe_name'])
            persons.append(person)
        
    #output
    #print universe, rewards and portals
    print("All universes")
    print("----------------------------------------")
    for universe in universes1:
        print("Universe: " + str(universe))
        print("Rewards:")
        if rewards == None:
            print(rewards)
        else:
            for reward in rewards:
                if reward.universe == universe.name:
                    print(str(reward))
        print("Portals:")
        if portals == None:
            print(portals)
        else:
            for portal in portals:
                if portal.universe == universe.name:
                    print(str(portal))
        print("")
    
    #print individuals
    print("All individuals")
    print("----------------------------------------")
    for person in persons:
        print(str(person))
    print("")
    
    #start simulation    
    print("Start simulation")
    print("----------------------------------------") 
    for i in range(100):
        #check if the person is stopped before move
        for person in persons:
            person.check_stop()
            person.check_border()
        #do the moving and check if the person is stopped after move
        for person in persons:
            person.move()
            person.check_stop()
            person.check_border()
        #pick up rewards and check if the person is stopped after that    
        for person in persons:
            person.check_reward(rewards)
            print(person.name)
            print(person.reward_name)
            person.check_stop()
            person.check_border()
        #check if two person meet 
        Person.check_meet(rewards,persons)
        #check if the person go though a portal
        for person in persons:
            person.check_portal(portals)
        
    print("")
    print("----------------------------------------") 
    #find max step        
    max_step = 0
    for person in persons:
        if person.step > max_step:
            max_step = person.step
    if max_step < 100:
        print("Simulation stopped at step " + str(max_step))
        print("0 individuals still moving")
    else:
        person_still_moving = []
        for person in persons:
            if not person.isstop:
                person_still_moving.append(person)
        if len(person_still_moving) == 0:
            print("Simulation stopped at step 100")
            print("0 individuals still moving") 
        else:
            print("Simulation stopped at step 100")
            person_still_moving_name = str(person_still_moving[0].name )
            if len(person_still_moving) > 1:
                for i in range(1,len(person_still_moving)):
                    person_still_moving_name = person_still_moving_name+", " + \
                        person_still_moving[i].name
            print(str(len(person_still_moving)) + " individuals still moving: " \
                  + str(person_still_moving_name))
        
    #find winner
    print("Winners:")
    max_points = -10
    winner = []
    for person in persons:
        if person.points > max_points:
            max_points = person.points
    for person in persons:
        if person.points == max_points:
            winner.append(person)
        
    for i in range(len(winner)):
        print(str(winner[i]))
        print("Rewards:")
        if rewards != None:
            for reward in winner[i].reward_name:
                print("    "+reward)
        print("")
                
            
     
            
        

    
        
    