"""Restaurant rating lister."""


# put your code here
import sys
filename = sys.argv[1]

def restaurant_ratings(filename):

    #reads ratings from file
    raw_restaurant_data = open(filename)

    #create dictionary
    restaurant_scores = {}

    is_new_add = raw_input("Do you want to add a restaurant?  Yes or No ")

    if is_new_add == "Yes":
        new_restaurant = add_restaurant_rating()
        restaurant_scores[new_restaurant[0].title()] = new_restaurant[1]

    #stores restaurant and rating to dictionary

    for line in raw_restaurant_data:
        name, rating = line.strip().split(":")
        restaurant_scores[name] = rating

    #returns ratings in alphabetical order by restaurant

    for restaurant, rating in sorted(restaurant_scores.items()):
        print "%s is rated at %s." % (restaurant, rating)


def add_restaurant_rating():
    new_restaurant = raw_input("What is the restaurant name? ")
    new_rating = raw_input("What is the new rating? ")
    
    return (new_restaurant, new_rating)


restaurant_ratings(filename)
