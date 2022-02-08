# print('1.1: Create a variable called `meal`, and save a string describing what you had for lunch in it')
meal = 'spicy noodles and egg'

# print('1.2: Print the meal variable')
print(meal)

# print('1.3: Update the meal variable to be a string describing what you want for dinner. print it out again')
meal = 'have not eaten dinner... drank a juice box!'
print(meal)

# print('2: How old is Google?')
# 2.1: Google was founded in 1993. The current year is 2022. Create a variable called google_age, and use subraction
# to figure out how old Google is
# ex: my_age = current_year - birth_year
google_age = 2022 - 1993
print(google_age)


# 2.2: Using an f-string, print out a sentence about Google's age. Make sure to include your variable in the f-string!
print(f'Google is {google_age} years old!')

# 2.3 How many _months_ old is Google? Create a new variable google_age_months, and use multiplication to figure it out,
# then print a new f-string with the info.
# (Assume 12 months for each year, you don't need to check which month they started)

google_age_months = google_age * 12
print(f"Google's age in months is: {google_age_months}!")


# print('3.1: The line of code below is commented out because it produces many SyntaxErrors.')
completion_message = 'Completed the first Python challenge!'
#completion message = 'Completed the first Python challenge!

# 3.2 What were the syntax errors that you fixed? print out a quick explanation of each one.
print('First, I added an underscore to correct the var name')
print('Then, I added another quote mark at the end of the sentence to complete the str')
# print('3.3: Turn the comment below back into regular Python code')
print(completion_message)