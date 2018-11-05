"""
Minghao Zhu hw4 part2 10/17/2018
This program is to write a program to looping take in user's input to do three kind
of functions(loc,zip,dist). Different ouput of result depends on user's command.
The loop won't stop until end command is taking in.
"""
import hw04_util
import math

def zip_by_location(zip_codes, location):
    '''
    zip_by_location function taking in zip codes data and location, and then 
    return all zip code in that location by a list
    '''
    zip_list = []
    for zip_code in zip_codes:
        if (zip_code[3] == location[0]) and (zip_code[4] == location[1]):
            zip_list.append(zip_code[0])
    return zip_list

def location_by_zip(zip_codes, code):
    '''
    location_by_zip function taking in zip codes data and a zip code, and then 
    return all information about this zip
    '''
    for zip_code in zip_codes:
        if zip_code[0] == code:
            return (zip_code[1], zip_code[2], zip_code[3], zip_code[4], zip_code[5])
        
def calculate_coordinates(c1,c2):
    '''
    calculate_coordinates function taking in 2 coordunate, and then convert to degree
    minute and second then return the coordinate information with right format
    '''    
    if(c1 > 0):#if c1>0, it's north
        c1_coor_degree = str(int(c1 // 1))
        c1_coor_minute = str(int((c1 % 1) * 60 // 1))+ "'"
        c1_coor_second = str(round((((c1 % 1) * 60) % 1) * 60, 2)) + '"'
        c1_coor = "({:0>3}\xb0{}{}N".format(c1_coor_degree, c1_coor_minute, c1_coor_second)
    elif(c1 <0):#if c1<0, it's south
        c1 = -c1
        c1_coor_degree = str(int(c1 // 1))
        c1_coor_minute = str(int((c1 % 1) * 60 // 1)) + "'"
        c1_coor_second = str(round((((c1 % 1) * 60) % 1) * 60, 2)) + '"'
        c1_coor = "({:0>3}\xb0{}{}S".format(c1_coor_degree, c1_coor_minute, c1_coor_second)
    else:#if c1=0, it's no direction
        c1_coor_degree = 0
        c1_coor_minute = 0
        c1_coor_second = 0 
        c1_coor = "({:0>3}\xb0{}{}".format(c1_coor_degree, c1_coor_minute, c1_coor_second)
    if(c2>0):#if c2>0, it's east
        c2_coor_degree = str(int(c2 // 1))
        c2_coor_minute = str(int((c2 % 1) * 60 // 1)) + "'"
        c2_coor_second = str(round((((c2 % 1) * 60) % 1) * 60, 2)) + '"'
        c2_coor = ",{:0>3}\xb0{}{}E)".format(c2_coor_degree, c2_coor_minute, c2_coor_second)
    elif(c2<0):#if c2<0, it's west
        c2 = -c2
        c2_coor_degree = str(int(c2 // 1))
        c2_coor_minute = str(int((c2 % 1) * 60 // 1)) + "'"
        c2_coor_second = str(round((((c2 % 1) * 60) % 1) * 60, 2)) + '"'
        c2_coor = ",{:0>3}\xb0{}{}W)".format(c2_coor_degree, c2_coor_minute, c2_coor_second)
    else:#if c2=0, it's no direction
        c2_coor_degree = 0
        c2_coor_minute = 0
        c2_coor_second = 0 
        c2_coor = "({:0>3}\xb0{}{}".format(c2_coor_degree, c2_coor_minute, c2_coor_second)    
        
    return c1_coor + c2_coor

if __name__ == "__main__":         
    #form imported hw04_util.read_zip_all() get all zip code information
    zip_codes = hw04_util.read_zip_all()        
    
    while True:
        #read in command
        command = input("Command ('loc', 'zip', 'dist', 'end') => ")
        print(command)
        if(command.lower() == 'loc'):#commmand loc 
            #read in zip code
            zip_code = input("Enter a ZIP code to lookup => ")
            print(zip_code)
            #from location_by_zip function, get the information about this zip
            this_zip = location_by_zip(zip_codes,zip_code)
            if this_zip:
                coor = calculate_coordinates(this_zip[0], this_zip[1])
                print("ZIP code {} is in {}, {}, {} county,\n\tcoordinates: {}\n".\
                  format(zip_code, this_zip[2], this_zip[3], this_zip[4], coor)) 
            else:#if zip code not valid
                print("Invalid or unknown ZIP code\n")
        elif(command.lower() == 'zip'):#commmand zip 
            #read in city name and state name
            city_name = input("Enter a city name to lookup => ")
            print(city_name)
            state_name = input("Enter the state name to lookup => ")
            print(state_name)
            city_name = city_name.capitalize()
            state_name = state_name.upper()
            location=(city_name,state_name)
            #use zip_by_location function to find all zip code in this location
            zip_list = zip_by_location(zip_codes, location)
            if zip_list:
                line = zip_list[0]
                for index_ in range(1,len(zip_list)):
                    line = line + ", " + zip_list[index_]
                print("The following ZIP code(s) found for {}, {}: {}\n".\
                      format(city_name, state_name, line))
            else:#if no zip code found
                print("No ZIP code found for {}, {}\n".format(city_name, state_name))
        elif(command.lower() == 'dist'):#command dist
            #read in two zip code
            first_zip = input("Enter the first ZIP code => ")
            print(first_zip)
            second_zip = input("Enter the second ZIP code => ")
            print(second_zip)
            #from location_by_zip function, get the information about these two zip
            first_zip_loc = location_by_zip(zip_codes,first_zip)
            second_zip_loc = location_by_zip(zip_codes,second_zip)
            #if both zip exist
            if(first_zip_loc) and (second_zip_loc):
                #convert to right unit
                lat1 = first_zip_loc[0] / 180 * math.pi
                long1 = first_zip_loc[1] / 180 * math.pi
                lat2 = second_zip_loc[0] / 180 * math.pi
                long2 = second_zip_loc[1] / 180 * math.pi
                #calculate distance
                a = (math.sin((lat2 - lat1) / 2)) ** 2 + math.cos(lat1) * math.cos(lat2) *\
                    (math.sin((long2 - long1) / 2)) ** 2
                r = 3959.191            
                d = 2 * r * math.asin(a ** (1 / 2))
                print("The distance between {} and {} is {:.2f} miles\n".\
                      format(first_zip, second_zip, d))      
            else:#if zip code is not valid
                print("The distance between {} and {} cannot be determined\n".\
                      format(first_zip, second_zip))
        elif(command.lower() == 'end'):#command end to end the loop
            print("\nDone")
            break
        else:#ignore other command
            print("Invalid command, ignoring\n")