print("Challenge 3.2: Playing with the stock market")

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amzn = 3000
aapl = 100
fb = 250
goog = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.


# Asking the client his name
client = input('What is your name? ')
print(client)

# Asking the client how much money for investment is available
investment_amount = input('How much savings do you have to invest? ')

# Changing the string to an integer
investment_amount = (int(investment_amount))



# Asking the client which stock is he imnterested in
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. ")

if stock == ('amzn'):
    print('I am interested in Amazon stocks')
elif stock.startswith ('aapl'): 
      print('I am interested in Apple stocks')
elif stock.startswith ('fb'):
      print('I am interested in Facebook stocks')
elif stock.startswith ('goog'): 
      print('I am interested in Google stocks')
elif stock.startswith ('msft'): 
      print('I am interested in Microsoft stocks')
else:
   print('There has been an input error. Please try again') # Having trouble creatinga loop that it should go back to code line 30.

# Calculating how many stock based on the investment amount.
if stock == ('amzn'):
   shares = f'{investment_amount/amzn}'
elif stock.startswith ('aapl'): 
   shares = f'{investment_amount/aapl}'
elif stock.startswith ('fb'):
   shares = f'{investment_amount/fb}'
elif stock.startswith ('msft'): 
   shares = f'{investment_amount/msft}'
elif stock.startswith ('goog'): 
   shares = f'{investment_amount/goog}'



print(f"{client} has {investment_amount} in savings. And he can buy {shares} shares in {stock}.")
