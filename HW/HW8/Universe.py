class Universe(object):
    '''
    Universe class is to keep track of each universe, and store its info in its
    attributes
    '''
    def __init__( self, rewards = None, portals = None, name = ""):
        #initialization
        self.rewards = rewards
        self.portals = portals
        self.name = name
            
    def __str__(self):
        #to string
        return (self.name + " (" + str(self.rewards) + " rewards and " + str(self.portals) +" portals)")
