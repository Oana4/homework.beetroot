class IsNotAvailable(Exception):
    pass


class Product:

    def __init__(self, type_of_product='', name='', price=1):
        self.type_of_product = type_of_product
        self.name = name
        self.price = price
        self.amount = 0
        self.discount = 30

    def __str__(self):
        return f"The product's category is {self.type_of_product}, its name is {self.name}" \
               f"and its initial price is {self.price}. At the moment, we have in stock" \
               f"{self.amount} pcs, at a discount of {self.discount}%!"


class ProductStore:

    def __init__(self):
        self.inventory = {}
        self.income = 0

    def add(self, product, amount):
        # adds a specified quantity of a single product
        # with a predefined price premium for your store(30 percent)
        if amount > 0:
            product.amount += amount
            self.inventory[product] = product.amount
        else:
            raise ValueError("Your amount is too small! Choose a positive integer!")

    def set_discount(self, identifier, percent=30, identifier_type='name'):
        # adds a discount for all products specified by input identifiers (type or name).
        # The discount must be specified in percentage
        if identifier_type == "name":
            for key in self.inventory.keys():
                if key.name == identifier:
                    key.discount = percent
        elif identifier_type == "type":
            for key in self.inventory.keys():
                if key.type_of_product == identifier:
                    key.discount = percent
        else:
            raise ValueError("Identifier type is neither 'type' nor 'name'!")

    def sell_product(self, product_name, amount):
        # removes a particular amount of products from the store if available, in other case raises an error.
        # It also increments income if the sell_product method succeeds.
        for key in self.inventory.keys():
            if key.name == product_name:
                if key.amount >= amount:
                    key.amount -= amount
                    self.income += amount * key.price * (1 - key.discount / 100)
                else:
                    raise IsNotAvailable("We don't have that many in stock!")

    def get_income(self):
        # returns amount of money earned by ProductStore instance.
        print(f"This product store has an income of {self.income}$.")
        return self.income

    def get_all_products(self):
        # returns information about all available products in the store.
        for key in self.inventory.keys():
            if key.amount > 0:
                print(f"{key.name} is available! Here are its details: ")
                print(f"Price {key.price},\nAmount {key.amount},\nDiscount {key.discount}")
            else:
                print(f"Sorry! {key.name} is out of stock!")

    def get_product_info(self, product_name):
        # returns a tuple with product name and amount of items in the store.
        for key in self.inventory.keys():
            if key.name == product_name:
                return key.name, key.amount


# p = Product('Sport', 'Football T-Shirt', 100)
# p2 = Product('Food', 'Ramen', 1.5)
# s = ProductStore()
# s.add(p, 10)
# s.add(p2, 300)
# s.sell_product("Ramen", 10)
#
# assert s.get_product_info('Ramen') == ('Ramen', 290)

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 2)
store = ProductStore()
store.add(p, 2)
store.add(p2, 50)
store.sell_product('Ramen', 50)
store.get_income()
store.get_all_products()
