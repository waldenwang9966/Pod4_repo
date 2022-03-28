
# Question 1: validate_user_input

from xml.dom import ValidationErr


def validate_user_input():
    user_number = validate_user_input
    user_number(input("please enter a number"))
        try:
            int(user_number)
            print("your input is valid")
            return user_number
        except ValueError:
            print("your input is invalid")
            validate_user_input()

validate_user_input()
print(f'The number the user entered is {user_input}.')
    


# The goal: create a function called validate_user_input that will
# - ask the user for a number: 'Please enter a number'
# - try to turn the user's input into an integer
# - if the user did not input a number, tell them 'You did not enter a valid number, please try again'
# - continue to ask them for a valid number until they input one
# - once a valid number is received, return that number

# NOTE: What type of error does python throw if you try to turn a non-number string into an integer?
# Test it out (or google it!) to see which one. Specifically catch that exception in your code.

print(TypeError)

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
        print(f"{top_ten[10]}")
    except IndexError:
        print("There is no tenth item in this list.")


# NOTE: What type of error does python throw if you try to index into a list past the number of items in it?
# Test it out (or google it!) to see which one. Specifically catch that exception in your code.



print("IndexError")



# Once you are done, uncomment the two lines below to ensure that your code works as expected



print_tenth_item(['a', 'b', 'c'])  # Should print out that there are not ten items in the list
print_tenth_item([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Should print out the 10th item in the list


