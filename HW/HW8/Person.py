'''
Minghao Zhu hw8 12/08/2018
Person class is class to store person related infomations
its name, radius, home universe, coordinates, speed, current_universe, reward
points and boundry
Also, it got five functions to check if the person stop moving, reach the boundry
pick up a reward, meet someone else or go though a portal
'''

import math

class Person(object):
    def __init__( self, name = "", radius = 0, home_universe = "", x = 0.0, y = 0.0,\
                  dx = 0.0, dy = 0.0, current_universe = ""):
        #initialization
        self.x = float(x)
        self.y = float(y)
        self.dx = float(dx)
        self.dy = float(dy)
        self.r = radius
        self.home_universe = home_universe
        self.current_universe = current_universe
        self.rewards = 0
        self.name = name
        self.points = 0
        self.step = 0
        self.isstop = False 
        self.maxx = 1000
        self.maxy = 1000
        self.reward_name = []
        
    def move(self):
        #move
        if not self.isstop:
            self.x = self.x+self.dx
            self.y = self.y+self.dy
            self.step = self.step + 1

    def check_stop(self):
        #check if it stop
        if not self.isstop:
            if abs(self.dx) < 10 or abs(self.dy) < 10:
                print(self.name + " stopped at simulation step " + str(self.step) +\
                      " at location (" + str(round(self.x,1)) + "," + str(round(self.y,1)) + ")")
                print("")
                self.isstop = True
                  
    def check_border(self):
        #check if it reaches the border
        if not self.isstop:
            if self.x >= self.maxx or self.x <= 0 or self.y >= self.maxy or self.y <= 0:
                print(self.name + " stopped at simulation step " + str(self.step) + \
                      " at location (" + str(round(self.x,1)) + "," + str(round(self.y,1)) + ")")
                print("")
                self.isstop = True
        
    def check_reward(self,rewards):
        #check if reaches reward
        if rewards == None:
            pass
        elif self.isstop:
            pass
        else:
            for reward in rewards:
                if (math.sqrt((self.x - reward.x) ** 2 + (self.y - reward.y) ** 2) <= self.r)\
                   and(reward.owner == None)and(reward.universe == self.current_universe):
                    reward.owner = self
                    self.rewards = self.rewards + 1
                    self.reward_name.append(reward.name)
                    self.points = self.points + reward.points                
                    self.dx = self.dx - (self.rewards % 2) * (self.rewards / 6) * self.dx
                    self.dy = self.dy-((self.rewards + 1) % 2) * (self.rewards / 6) * self.dy
                    print(self.name + ' picked up "' + reward.name +'" at simulation step ' + str(self.step))
                    print(str(self))
                    print("")
                                                 
    def check_meet(rewards,persons):
        #check if two people meet
        for i in range(len(persons) - 1):
            for j in range(i + 1, len(persons)):
                if (math.sqrt((persons[i].x - persons[j].x) ** 2 + \
                              (persons[i].y - persons[j].y) ** 2) <= persons[i].r \
                    +persons[j].r) and (not persons[i].isstop) and (not persons[j].isstop) \
                   and (persons[i] != persons[j]) and \
                   (persons[i].current_universe == persons[j].current_universe):
                    
                    print(persons[i].name + " and " + persons[j].name + " crashed at simulation step "\
                          + str(persons[i].step) + " in universe " + persons[i].current_universe)
                    if persons[i].rewards > 0:                           
                        persons[i].rewards = persons[i].rewards - 1
                        
                        for reward in rewards:
                            if reward.name == persons[i].reward_name[0]:
                                print(persons[i].name + ' dropped "' + reward.name + \
                                      '", reward returned to ' + reward.universe + \
                                      " at (" + str(reward.x) + "," + str(reward.y) + ")")
                                reward.owner = None
                                persons[i].points = persons[i].points - reward.points
                        del persons[i].reward_name[0]
                        persons[i].dx = -(persons[i].dx + (persons[i].rewards % 2) * \
                                          (persons[i].rewards / 6) * persons[i].dx)
                        persons[i].dy = -(persons[i].dy + ((persons[i].rewards+1) % 2) * \
                                          (persons[i].rewards / 6) * persons[i].dy)
                        
                    if persons[j].rewards > 0:
                        persons[j].rewards = persons[j].rewards - 1
                        
                        for reward in rewards:
                            if reward.name == persons[j].reward_name[0]:
                                print(persons[j].name + ' dropped "' + reward.name +\
                                      '", reward returned to ' + reward.universe + \
                                      " at (" + str(reward.x) + "," + str(reward.y) + ")")
                                reward.owner = None
                                persons[j].points = persons[j].points - reward.points
                        del persons[j].reward_name[0]
                        persons[j].dx = -(persons[j].dx + (persons[j].rewards % 2) *\
                                          (persons[j].rewards/6)*persons[j].dx)
                        persons[j].dy = -(persons[j].dy + ((persons[j].rewards+1)%2) *\
                                          (persons[j].rewards/6)*persons[j].dy)
                    
                    print(str(persons[i]))
                    print(str(persons[j]))
                    print("")
    
    def check_portal(self,portals):
        #check if a person pass the portal
        if portals == None:
            pass
        elif self.isstop:
            pass   
        else:
            for portal in portals:
                if (math.sqrt((self.x - portal.fromx) ** 2 + (self.y - portal.fromy) **2 )\
                    <= self.r) and (self.current_universe == portal.universe):  
                    self.current_universe = portal.to_universe
                    self.x = portal.to_x
                    self.y = portal.to_y
                    print(self.name + " passed through a portal at simulation step " + str(self.step))
                    print(str(self))
                    print("")

    def __str__(self):
        #to string
        return(self.name + " of " + self.home_universe+ " in universe " + self.current_universe \
               + "\n    at " + "(" + str(round(self.x,1)) + ',' + str(round(self.y,1)) + ")" \
               + " speed "+ "(" + str(round(self.dx,1)) + ',' + str(round(self.dy,1)) + ")" \
               + " with " + str(self.rewards)+ " rewards and " + str(self.points)\
               + " points" )
  
