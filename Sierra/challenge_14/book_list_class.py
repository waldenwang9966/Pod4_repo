from book_class import Book


class Booklist():
	def __init__(self):
		"""Initialize the empty book list"""
		self.books = []

	def add(self, title, author):
		"""Add a Book object with the given title and author to the book list"""
		book = Book(title, author)
		self.books.append(book.title)
		self.books.append(book.author)
		# I had it formatted as: self.books.append(f'{book.title} - {book.author}') but then 
		# I couldn't remove the title if it was in self.books for the remove_title method
		
	def count_books(self):
		"""Return the number of books currently in the booklist"""
		print(len(self.books))

	def remove_title(self, title):
		"""Remove a book from the book list"""
		if title in self.books:
			self.books.remove(title)

	def display_titles(self):
		"""Print out all titles currently in the book list"""
		pass

	def is_empty(self):
		"""Return True if the book list is empty, False if not"""
		pass

	
nyt_bestsellers = Booklist()
nyt_bestsellers.add('It Ends With Us', 'Colleen Hoover')
nyt_bestsellers.add('Refugee', 'Alan Gratz')
#print(nyt_bestsellers.books)

	