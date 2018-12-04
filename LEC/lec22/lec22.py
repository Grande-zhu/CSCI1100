from tkinter import *

class MyApp(object):
    def __init__(self, parent):
        print('Initialized!')
        self.parent = parent
        self.main_frame = Frame(parent)
        self.main_frame.pack()
        self.button1 = Button(self.main_frame, text="Launch", command=self.terminate_program)
        self.button1.configure(width=12, padx="4m", pady="4m")
        self.button1.pack()
        self.button2 = Button(self.main_frame, text="C", command=self.c)
        self.button2.configure(width=12, padx="4m", pady="4m")
        self.button2.pack()
        self.rocket = 2

    def d(self):
        self.rocket += 2

    def c(self):
        print("Launching ... counting", end='')
        for i in range(self.rocket):
            print('...{}'.format(self.rocket), end='')
            self.rocket -= 1
        print('...Liftoff!', flush=True)

    def terminate_program(self):
        self.c()
        print('Terminated')
        self.parent.destroy()

if __name__ == "__main__":
    root = Tk()
    print("Countdown ready")
    myapp = MyApp(root)
    myapp.d()
    root.mainloop()
    myapp.d()
    print(myapp.rocket)
    myapp.c()
    print("Done")