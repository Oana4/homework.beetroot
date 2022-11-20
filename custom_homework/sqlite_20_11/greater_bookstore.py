"""
Create an application for a small bookstore.
Your application would store data about available items in stock - books, magazines and other related goods like notebooks, postcards etc.
Main functionality of your application is to track sales and available items quantity.
Make sure your application supports stock replenishment.
Also it might be useful to have an easy way to calculate total cost of goods sold for some period (day, week, month).
For books application would keep some additional information like author, the genre of the book, year of publishing, optional short description.
For magazines we're interested to know the month of its publication and possible target audience (children, adults, scientists, gardeners etc.)
Use sqlite database for your data storage.
"""

import sqlite3
import datetime


class Item:
    registry = []

    def __init__(self, item_id, name, item_type, price, quantity):
        self.id = item_id
        self.name = name
        self.item_type = item_type
        self.price = price
        self.quantity = quantity
        self.registry.append(self)

    @classmethod
    def create_table(cls, connection):
        with connection:
            connection.cursor().execute(
                """CREATE TABLE IF NOT EXISTS items (
                id integer PRIMARY KEY AUTOINCREMENT,
                name text,
                type text,
                price integer,
                quantity integer
                )"""
            )
            connection.cursor().execute(
                """CREATE TABLE IF NOT EXISTS purchases (
                id integer PRIMARY KEY AUTOINCREMENT,
                item_id integer,
                time_sold integer,
                income integer
                )"""
            )

    @classmethod
    def create_or_update(cls, connection, name, item_type, price, quantity):
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT id, quantity FROM items WHERE name = :name and type = :type",
                {"name": name, "type": item_type},
            )
            matches = cursor.fetchall()

            if len(matches) == 0:
                # create new instance
                print("New instance created!")
                cursor.execute(
                    f"""INSERT INTO items(name, type, price, quantity) VALUES (:name, :item_type, :price, :quantity)""",
                    {
                        "name": name,
                        "item_type": item_type,
                        "price": price,
                        "quantity": quantity,
                    },
                )

                cursor.execute(
                    "SELECT id FROM items WHERE name = :name and type = :type",
                    {"name": name, "type": item_type},
                )
                object_id = cursor.fetchone()

                return cls(object_id, name, item_type, price, quantity)

            elif len(matches) == 1:
                # update quantity
                cursor.execute(
                    """UPDATE items 
                    SET quantity = :quantity 
                    WHERE id = :id""",
                    {
                        "quantity": int(matches[0][1]) + quantity,
                        "id": matches[0][0],
                    },
                )

                for item in cls.registry:
                    if item.id == matches[0][0]:
                        print("instance updated!")
                        item.quantity += quantity
                        return item

                return cls(matches[0][0], name, item_type, price, int(matches[0][1]) + quantity)

            else:
                raise sqlite3.DataError(
                    f"You have a duplicate of name {name}, type {item_type} in your database."
                )

    def sell_items(self, connection, sold_quantity):
        if sold_quantity > self.quantity:
            raise ValueError(f"You can't sell more than you have! You only have {self.quantity} items!")
        else:
            self.quantity -= sold_quantity
            with connection:
                cursor = connection.cursor()
                cursor.execute(
                    """UPDATE items 
                    SET quantity = :quantity 
                    WHERE id = :id""",
                    {
                        "id": self.id,
                        "quantity": self.quantity
                    },
                )

    def delete_all(self, connection):
        connection.cursor().execute("DELETE FROM items")


if __name__ == "__main__":
    connection = sqlite3.connect("bookstore2.db")
    cursor = connection.cursor()

    Item.create_table(connection)

    new_test_object = Item.create_or_update(
        connection, "Test name 1", "Test type", 10, 0
    )
    print(new_test_object.quantity)

    new_test_object.sell_items(connection, 4)

    cursor.execute(
       "SELECT * FROM items WHERE name = 'Test name 1' and type = 'Test type'"
    )
    print(cursor.fetchall())
