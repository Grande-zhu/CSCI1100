
from tkinter import *

class MyApp(object):
    def __init__(self, parent):
        self.width = 600
        self.height = 600
        self.length = min(self.width, self.height)/4
        self.level=5
        self.parent = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.canvas_frame = Frame(self.main_frame)
        self.canvas_frame.pack(side=TOP)
        self.canvas = Canvas(self.main_frame, \
                             width=self.width, height=self.height)
        self.canvas.pack()
        
        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(side=BOTTOM)
        self.drawbutton = Button(self.button_frame, text="Draw", \
                                 command = self.draw)
        self.drawbutton.pack(side=LEFT)
        self.clearbutton = Button(self.button_frame, text="Clear", \
                                  command = self.clear)
        self.clearbutton.pack(side=LEFT)
        self.quitbutton = Button(self.button_frame, text="Quit", \
                                 command = self.quit)
        self.quitbutton.pack(side=RIGHT)
        
    def clear(self):
        self.canvas.delete("all")

    def quit(self):
        self.parent.destroy()

   # def draw(self,center_x,center_y):
    def draw(self):
        #self.draw_lines(self.width/2, self.height/2, \
                        #min(self.width, self.height)/4 )
        self.draw_lines(self.width/2, self.height/2, \
                        min(self.width, self.height)/4,self.level )
        #self.draw_lines(center_x,center_y,self.length,self.level)

        
    ## Modify this function to call itself recursively to draw smaller
    ## plus signs at the four end points of the current plus sign.
    ## You must have a stopping condition to make sure that the
    ## recursion ends!
    def draw_lines(self, centerx, centery, length,level):
       
        self.canvas.create_line(centerx, centery+length, \
                                centerx, centery-length, fill="black") 
        self.canvas.create_line(centerx+length, centery, \
                                centerx-length, centery, fill="black") 
        self.canvas.update()
        self.canvas.after(0)
        if level > 0:        
            level=level-1
            #top 
            center_1_x=centerx
            center_1_y=centery + length
            
            #right    
            center_2_x=centerx + length
            center_2_y=centery
             
            #bottom  
            center_3_x=centerx
            center_3_y=centery - length
            
            #left
            center_4_x=centerx - length
            center_4_y=centery
            
            length=length/2
            
    
    
            self.draw_lines(center_1_x,center_1_y,length,level)
            self.draw_lines(center_2_x,center_2_y,length,level)
            self.draw_lines(center_3_x,center_3_y,length,level)
            self.draw_lines(center_4_x,center_4_y,length,level)            
            


### The main code simply creates a canvas and three buttons. 
if __name__ == "__main__":
    root = Tk()
    root.title("Recursion Example: Lab 12 Checkpoint 2")
    myapp = MyApp(root)
    myapp.draw()
    #myapp.draw(300,300)
    root.mainloop()
