# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

employee_name = 'Ash Rahman'


lower_name = employee_name.lower()
print(lower_name)
# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list' (use a string method to split the string into a list)
names_list = lower_name.split(" ")
print(names_list)
# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names' (use a string method to join the list into a new string)
joined_names = ".".join(names_list)
print(joined_names)
# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email' (use an f-string to combine the username with the email domain)
email=(f'{joined_names}@ripplemedia.com ')
print(email)

