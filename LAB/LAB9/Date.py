'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]


class Date(object):
    def __init__(self,x0=1900,y0=1,z0=1):
        #This should take a year, a month and a day with default values of 1900,1, 1.
        self.x = x0
        self.y = y0
        self.z = z0

    def __str__(self):
        #Format the data as a string with year/month/day.

        return "({:04d}/{:02d}/{:02d})".format(self.x, self.y,self.z)

    def same_day_in_year(d1,d2):
        if (d1.y==d2.y)and(d1.z==d2.z):
            return True
        else:
            return False
    
    def is_leap_year(self):
        if(self.x % 4==0):
            if(self.x % 100 == 0):
                if(self.x % 400 == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
            
            
    def __lt__(d1,d2):
        if d1.x<d2.x:
            return True
        elif d1.x>d2.x:
            return False
        elif d1.x==d2.x:
            if d1.y<d2.y:
                return True
            elif d1.y>d2.y:
                return False
            elif d1.y==d2.y: 
                if d1.z<d2.z:
                    return True
                else:
                    return False   

if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print ()
