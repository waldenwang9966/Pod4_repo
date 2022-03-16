from book_class import Book


class Booklist():
	def __init__(self):
		"""Initialize the empty book list"""
		self.books = []
		

	def add(self, title, author):
		"""Add a Book object with the given title and author to the book list"""
		book = Book(title, author)
		self.books.append(book)	

		
	def count_books(self):
		"""Return the number of books currently in the booklist"""
		return len(self.books)
	
	def remove_title(self, title):
		"""Remove a book from the book list"""
		for book in self.books:
			if book.title == title: 
				self.books.remove(book)
		
	# method to display all book titles in alphabetical order
	def display_titles(self):
		print(sorted([book.title for book in self.books]))

	def is_empty(self):
		"""Return True if the book list is empty, False if not"""
		if len(self.books) == 0: 
			return True 
		else: 
			return False

	
	
