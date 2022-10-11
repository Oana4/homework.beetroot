class Shop:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Shop name: {self.name}'


class ShoppingList:
    def __init__(self, shops=None):
        if shops is None:
            shops = {}
        self.shops = shops

    def add_shop(self, shop_):
        self.shops[shop_] = []

    def add_to_cart(self, shop_, product):
        self.shops[shop_].append(product)

    def __getitem__(self, dif_shops):
        return dif_shops

    def __iter__(self):
        return ShoppingListIter(self)

    def __str__(self):
        return f"{self.shops}"


class ShoppingListIter:
    def __init__(self, shopping_list_class):
        self._shops = list(shopping_list_class.shops.keys())
        self._class_size = len(shopping_list_class.shops)
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self._class_size:
            new_shop = self._shops[self._current_index]
            self._current_index += 1
            return new_shop
        raise StopIteration


shopping_list = ShoppingList()
shop_1 = Shop("Zara")
shopping_list.add_shop(shop_1)
shop_2 = Shop("H&M")
shopping_list.add_shop(shop_2)
shop_3 = Shop("Stradivarius")
shopping_list.add_shop(shop_3)
shopping_list.add_to_cart(shop_1, "T-shirt")
shopping_list.add_to_cart(shop_1, "Skirt")
shopping_list.add_to_cart(shop_2, "Nothing")
shopping_list.add_to_cart(shop_3, "Dress")

# I want to print now all the products that I want to buy from a specific shop
for each_shop in shopping_list:
    print(f"{each_shop.name}: {shopping_list.shops[each_shop]}")

# output
# Zara: ['T-shirt', 'Skirt']
# H&M: ['Nothing']
# Stradivarius: ['Dress']
