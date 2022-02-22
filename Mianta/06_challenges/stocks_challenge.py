from http import client


print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amzn = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# asked the client their name and saved it to the variable.
client_name = input ('Please enter your name...-')
if client_name.isdigit() == False:
     print('Please re-enter your name-')
client_name = input ('Please enter your name-') #this ensures numerical input is not input but instead alphabets 

#asked client what their savings account amount and saved it to another variable.
client_savings = int(input(f'Hello,{client_name} and Thank you! How much is in your savings account?'))

#Wrote code to asked the client the stock they are interested in and saved it to another variable, as shown below.
stock = input("Awesome, thank you! Which stock are you interested in? Please type 'amzn' for Amazon, 'appl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print('Uh-Oh! Please re-type your preferred stock only alphabet letters.')
stock = input('Which stock(s) are you interested in?') #same as above

print()

print("Challenge 3.2.2: Perform user-specific calculations")
#all 3 user inputs stored in variables. Then wrote conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
if stock == 'amzn': 
    price = amzn
    num_of_stocks = client_savings / price
elif stock == 'appl':
    price = apple
    num_of_stocks = client_savings / price 

elif stock == 'fb':
    price = fb
    num_of_stocks = client_savings / price 
elif stock == 'goog':
    price = google
    num_of_stocks = client_savings / price 
elif stock == 'msft':
    price = msft
    num_of_stocks = client_savings / price 
else:
    print('Whoops!!!! An error occurred please try again')

print()

print("Challenge 3.2.3: Output for the user the result")
#Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
print(f'{client_name} has ${client_savings} in savings and they can purchase {num_of_stocks} shares of {stock} at the price of {price}')
print()