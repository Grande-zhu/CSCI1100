import lab05_util
import webbrowser

def find_info(restaurant):
    names = restaurant[0]
    type_1 = restaurant[5]
    print(names+"("+type_1+")")
    address = restaurant[3]
    address = address.split("+")
    for line in address:
        print("\t"+line)
    score_1 = restaurant[6]
    total_score =0
    max_score = 0
    min_score = 10
    review= len(score_1)
    for i in range(len(score_1)):
        total_score = total_score+score_1[i]
        if (score_1[i]>max_score):
            max_score = score_1[i]
        if (score_1[i]<min_score):
                min_score = score_1[i]        
    i = i+1
    if review>3:
        avg_score = (total_score-max_score-min_score)/(len(score_1)-2)
    
    else:
        avg_score = total_score/len(score_1)
        
    if(avg_score>0)and(avg_score<=2):
        print("This restaurant is rated bad, based on {:.0f} reviews".format(review))
    if(avg_score>2)and(avg_score<=3):
        print("This restaurant is rated average, based on {:.0f} reviews".format(review))
    if(avg_score>3)and(avg_score<=4):
        print("This restaurant is rated above average, based on {:.0f} reviews".format(review))
    if(avg_score>4)and(avg_score<=5):
        print("This restaurant is rated very good, based on {:.0f} reviews".format(review))  
        
    print("What would you like to do next?")
    print("1. Visit the homepage")
    print("2. Show on Google Maps")
    print("3. Show directions to this restaurant")
    
    address_line=""
    for line in address:
        address_line = address_line+" "+line    
    
    choice_1 = input("Your choice (1-3)? ==> ")
    if(choice_1=="1"):
        webbrowser.open(restaurant[4])
        
    elif(choice_1=="2"):
        webbrowser.open('http://www.google.com/maps/place/'+address_line)
    
    elif(choice_1=="3"):
        webbrowser.open('http://www.google.com/maps/dir/110 8th Street Troy NY/'+address_line)

restaurants = lab05_util.read_yelp('yelp.txt')


restaurant_id=int(input("Please type in the id of the restaurant you want to find => "))
if ((restaurant_id)>155)or((restaurant_id)<1):
    print("It is out of range")
else:
    restaurant_id =restaurant_id -1
    find_info(restaurants[restaurant_id])
