print("Challenge: Favorite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp.

Go through the dictionary and print out the following 3 pieces of information about the restaurant:
1. The latitude and longitude of Four Barrel Coffee
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print({restaurant["latitude"]}) #this will print the latitude

print({restaurant["longitude"]}) #this will print the longitude



# TODO: Wrote code to print the complete address of the Four Barrel Coffee, formatted it as a string - it should include the address, city, state and the zip code.
print(f'The address of the Four Barrel Coffee restaraunt is {restaurant["address1"]} {restaurant["city"]}{restaurant["state"]} {restaurant["zip_code"]}')

# TODO: Wrote code to print the URL of the website of the Four Barrel Coffee.
print(restaurant["url"])

print()

print("Question 2")

#Chose 3 of your most favorite restaurants in NYC, and created a dictionary for each of them with the following key-value pairs:
# Printed each dictionary

# The dictionary for each restaurant should look something like this
restaurant_1  = {
    "name": "The Honey Well",#1. name of the restaurant (string)
    "address" : "3604 Broadway, New York, NY 10031",#2. address of restaurant (string)
    "favorite_dish" : "Maryland Crabcakes"#3. favorite_dish (string)
}

restaurant_2 = {
    "name": "Sushi Nakazawa",#1. name of the restaurant (string)
    "address": "23 Commerce Street, NY, 10004",#2.address of the restaurant (string)
    "favorite_dish" : "Chu-Maki"#3. favorite_dish (string)
}

restaurant_3 = {
    "name" : "West Side SteakHouse",
    "address" : " 597 10th Avenue, New York, NY 10036",
    "favorite_dish" : "Grilled Baby Loin Lamb Chops"
}

print(restaurant_1)
print(restaurant_2)
print(restaurant_3)

print()

print("Question 3")
'''
Imagine that any 1 of your most favorite restaurants stopped serving your favorite dish there.
'''
#Removed the 'favorite_dish' key-value pair from restaurant_2
restaurant_2.pop('favorite_dish')
#Printed new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
print(restaurant_2)

print()

print("Question 4")
'''
Imagine that another one of your most favorite restaurants modified its address.
Update just this value in that restaurant's dictionary
'''

#Update the address field of 1 restaurant
restaurant_1["address"] = "999 Let Me Get a Taste Lane, Somewhere, OutThere, 99999" 
#Printed the new address of the restaurant by accessing that field of the restaurant's dictionary
print(restaurant_1)
#Printed the updated dictionary.

print()


print("Question 5")
'''
Printing out all 3 of our restaurants every time is getting annoying. Let's clean up our code!
'''

#Put 3 restaurant dictionaries into a list called `restaurants`
restaurants = [restaurant_1, restaurant_2, restaurant_3]
#Looped through my list and printed out the name and address of each restaurant
for i in restaurants:
    print(i["name"], 
    i["address"])
