import math

class Ball(object):
    def __init__( self, x0=0, y0=0, dx=0 ,dy=0 , radius=0,  color="red" ):
        #initialize
        self.ball_x = x0
        self.ball_y = y0
        self.ball_dx = dx
        self.ball_dy = dy
        self.ball_radius = radius
        self.ball_color = color
        

    def position(self):
        #return position
        return (self.ball_x, self.ball_y)

    def move(self):
        #move
        self.ball_x=self.ball_x+self.ball_dx
        self.ball_y=self.ball_y+self.ball_dy
        
    
    def bounding_box(self):
        #return tuple of 4
        return (self.ball_x-self.ball_radius, self.ball_y-self.ball_radius, self.ball_x+self.ball_radius, self.ball_y+self.ball_radius)
    
    def get_color(self):
        #return color
        return self.ball_color 
    
    def some_inside(self,maxx,maxy):
        #return if it is inside the window
        if (0 < self.ball_x + self.ball_radius)and(self.ball_x - self.ball_radius < maxx)and(0 < self.ball_y + self.ball_radius)and(self.ball_y - self.ball_radius < maxy):
            return True
        else:
            return False
        
    def check_and_reverse(self,maxx,maxy):
        if (self.ball_x - self.ball_radius < 0)or(self.ball_x + self.ball_radius > maxx):
            self.ball_dx*=-1
        if (self.ball_y - self.ball_radius < 0)or(self.ball_y + self.ball_radius > maxy):
            self.ball_dy*=-1
            
    
        
 
#if __name__ == "__main__":
    