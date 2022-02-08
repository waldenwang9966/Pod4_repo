# print temp of 100 celsius var is celsius_100 
# wanted to make sue I knew what it was doing
celsius_100 = 100 
print(celsius_100)

# to convert F to C 
#Use the formula -32 * 5/9.
#The result is Float due to division "/"
celsius_100 = (100 - 32) * 5/9
print(celsius_100)

# convert deg F to 0 deg C 
# variable "celsius_0" --  utilize the same fomula given and still result in a Float
celsius_0 = (0 - 32) * 5/9
print(celsius_0)

# convert 34.2 deg F to deg C without variables and all in one line
print((34.2 - 32) * 5/9)

# convert temp 5 deg C to F 
# using f * 1.8 + 32
print ((5*1.8) + 32)

# Which is hotter 30.2 C or 85.1 F?
# 30.2 C is hotter than 85.1 F 
celsius_temp = (30.2 * 1.8) + 32
print(celsius_temp)
# To check and see if 30.2 is hotter... used f string to cnvert 30.2 degrees C to F
print(f'30.2 degrees C converts to 86.36 degrees F; which is hotter than 85.1 degrees F')