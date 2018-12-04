"""
Minghao Zhu hw7 part2 11/12/2018
This program is to show some stats of movies in a file based on a min and max year
and weight of IMDB and Twitter of rating.
Deal with file by importing json and dictionarys.
"""
import json

def find_avg(list1):
    """
    A function to return average of a list
    """
    sum_1=0
    for i in range(len(list1)):
        sum_1 =sum_1 + list1[i]
        
    return sum_1/len(list1)

def ssort(s):
    """
    A function to do the sorting for dictionary
    """
    dic= sorted(s.items(), key=lambda d:d[1], reverse = True)
    i=1
    while i< len(dic):
        if(dic[i][1][0]==dic[i-1][1][0]):
            temp=(dic[i-1])
            dic[i-1]=dic[i]
            dic[i]=temp
            i+=1
        else:
            i+=1    
    return dic 

if __name__ == "__main__":
    #Take user's input
    min_year = int(input("Min year => "))
    print(min_year)                
    max_year = int(input("Max year => "))
    print(max_year) 
    w1= input("Weight for IMDB => ")
    print(w1)
    w2 = input("Weight for Twitter => ")
    print(w2)
    #read in file with json   
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())    
    #convert to right unit
    w1=float(w1)
    w2=float(w2)       
    #intilize variable
    rate_movie=dict()
    movie_detail=[]
    sorted_movie=[]
    #save movie information in a dict
    for movies_id in movies:
        if ((movies[movies_id]['movie_year'])>=min_year)and\
           ((movies[movies_id]['movie_year'])<=max_year):
            if movies_id in ratings:
                if len(ratings[movies_id])>2:
                    imdb_rating=movies[movies_id]['rating']
                    average_twitter_rating=find_avg(ratings[movies_id])
                    #calculate rating
                    final_rate=(w1*imdb_rating + w2*average_twitter_rating)/(w1+w2)
                    #store in dict
                    rate_movie[movies[movies_id]['name']]= final_rate,\
                        movies[movies_id]['movie_year'],movies[movies_id]['genre']
                    
    #do sorting with ssort
    sorted_dict=ssort(rate_movie)
    
    while True:#Using a loop to take in command 
        genre_type = input("\nWhat genre do you want to see? ")
        print(genre_type)
        genre_type=genre_type.title()
        if (genre_type == "Stop"):#exit loop if a stop command is given
            break
        else:
            best_found=0
            #find best movie in this genre
            for i in range(len(sorted_dict)):
                if (genre_type in sorted_dict[i][1][2]):
                    print("\nBest:")
                    print("\tReleased in {}, {} has a rating of {:.2f}".\
                          format(sorted_dict[i][1][1],sorted_dict[i][0],\
                                 sorted_dict[i][1][0]))
                    best_found=1
                    break
            #find worst movie in this genre           
            for i in range(len(sorted_dict)):
                if (genre_type in sorted_dict[len(sorted_dict)-1-i][1][2]):
                    print("\nWorst:")
                    print("\tReleased in {}, {} has a rating of {:.2f}".\
                          format(sorted_dict[len(sorted_dict)-1-i][1][1],\
                                 sorted_dict[len(sorted_dict)-1-i][0],\
                                 sorted_dict[len(sorted_dict)-1-i][1][0]))
                    break
            if(best_found==0):#print not found if no movie in this genre
                print("\nNo {} movie found in {} through {}".\
                      format(genre_type,min_year,max_year))