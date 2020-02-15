class Book:
	def __init__(self,title):
		self.title = title
		self.page = 1

	def read(self):
		print("We are reading the book at the moment and we are at page {0}".format(self.page))

	def bookmark(self, page):
		self.page = page

class Tome:

	def __init__(self,title):
		self.title = title
		self.page = 1

	def read(self):
		print("We are reading the tome at the moment and we are at page %d".format(self.page))

	def bookmark(self, page):
		self.page = page

class Novel(Tome, Book):
	pass

b1 = Novel("Ajah's love life")
b1.read()