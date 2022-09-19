stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def total_price(new_stock, new_prices):
    total_sum = 0
    for key in new_stock:
        total_sum += new_stock[key] * new_prices[key]
    print("Total price is: ", total_sum)

total_price(stock, prices)