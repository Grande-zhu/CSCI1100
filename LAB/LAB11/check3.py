from tkinter import *

from Ball1 import *
import random
import copy

class BallDraw(object):
    def __init__ (self, parent,maxx=400,maxy=400,wait_time=100,balls=[]):
        ##=====DATA RELEVANT TO BALL===============
        ##  We are going to repeatedly draw a ball object on the canvas,
        ##  "moving" it across the canvas.  The ball object is specified
        ## by (a) its x and y center coordinates (a tuple), (b) its radius,
        ##  (c) the delta x and delta y to move the ball in each time
        ## increment, and (d)  its color.
        self.balls=balls
        self.balls_ori=copy.deepcopy(balls)
        self.wait_time=wait_time
        self.isstopped = False 
        self.maxx=maxx
        self.maxy=maxy

        #=============CREATE THE NEEDED GUI ELEMENTS===========

        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="white", \
                             width=self.maxx, height=self.maxy )
        self.canvas.pack()
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.restart = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restart.pack(side=LEFT)
        self.slow = Button(self.bottom_frame, text="Slower", command=self.slower)
        self.slow.pack(side=LEFT)
        self.fast = Button(self.bottom_frame, text="Faster", command=self.faster)
        self.fast.pack(side=LEFT)
        self.quit = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quit.pack(side=RIGHT)

    def faster(self):
        if self.wait_time > 2:
            self.wait_time //= 2

    def slower(self):
        self.wait_time *= 2
            
    def restart(self):
        self.balls=copy.deepcopy(self.balls_ori)
        
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
        
    def draw_ball(self):
        #  Remove all the previously-drawn balls
        self.canvas.delete("all")
        
        # Draw an oval on the canvas within the bounding box
        for ball in self.balls:
            self.canvas.create_oval(ball.bounding_box(), fill=ball.ball_color)
            self.canvas.update()      # Actually refresh the drawing on the canvas.

        # Pause execution.  This allows the eye to catch up
        self.canvas.after(self.wait_time)

    def animate(self):
        ##  Loop until the ball runs off the screen.
        
        while(not self.isstopped):
            # Move the ball
            self.draw_ball()
            for ball in self.balls:
                ball.check_and_reverse(self.maxx,self.maxy)
                ball.move()
            
    def creat_ball():
        x,y = random.randint(10,390),random.randint(10,390)    # initial location

        radius = random.randint(5,10)

        dx,dy = random.randint(-8,8),random.randint(-8,8)    # the movement of the ball object

        colorList = ["blue", "red", "green", "yellow", "magenta", "orange"]
        color = random.choice(colorList) 

        ball=Ball(x,y,dx,dy,radius,color)
        return ball
    



if __name__ == "__main__":
    ##  We will create a root object, which will contain all 
    ##  our user interface elements
    ##
    

    balls=[]
    for i in range(9):
        ball=BallDraw.creat_ball()
        balls.append(ball)
    
        
        
    root = Tk()
    root.title("Tkinter: Lab 11")

    
    ## Create a class to handle all our animation
    bd = BallDraw(root,balls=balls)
    
    ## Run the animation by continuously drawing the ball and then moving it
    bd.animate()
    
    

    ## This is an infinite loop that allows the window to listen to
    ## "events", which are user inputs.  The only user event here is
    ## closing the window, which ends the program. 
    root.mainloop()


    
