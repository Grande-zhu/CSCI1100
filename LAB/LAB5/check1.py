import lab05_util

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
    for i in range(len(score_1)):
        total_score = total_score+score_1[i]
        i = i+1
    avg_score = total_score/len(score_1)
    print("Average Score: {:.2f}".format(avg_score))
    
restaurants = lab05_util.read_yelp('yelp.txt')

find_info(restaurants[0])
print("")
find_info(restaurants[4])
print("")
find_info(restaurants[42])


