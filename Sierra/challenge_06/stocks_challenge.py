from unittest.util import strclass


print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
client_name = input('What is your name? ')
if client_name.isdigit() == True:
    print('Sorry. Please re-type your name!')
    client_name = input('What is your name? ') # I know this code doesn't make sure to ask user for name again if input is a number again T.T

# TODO: Write code to ask the client his savings and save it to another variable.
client_savings = input(f'Thank you, {client_name}! How much do you have in your savings? ')
if client_savings.isdigit() == False:
    print('Oops! Please re-enter your savings amount using numbers only.')
    client_savings = input(f'How much do you have in your savings? ') # Same comment here about it not checking again!

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Great! Which stock are you interested in? Please type 'amzn' for Amazon, 'app' for Apple, 'fcbk' for Facebook, 'ggl' for Google and 'mcsft' for Microsoft. ")
if stock.isalpha() == False:
    print('Oh no! Please re-type your preferred stock using letters only.')
    stock = input('Which stock are you interested in? ') # Aaaaaand same here as well T_T lol
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
if stock == 'amzn': 
    num_of_stocks = int(int(client_savings) / amazon)
    print(f'{client_name} has ${client_savings} in savings and they can purchase {num_of_stocks} share/s of Amazon at the current price of $3000')
elif stock == 'app':
    num_of_stocks = int(int(client_savings) / apple)
    print(f'{client_name} has ${client_savings} in savings and they can purchase {num_of_stocks} share/s of Apple at the current price of $100')
elif stock == 'fcbk':
    num_of_stocks = int(int(client_savings) / fb)
    print(f'{client_name} has ${client_savings} in savings and they can purchase {num_of_stocks} share/s of Facebook at the current price of $250')
elif stock == 'ggl':
    num_of_stocks = int(int(client_savings) / google)
    print(f'{client_name} has ${client_savings} in savings and they can purchase {num_of_stocks} share/s of Google at the current price of $1400')
elif stock == 'mcsft':
    num_of_stocks = int(int(client_savings) / msft)
    print(f'{client_name} has ${client_savings} in savings and they can purchase {num_of_stocks} share/s of Microsoft at the current price of $200')

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()
