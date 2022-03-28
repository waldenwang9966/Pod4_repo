# You are starting a bike-sharing service. Your first bike station will be at 14th St and 5 Ave.
# The dictionary below represents your first station.

from unicodedata import name


station = { 
	'name': 'Station A',
 	'address': '14th St and 5 Ave',
 	'bikes': []
}

print('Question 1')

# You don't have any bikes at this station. Create a function 'add' that adds bikes to the bikes list.
# A bike can be represented by an id number in the bikes list
# Parameters: id (int)
# Returns: nothing
def add(id):
    station['bikes'].append(id)
print('')

print('Question 2')
# Create a function 'check_out' to checks out a bike (removes it by id) from the bikes list
# Parameters: id (int)
# Returns: nothing
def check_out(id):
    station['bikes'].remove(id)
print('')

print('Question 3')
# Create a function 'check_in' that returns a bike (adding it by id) to the bikes list.
# Parameters: id (int)
# Returns: nothing
def check_in(id):
    station['bikes'].append(id)
print('')

print('Question 4')
# Congratulations! Your business is expanding. You want to create multiple stations around the city.


# Returns: BikeStation Object
# Create a class BikeStation that has the data (name, address, bikes) and all the functions (add, check_out, check_in)
class Bikestation ():
    def __init__(self, name, address):
        # Parameters to create object: name (string) and address (string)
        self.name = name #intitating 
        self.address = address 
        self.bikes = [] #this is an empty list
    def add(self, id):
        self.bikes.append(id)
    def check_out(self, id):
        self.bikes.remove(id)
    def check_in(self, id):
        self.bikes.append(id)
print('')

print('Question 5')
# You will create station objects using BikeStation class and save them to variables.
# 5.1 - First station, name is Station A. Give it an address of your own choosing. 
# 5.2 - Second station, name is Station B. Give it an address of your own choosing.
station_a = Bikestation("Station A", "Telegraph Ave.")
station_b = Bikestation("Station B","40th Street")
print('')

print('Question 6')
# 6.1 - Add bikes 1, 2, 3 to Station A. 
station_a.add(1)
station_a.add(2)
station_a.add(3)

# #NOTE: version 2
# for i in range(1,4):
#     station_a.add(i)
# # 6.2 - Add bikes 4, 5, 6 to Station B.
# Print the bikes attributes for both Station A and Station B objects.
for i in range(4,7):
    station_b.add(i)
print('')

print('Question 7')
# 7.1 - Check out bike 3 from Station A
station_a.check_out(3)
# 7.2 - Check out bike 5 from  Station B
station_b.check_out(5)
# 7.3 - Check in bike 3 to Station B 
station_b.check_in(3)
# Print the bikes attributes for both Station A and Station B objects.
print(station_a.bikes)
print(station_b.bikes)
print()
print(station_a.bikes + station_b.bikes)