def make_country(name, capital):
    world_map = {'name': name, 'capital': capital}
    for country in world_map.values():
        print(country)


input_name = input("Name a country: ")
input_capital = input("And its capital is.. ")

make_country(input_name, input_capital)


