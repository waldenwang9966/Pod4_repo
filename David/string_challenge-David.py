# 1.1 Printing multiple items in a single line

ingredient_1 = 'milk'
ingredient_2 = 'eggs'
ingredient_3 = 'flour'
ingredient_4 = 'sugar'
print(ingredient_1,  ingredient_2, ingredient_3, ingredient_4)

#1.2 Printing as a cancatenation

# PROBLEM - couldn't create space between the words without quotations
# print(ingredient_1,  ingredient_2, ingredient_3, ingredient_4)
all_ingredients = ingredient_1, ingredient_2, ingredient_3
print(all_ingredients)

#1.3 using the f string
print(f'{ingredient_1}, {ingredient_2}, {ingredient_3}, {ingredient_4}')

#2.1 - 2.2
ingredient_1 = ingredient_1.replace('milk', 'butter')
ingredients = f'{ingredient_1}, {ingredient_2}, {ingredient_3}, {ingredient_4}'
print(ingredients)

#2.3 Counting the word "Milk" = 0, unless you # replacement to 'butter'
num_milk = ingredient_1.count('milk')
print(num_milk)

#2.4
print(ingredients)

#2.5 - Don't understand the question, we already did the 'replacement' and we get 'butter'
#2.6 - Upper Case
print(ingredients.upper())

# 3.1
activity = input('What do you like to do for fun? ')

# 3.2
frequency = input(f'Roughly how many times a week do you make time to {activity}? ') 
frequency = int(frequency)

# 3.3 answer is an 'integer'
print(type(frequency))

# 3.4 Uncomment the print statements below, and use `type conversion` to fix the second one, allowing it to run
print('Research shows that making time for enjoyment actually makes you more focused.')
print(f'We recommend you {activity} at least {frequency * 2} times a week!')