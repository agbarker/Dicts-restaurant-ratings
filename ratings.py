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
        tokened_restaurants = line.strip("\n").split(":")
        restaurant_scores[tokened_restaurants[0]] = tokened_restaurants[1]

    #returns ratings in alphabetical order by restaurant

    alpha_restaurant_names = sorted(restaurant_scores)

    for restaurant in alpha_restaurant_names:
        rest_vals = restaurant_scores[restaurant]
        print "%s is rated at %s." % (restaurant, rest_vals)

restaurant_ratings(filename)
