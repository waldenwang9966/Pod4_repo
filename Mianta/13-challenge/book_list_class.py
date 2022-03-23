from turtle import title
from book_class import Book


class Booklist():
	def __init__(self):

		"""Initialize the empty book list"""
		self.books = []
		
	def add(self, title, author):

		book= Book(title, author)
		self.books.append(book.title)#this made the books above accessible otherwise the book was dimmed and inaccessible.
		self.books.append(book.author)

	def count_books(self):
		"""Return the number of books currently in the booklist"""
		pass
	
		print(len(self.books))

	def remove_title(self, title):
			"""Remove a book from the book list"""
			pass
			if title in self.books:
				self.books.remove(title)

	def display_titles(self):
		
		def is_empty(self):
#Return True if the book list is empty, False if not
			pass

	nyt_bestsellers = Book()

	nyt_bestsellers.add('The Body Keeps The Score', 'Bessel vander Kolk')

	nyt_bestsellers.add('All About Love', 'bell hooks')
	print(nyt_bestsellers.books)