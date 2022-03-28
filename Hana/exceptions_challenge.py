
# Question 1: validate_user_input

# The goal: create a function called validate_user_input that will
# - ask the user for a number: 'Please enter a number'
# - try to turn the user's input into an integer
# - if the user did not input a number, tell them 'You did not enter a valid number, please try again'
# - continue to ask them for a valid number until they input one
# - once a valid number is received, return that number

def validate_user_input():
    while True:
        try:
               number = int(input("Please enter a number"))
               break
        except ValueError:
                print("You did not enter a valid number, please try again")
        return number


#The computer will try to execute whatever is inside the try box, and if the block of code after try successfully is executed, the except code block will be skipped by the computer. However, if the code inside the try block fails, the code inside the except code block will be executed


# NOTE: What type of error does python throw if you try to turn a non-number string into an integer?
# Test it out (or google it!) to see which one. Specifically catch that exception in your code. Value Error



# Once you are done, uncomment the two lines below to ensure that your code works as expected

# user_number = validate_user_input()
# print(f'The number the user entered is {user_input}.')



# Question 2: print_tenth_item
# The goal: create a function called print_tenth_item that will
# - take in a list of items as a parameter called `top_ten`
# - try to print out an f-string stating the 10th item in the list
# - if there are not ten items in the list, tell the user that

def print_tenth_item(top_ten):
    try:
        print(f"{top_ten[9]}")
    except IndexError:
        print("Theres no tenth item in this list")

# NOTE: What type of error does python throw if you try to index into a list past the number of items in it?
# Test it out (or google it!) to see which one. Specifically catch that exception in your code.
#Index Error

# Once you are done, uncomment the two lines below to ensure that your code works as expected

print_tenth_item(['a', 'b', 'c'])  # Should print out that there are not ten items in the list
print_tenth_item([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Should print out the 10th item in the list
