# You are starting a bike-sharing service. Your first bike station will be at 14th St and 5 Ave.
# The dictionary below represents your first station.

station = { 
	'name': 'Station A',
 	'address': '14th St and 5 Ave',
 	'bikes': []
}

print('Question 1')
def add(id:int):
	station['bikes'].append(id)


# You don't have any bikes at this station. Create a function 'add' that adds bikes to the bikes list.
# A bike can be represented by an id number in the bikes list
# Parameters: id (int)
# Returns: nothing

print('')

print('Question 2')
# Create a function 'check_out' to checks out a bike (removes it by id) from the bikes list
# Parameters: id (int)
# Returns: nothing
def check_out(id:int):
	station['bikes'].remove(id)

print('')

print('Question 3')
# Create a function 'check_in' that returns a bike (adding it by id) to the bikes list.
# Parameters: id (int)
# Returns: nothing

print('')
def check_in(id:int):
	station['bikes'].append(id)

print('Question 4')
# Congratulations! Your business is expanding. You want to create multiple stations around the city.
# Create a class BikeStation that has the data (name, address, bikes) and all the functions (add, check_out, check_in)
# Parameters to create object: name (string) and address (string)
# Returns: BikeStation Object

print('')


class BikeStation(object):
	def _init_(self, name, address):
		self.name = name
		self.address = address
		self.bikes = []
	def add(self, id):
		self.bikes.append(id)
	def check_out(self, id):
		self.bikes.remove(id)
	def check_in(self, id):
		self.bikes.append(id)

		
print('Question 5')
Station_A = BikeStation('Station_A', '14th Street')
Station_B = BikeStation('Station_B', '42nd Street')
print (BikeStation)
# You will create station objects using BikeStation class and save them to variables.
# 5.1 - First station, name is Station A. Give it an address of your own choosing. 
# 5.2 - Second station, name is Station B. Give it an address of your own choosing.

print('')

print('Question 6')
# 6.1 - Add bikes 1, 2, 3 to Station A. 
# 6.2 - Add bikes 4, 5, 6 to Station B.
#tation_A.a Print the bikes attributes for both Station A and Station B objects.
Station_A.add(1)
Station_A.add(2)
Station_A.add(3)

Station_B.add(4)
Station_B.add(5)
Station_B.add(6)
print(Station_A.bikes)
print(Station_B.bikes)

print('')

print('Question 7')

Station_A.check_out(3)
Station_B.check_out(5)
Station_B.check_in(3)


print(Station_A.bikes)
print(Station_B.bikes)
# 7.1 - Check out bike 3 from Station A
# 7.2 - Check out bike 5 from  Station B
# 7.3 - Check in bike 3 to Station B 
# Print the bikes attributes for both Station A and Station B objects.
