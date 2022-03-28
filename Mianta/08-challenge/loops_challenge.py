days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# # QUESTION 1: For loops with list

# # Let's start simple, and build up from there.
# # 1.1: Write a for loop that prints out each day in the `days` variable above.
for day in days:
     print(day)

# # 1.2: Now, instead of printing out the day, let's ask the user what their favorite thing
# # to do is on that day of the week. (Make sure to use an f-string so that the user knows which day they're being asked about.)

activities = [] # "list()"this is a way to define an empty list
for day in days: #this is the loop that breaks down the days to ask user what their fav activity is.
    user_activity = input(f"What is your favorite thing to do on {day}?")
    activities.append(user_activity)  #this is where the user input is saved and added to the activities variable.

# # 1.3: We should keep track of the user's favorite things to do so that we can print them out all together.ABOVE your for loop, create a new empty list to hold the user's favorite activities.
print(activities)


# # 1.4: Now, back in your for loop, append each of the user's answers into your new list.
# # Print out the list after your loop to check if it got populated correctly.
for i in range(len(days)):
    print(f'On {days[i]}, favorite activity is to {activities[i]}.') #this is where I used the range function, and used (len) to list the days on separate lines asking user what fav activity is 

# 1.5: After your first loop, let's create a new one. As an example, let's say the user's favorite thing to
# do on mondays is plan their week. This time, we want the output to be something like this:
# 'On Mondays, your favorite activity is to plan your week.'
# We need information from both lists! Let's use the `range` function to loop through the indexes
# of the items in the lists (this will work because the lists are the same length).
# Each time through this new loop, use the index number to index into each of your lists for the data
# you need to print out.


# Take a look back at the code you just wrote. Look at how much it does!
# Often, programmers will be given large tasks, and it's our responsibility to be able to break it down into smaller pieces. We did the above piece by piece, but think about what the prompt might have been to get us there.

# Maybe: Write a program that asks the user about their favorite thing to do each day of the week. Afterward, print out for the user each of their favorite daily activities.

#Would this larger task have felt doable without breaking it down into steps? Is it clear what needs to be done?

####### This defintely is easier to see what I need to do in order to get the loop to function properly. 


# Try to break down the steps required for this second loop challenge.
    # 1- Created a the day variable from the list of days

    # 2- created a loop to take users input to determine what their favorite activity is on a given day.

    # 3- saved user input and added to the activities variable. 

    # 4- this is where I used the range function, and used (len) to list the days on separate lines asking user what fav activity is 

# QUESTION 2: For loops with list:

# Write a program that loops through the days in the week. Each day, ask the user what the temperature is. 
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


temperature = '' #this is the list for integers

for day in days:
    temperature = int(input(f"What is the temperature {day}?"))#Wrote temperature = an integer then takes user numerical input to ask what temperature for each day



    if temperature < 50:
        print('Put on a jacket!')# If the temperature is below 50, tell the user to put on a jacket
    elif temperature >= 50 and temperature <= 65:
        print('Put on a sweater!')#if the temperature is between 50 and 65, tell the user to put on a sweater.
    else:
        print('Put on sunscreen!')#Finally, if the temperature is above 65, tell the user to put on some sunscreen.



# QUESTION 3: For loops with the range function

#Write a program that asks the user how many times they would like to be wished happy birthday.
number_birthday_wishes = int(input('How many times would you like to be wished Happy Birthday? '))

for i in range(number_birthday_wishes):
    print('Happy Birthday!!!')# Then, print out happy birthday that number of times.



# QUESTION 4: While loops
temperature = int(input('What temperature is it outside? '))#Wrote temperature = an integer then takes user numerical input to ask what temperature it is outside.

while (temperature < 65):
    print('Put on a sweater!') #Used a while statement to declare if the temperature is below 65 tell the user to wear a sweater. 
    break #this is to terminate the loop so the next statement can resume.
else:
    print('Spring has sprung!')#  Once the temperature is over 65, stop looping, and tell the user that "Spring has sprung!!!"