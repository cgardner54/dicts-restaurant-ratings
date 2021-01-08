"""Restaurant rating lister."""

# put your code here

"""
open file
parse data from file
Reads the ratings in from the file

Stores them in a dictionary

And finally, spits out the ratings in alphabetical order by restaurant
sort and print restaurant ratings

Hint 1: Using .items() to get a list of your dictionary entries will help with sorting.

Hint 2: Refer to the Python docs on the sorted() function if you need a reminder of how to sort.

str = "key1=value1;key2=value2;key3=value3"

d = dict(x.split("=")

for k, v in d.items():
    print(k, v)


"""
def display_ratings(filename):
    ratings = open(filename)
    rating_dict = {}
    for line in ratings:
        rate_n_restaurants = (line.rstrip().split(":"))
        restaurant, rating = rate_n_restaurants
        rating_dict[restaurant] = rating
        

        # rate_n_restaurants = [name, rating]
        # restaurant = rate_n_restaurants[0]
        # rating = rate_n_restaurants[1]
        
    for restaurant, rating in sorted(rating_dict.items()):
        print(f"{restaurant}'s rating is {rating}")
    return rating_dict
(display_ratings('scores.txt'))     
        # rate_n_restaurant = dict(line.split(":"))
        # for item in str.split(":"):
        #     print(rate_n_restaurant)
        #     #for key, value in item():
        #         #print(f"{key} is rated at {value}")

numbers = [1, 2, 3, 4, 5]
           0, 1, 2, 3, 4 

for i, num in enumerate(numbers):
    numbers[i]