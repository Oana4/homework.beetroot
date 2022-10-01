from task2_classes import Author, Book, Library

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
