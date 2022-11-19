"""
Create an application for a small bookstore. Your application would store data about available items in stock -
 books, magazines and other related goods like notebooks, postcards etc.
Main functionality of your application is to track sales and available items' quantity.
Make sure your application supports stock replenishment.
Also, it might be useful to have an easy way to calculate total cost of goods sold for some period (day, week, month).
For books application would keep some additional information like author, the genre of the book,
year of publishing, optional short description.
For magazines, we’re interested to know the month of its publication and possible target audience
 (children, adults, scientists, gardeners etc.)
Use sqlite database for your data storage.
"""

import sqlite3


class Item:
    @classmethod
    def create_table(cls, conn):
        with conn:
            conn.cursor().execute("""CREATE TABLE IF NOT EXISTS items(
                name text,
                type text,
                price integer,
                quantity integer            
                )""")

    def __init__(self, name, item_type, price, quantity):
        self.name = name
        self.item_type = item_type
        self.price = price
        self.quantity = quantity

    def add_item(self, conn):
        with conn:
            c = conn.cursor()
            c.execute("SELECT name FROM items WHERE name = :name and type = :type",
                      {'name': self.name, 'type': self.item_type})
            result = c.fetchone()
            if result is not None:
                c.execute("SELECT quantity FROM items WHERE name = :name and type = :type",
                          {'name': self.name, 'type': self.item_type})
                previous_quantity = c.fetchone()[0]
                c.execute(
                    """UPDATE items SET quantity = :first_quantity + :new_quantity WHERE
                    name = :name AND type = :type""",
                    {'first_quantity': previous_quantity, 'new_quantity': self.quantity,
                     'name': self.name, 'type': self.item_type})
            else:
                c.execute("""INSERT INTO items VALUES (:name, :type, :price, :quantity)""",
                          {'name': self.name, 'type': self.item_type, 'price': self.price,
                           'quantity': self.quantity})

    @classmethod
    def see_all_items(cls, conn):
        with conn:
            c = conn.cursor()
            c.execute("SELECT * FROM items")
        return c.fetchall()

    @classmethod
    def delete_all_items(cls, conn):
        with conn:
            c = conn.cursor()
            c.execute("DELETE FROM items")


class Book(Item):
    def __init__(self, name, price, quantity, author, genre, year):
        super().__init__(name, "Book", price, quantity)
        self.author = author
        self.genre = genre
        self.year = year


class Magazine(Item):
    def __init__(self, name, price, quantity, month, target_audience):
        super().__init__(name, "Magazine", price, quantity)
        self.month = month
        self.target_audience = target_audience


if __name__ == "__main__":
    postcard1 = Item("Happy New Year", "postcard", 5, 1)
    postcard2 = Item("Happy New Year", "postcard", 5, 3)
    postcard3 = Item("Happy Easter", "postcard", 1, 6)
    book1 = Item("1984", "book", 140, 5)
    conn = sqlite3.connect('bookstore.db')
    c = conn.cursor()

    Item.create_table(conn)
    postcard1.add_item(conn)
    book1.add_item(conn)
    postcard2.add_item(conn)
    postcard3.add_item(conn)

    print("See all items from your table! \n")
    print(Item.see_all_items(conn))

    print("Now we'll delete all items from our table! \n")
    Item.delete_all_items(conn)

    print("See the new table! \n")
    print(Item.see_all_items(conn))

    conn.close()
