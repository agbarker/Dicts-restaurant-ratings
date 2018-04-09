"""Restaurant rating lister."""


# put your code here
import sys
filename = sys.argv[1]

def restaurant_ratings(filename):

    #reads ratings from file
    raw_restaurant_data = open(filename)

    #create dictionary
    restaurant_scores = {}

    #stores restaurant and rating to dictionary

    for line in raw_restaurant_data:
        name, rating = line.strip().split(":")
        restaurant_scores[name] = rating

    #returns ratings in alphabetical order by restaurant

    for restaurant, rating in sorted(restaurant_scores.items()):
        print "%s is rated at %s." % (restaurant, rating)

restaurant_ratings(filename)
