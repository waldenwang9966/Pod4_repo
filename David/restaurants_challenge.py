print("Challenge: Favourite Restaurants")

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
    "address1": "375 Valencia St.",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(f'The Latitude is {restaurant["latitude"]}, The longitude is {restaurant["longitude"]}')
print(f'The address for {restaurant["name"]} is, {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]}  {restaurant["zip_code"]}')
print(f'{restaurant["url"]}')

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
# TODO: Write code to print the URL of the website of Four Barrel Coffee.


print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this


restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich"
}

restaurant_2  = {
    "name": "Boeuf & Bun",
    "address" : "271 Kingstone Ave., NY 11213",
    "favourite_dish" : "Crispy Chicken Bites"
}

restaurant_3  = {
    "name": "Izzys Smoke House",
    "address" : "660 Amsterdam Ave., NY 10025",
    "favourite_dish" : "Half BBQ Chicken"
}
print('My top 3 Restaurants')
print()
print('Restaurant #1')
for value in restaurant_1.values():
    print(value)
print()
print('Restaurant #2')
for value in restaurant_2.values():
    print(value)
print()
print('Restaurant #3')
for value in restaurant_3.values():
    print(value)
print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there.
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

restaurant_1.pop("favourite_dish")
print(restaurant_1)

print()

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address.
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.
restaurant_2["address"]='1558 E 20th St.'
print(restaurant_2["address"])
print(restaurant_2)

print()


print("Question 5")
'''
Printing out all 3 of our restaurants every time is getting annoying. Let's clean up our code!
'''

# TODO: Put your 3 restaurant dictionaries into a list called `restaurants`
# TODO: Loop through your list and print out the name and address of each restaurant

restaurants = [restaurant_1, restaurant_2, restaurant_3]
for i in restaurants:
    print(i)
print()
print('Completed!')