class Book:

    amount_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f"The book's name is {self.name}, it was written by {self.author} and " \
               f"the year of publication is {self.year}."

    def __repr__(self):
        return self.__str__()


class Author:

    def __init__(self, name, country, birthday, books=None):
        if books is None:
            books = []
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f"The author's name is {self.name}, he was born in {self.country} on {self.birthday} " \
               f"and he wrote the following books that can be found in our library: {self.books}."

    def __repr__(self):
        return self.__str__()


class Library:

    def __init__(self, name, books=None, authors=None):
        if authors is None:
            authors = set()         # there is only an author
        if books is None:
            books = []              # it can be the same book title but different edition
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: Author):
        # returns an instance of Book class and adds the book to the books list for the current library.
        one_book = Book(name, year, author)
        self.books.append(one_book)
        self.authors.add(author.name)
        # add an extra feature to connect the new book to the list of books of the current author
        # available in our library
        author.books.append(one_book.name)
        Book.amount_of_books += 1
        return one_book

    def group_by_author(self, author: Author):
        # returns a list of all books grouped by the specified author
        return [book.name for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        # returns a list of all the books grouped by the specified year
        return [book.name for book in self.books if book.year == year]

    def __str__(self):
        return f"The library's name is {self.name}. " \
               f"Here, you can find many books, {self.books}, written by the following authors: " \
               f"{self.authors}."

    def __repr__(self):
        return self.__str__()


fav_author = Author('Agatha Christie', 'UK', '15th Sept 1890')
another_author = Author('Andy Weir', 'UK', 'IDK')

book_1 = Book("Death on a plane", 1933, fav_author)
book_2 = Book("Hail Mary Project", 2021, another_author)
book_3 = Book("Crime on Nile", 1915, fav_author)

my_lib = Library('Huge Library')
my_lib.new_book(book_1.name, book_1.year, book_1.author)
my_lib.new_book(book_2.name, book_2.year, book_2.author)
my_lib.new_book(book_3.name, book_3.year, book_3.author)
print(fav_author)
# print(my_lib.__str__())

print(my_lib.group_by_author(fav_author))
print(my_lib.group_by_year(1915))
print(Book.amount_of_books)
