"""Restaurant rating lister."""


def restaurant_ratings(filename):
    """Translates text file to dictionary"""

    #reads ratings from file
    raw_restaurant_data = open(filename)

    #create dictionary
    restaurant_scores = {}

    #stores restaurant and rating to dictionary

    for line in raw_restaurant_data:
        name, rating = line.strip().split(":")
        restaurant_scores[name] = rating

    raw_restaurant_data.close()

    #returns ratings in alphabetical order by restaurant
    return restaurant_scores


def add_restaurant_rating(restaurant_scores):
    """Allows user to add a new restaurant to the list"""

    is_new_add = raw_input("Do you want to add a restaurant?  Yes or No ")

    if is_new_add != "Yes":
        return restaurant_scores
    else:
        new_name = raw_input("What is the restaurant name? ")
        new_rating = get_good_rating()

        restaurant_scores[new_name.title()] = new_rating


def alpha_restaurants(restaurant_scores):
    """Allows user to view alphabetical restaurant scores"""

    for restaurant, rating in sorted(restaurant_scores.items()):
        print "%s is rated at %s." % (restaurant, rating)


def update_random_restaurant(restaurant_scores):
    """Generates a random restaurant and its current rating.  Allows user to update the rating for the random restaurant."""
    import random

    #choose random restaurant (choice function)
    rand_name = random.choice(restaurant_scores.keys())
    rand_rating = restaurant_scores[rand_name]

    #print random restaurant and rating
    print "The random restaurant is %s, its rating is %s" % (rand_name, rand_rating)

    #ask user
    new_rand_rating = get_good_rating()

    #update rating
    restaurant_scores[rand_name] = new_rand_rating


def update_chosen_restaurant(restaurant_scores):
    """Asks user for retaurant and updates rating"""

    alpha_restaurants(restaurant_scores)

    user_rest = get_good_restaurant(restaurant_scores)
    user_new_rating = get_good_rating()
    restaurant_scores[user_rest] = user_new_rating


def get_good_rating():
    """ Asks for a user rating, checks if user rating is within 1-5 scale."""
    user_rating = raw_input("Rating: ")
    while user_rating not in ["1", "2", "3", "4", "5"]:
        user_rating = raw_input("Please enter valid rating 1-5: ")
    return user_rating


def get_good_restaurant(restaurant_scores):
    """Asks user for restaurant, check if valid."""
    user_rest = raw_input("Restaurant: ")
    while user_rest not in restaurant_scores:
        user_rest = raw_input("Please enter valid restaurant: ")
    return user_rest


import sys
filename = sys.argv[1]
restaurant_scores = restaurant_ratings(filename)
user_choice = "0"
while user_choice != "5":

    user_choice = raw_input("""
    1. See all the ratings
    2. Add a new restaurant
    3. Update a random restaurant
    4. Update a chosen restaurant
    5. Quit
    > """)

    if user_choice == "1":
        alpha_restaurants(restaurant_scores)
    elif user_choice == "2":
        add_restaurant_rating(restaurant_scores)
    elif user_choice == "3":
        update_random_restaurant(restaurant_scores)
    elif user_choice == "4":
        update_chosen_restaurant(restaurant_scores)
    elif user_choice == "5":
        break
    else:
        user_choice = raw_input("Please enter a valid input. ")
