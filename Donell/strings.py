


ingredient_1 = "milk"
ingredient_2 = "eggs"
ingredient_3 = "flour"
ingredient_4 = "sugar"

#1.2

print (ingredient_1,ingredient_2,ingredient_3,ingredient_4)

#1.2

print ("ingredient_1 + ", "  + ingredient_2 + ", "  ingredient_3 + ", " ingredient_4")

#1.3

print (f"ingredient 1: {ingredient_1}. ingredient 2: {ingredient_2}. ingredient 3: {ingredient_3}. ingredient 4 {ingredient_4}.")

#2.1

ingredients =  (f"ingredient 1: {ingredient_1}. ingredient 2: {ingredient_2}. ingredient 3: {ingredient_3}. ingredient 4 {ingredient_4}.")

#2.2
print(ingredients.replace("milk", "butter"))

#2.3
print(ingredients.count("milk"))

#2.4
print(ingredients)

#2.5
ingredients = ingredients.replace("milk","butter")

#2.6 
print(ingredients.upper())

#3.1
activity = input("whats your favorite thing to do ?")

#3.2
frequency =input(f"i listen to music {activity}?")
print (frequency)
print(type(frequency))

#3.3
#its a string.

#3.4
print('Research shows that making time for enjoyment actually makes you more focused.')
print(f'We recommend you {activity} at least {frequency * 2} times a week!')