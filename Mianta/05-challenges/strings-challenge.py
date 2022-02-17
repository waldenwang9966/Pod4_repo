#1.1 Printed multiple items in a single line

ingredient_1 = 'milk'
ingredient_2 = 'eggs'
ingredient_3 = 'flour'
ingredient_4 = 'sugar'
print(ingredient_1,  ingredient_2, ingredient_3, ingredient_4)

#1.2 Printed as a cancatenation
all_ingredients = ingredient_1, ingredient_2, ingredient_3
print(all_ingredients)

#1.3 Used an 'f' string
print(f'{ingredient_1}, {ingredient_2}, {ingredient_3}, {ingredient_4}')

#2.1 
ingredient_1 = ingredient_1.replace('milk', 'butter')

#2.2
ingredients = f'{ingredient_1}, {ingredient_2}, {ingredient_3}, {ingredient_4}'
print(ingredients)

#2.3 Counted the word "Milk" = 0, unless # replaced to 'butter'
number_milk = ingredient_1.count('milk')
print(number_milk)

#2.4 printed ingredients
print(ingredients)

#2.5
#2.6 - printed ingredients in Upper Case
print(ingredients.upper())

#3.1 asked a question to user
activity = input('What do you like to do for fun? ')

#3.2 follow up question prompt from forst question
frequency = input(f'Roughly how many times a week do you make time to do {activity}? ') 
frequency = int(frequency)

#3.3 answered is an 'integer'
print(type(frequency))

#3.4 Uncommented the print statements below, and used `type conversion` to fix the second one, allowing it to run
print('Research shows that making time for enjoyment actually makes you more focused.')
print(f'We recommend you {activity} at least {frequency * 2} times a week!')