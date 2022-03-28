print('Question 1:')
# You are working on a library management system, here are the list books at the library
books = ['MY OWN WORDS', 'WHITE FRAGILITY', 'THE BODY KEEPS THE SCORE', 'SO YOU WANT TO TALK ABOUT RACE', 'STAMPED FROM THE BEGINNING', 'JUST MERCY', 'BORN A CRIME',
         'THE WARMTH OF OTHER SUNS', 'THE COLOR OF LAW', 'THE NEW JIM CROW', 'THE TRUTHS WE HOLD', 'SAPIENS', 'BRAIDING SWEETGRASS', "MY GRANDMOTHER'S HANDS", 'ON TYRANNY']
print()
# 1.0
# What data type is the object 'books'? How do you know?
print()
# It's a string list because of the square brackets and astring list because of the comma's. this can be checked with the type function
print(type(books))
print()
# 1.1
def available_books():
    print(books)
available_books()
print()
# Create a function 'available_books' to print the books list
# Parameters: Not needed for this function
# Return: Not needed for this function

# 1.2
# Run the 'available_books' function

# 1.3
# Create a function 'check_out' that removes a book from the books list
# Parameters: book (string)
# Return: Not needed for this functiod
def check_out(book): #book is paramiter
    books.remove(book) #removing book from books list
check_out('SAPIENS')
print()    
# 1.4
# Check out 'SAPIENS' using the check_out function

# Bonus: Run available_books function again to see if the book was checked out
print(books)
print('SAPIENS' in books) 
print()
# 1.5
# Create a function 'check_in' that adds a book to the books list
# Parameters: book (string)
# Return: Not needed for this function
def check_in(book):
    books.append(book) # tell"s the computer which list we are working on
check_in('SAPIENS')
print()
# 1.6
# Check in 'SAPIENS' using the check_in function

# Bonus: Run available_books function to see if the book was checked in
print('SAPIENS' in books)
available_books()
print()
# 1.7
# Create a function 'search_by_name' that prints 'Available' if exists in books list, 'Not Available' if it doesn't.
def search_by_name(book):
    if 'SAPIENS':
     print('Available')
    else: 
     print('Not Available')


search_by_name(books)
print()
# Parameters: book (string)
# Return: Not needed for this function
print()
# 1.8
# Search for the book 'JUST MERCY'
def search_by_name(book):
    if 'JUST MERCY':
     print('Available')
    else: 
     print('Not Available')

search_by_name(books)
print()

print('Question 2')
# Here's the same list of books, with additional details
books_with_details = [
    {
        'title': 'MY OWN WORDS',
        'author': 'Ruth Bader Ginsburg with Mary Hartnett and Wendy W Williams',
        'description': 'A collection of articles and speeches by the Supreme Court justice.'
    },
    {
        'title': 'WHITE FRAGILITY',
        'author': 'Robin DiAngelo',
        'description': 'Historical and cultural analyses on what causes defensive moves by white people and how this inhibits cross-racial dialogue.'
    },
    {
        'title': 'THE BODY KEEPS THE SCORE',
        'author': 'Bessel van der Kolk',
        'description': 'How trauma affects the body and mind, and innovative treatments for recovery.'
    },
    {
        'title': 'SO YOU WANT TO TALK ABOUT RACE',
        'author': 'Ijeoma Oluo',
        'description': 'A look at the contemporary racial landscape of the United States.'
    },
    {
        'title': 'STAMPED FROM THE BEGINNING',
        'author': 'Ibram X Kendi',
        'description': 'Winner of the 2016 National Book Award for nonfiction. A look at anti-Black racist ideas and their effect on the course of American history.'
    },
    {
        'title': 'JUST MERCY',
        'author': 'Bryan Stevenson',
        'description': 'A civil rights lawyer and MacArthur grant recipient’s memoir of his decades of work to free innocent people condemned to death.'
    },
    {
        'title': 'BORN A CRIME',
        'author': 'Trevor Noah',
        'description': 'A memoir about growing up biracial in apartheid South Africa by the host of “The Daily Show.”'
    },
    {
        'title': 'THE WARMTH OF OTHER SUNS',
        'author': 'Isabel Wilkerson',
        'description': 'An account of the Great Migration of 1915-70, in which six million African-Americans abandoned the South.'
    },
    {
        'title': 'THE COLOR OF LAW',
        'author': 'Richard Rothstein',
        'description': 'A case for how the American government abetted racial segregation in metropolitan areas across the country.'
    },
    {
        'title': 'THE NEW JIM CROW',
        'author': 'Michelle Alexander',
        'description': 'A law professor on the “war on drugs” and its role in the disproportionate incarceration of Black men.'
    },
    {
        'title': 'THE TRUTHS WE HOLD',
        'author': 'Kamala Harris',
        'description': 'A memoir by the daughter of immigrants who is now a California senator and the 2020 Democratic candidate for vice president.'
    },
    {
        'title': 'SAPIENS',
        'author': 'Yuval Noah Harari',
        'description': 'How Homo sapiens became Earth’s dominant species.'
    },
    {
        'title': 'BRAIDING SWEETGRASS',
        'author': 'Robin Wall Kimmerer',
        'description': 'A botanist and member of the Citizen Potawatomi Nation espouses having an understanding and appreciation of plants and animals.'
    },
    {
        'title': 'MY GRANDMOTHER\'S HANDS',
        'author': 'Resmaa Menakem',
        'description': 'A therapist who specializes in trauma, body-centered psychotherapy and violence prevention explains racism\'s effect on the body.'
    },
    {
        'title': 'ON TYRANNY',
        'author': 'Timothy Snyder',
        'description': 'Twenty lessons from the 20th century about the course of tyranny.'
    },
    {
        'title': 'THE ROAD TO UNFREEDOM',
        'author': 'Timothy Snyder',
        'description': 'Snyder explores Russian attempts to influence Western democracies and the influence of philosopher Ivan Ilyin on Russian President Vladimir Putin and the Russian Federation in general.'
    }
]
print()
# 2.0
# Describe the structure of the data in books_with_details. What types of data are nested within others? How do you know?
# Answer: these are keys and values both strings' all dictonaries 
# 2.1
# Create a function 'count_books' that returns the number of books in the books_with_details list
def count_books(books_with_details):
    print(len(books_with_details))
count_books(books_with_details)

# Parameters: Not needed for this function
# Return: number of books (integer)
print()
# 2.2
# Check the number of books available in the books list using the count_books function
def count_books(books):
    print(len(books))
count_books(books)# 2.3
# Create a function 'search_by_author' that returns the titles of books by an author
def search_by_author(author):
    author_books = []
    for book in books_with_details:
        if book ['author'] == author:
            author_books.append(book['title'])
    return author_books


# Parameters - author (string)
# Return - author's books (list of strings)
# Hint - You will need a for loop, if statement, .append() for this solution!


# 2.4
print(search_by_author('Timothy_Snyder'))

 
# Search for book titles by the author 'Timothy Snyder' using the search_by_author function
