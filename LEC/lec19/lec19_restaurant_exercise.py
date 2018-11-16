'''
Demonstration example to build a list of Restaurant objects from the
Yelp data we worked with in Lecture 19.
'''

from Restaurant import Restaurant

def convert_input_to_restaurant(line):
    '''
    Parse the Yelp input data to create a Restaurant object.
    '''
    m = line.strip().split("|")
    name = m[0]
    latitude = float(m[1])
    longitude = float(m[2])
    address = m[3].split('+')   # creates a list of the address lines
    url = m[4]
    restaurant_type = m[5]
    reviews = []
    for r in m[6:]:
        reviews.append(int(r))
    return Restaurant(name, latitude, longitude, address, url, \
                          restaurant_type, reviews )

def build_restaurant_list( file_name ):
    '''
    Assuming the Yelp data is in the form of one line per restaurant,
    read each line, create a restaurant object from each, and form a
    list of these objects.  Return the list.
    '''
    restaurants = []
    for line in open(file_name):
        restaurants.append(convert_input_to_restaurant(line))
    return restaurants
    
if __name__ == "__main__":
    file_name = 'yelp.txt'
    restaurants = build_restaurant_list( file_name )
    num_restaurants = len(restaurants)

    # Initial code to print the first three restaurants, just to see
    # how each restaurant is formed into an object and converted to a
    # string for output.
    for i in range(0,3):
        print(str(restaurants[i]))

    '''
    As a demonstration, here is code to find the top restaurant in a
    user-provided city.  We'll need to add methods to the Restaurant
    class to complete this.
    '''

    """
    print('This program will find the top-rated restaurant')
    print('in a city of your choice.')
    city_name = input('Enter the name of the city => ').strip()

    #  Record the name of the top restaurant and the best rating
    top_name = ''
    top_avg = -1

    #  Examine the restaurants one-by-one
    for r in restaurants:
        # Skip restaurants that are not in the given city
        if not r.is_in_city(city_name):
            continue
        
        #  Find the average region and if it is higher than the top
        #  review thus far then save it and save the name of the
        #  restaurant
        rating = r.average_review()
        if rating > top_avg:
            top_name = r.name
            top_avg = rating

    if top_name == '':
        print("Found no restaurants in {}".format(city_name))
    else:
        print('{} is the top restaurant in {}'.format(top_name,city_name))
        print('It has an average rating of {:.2f}'.format(top_avg))
    """
