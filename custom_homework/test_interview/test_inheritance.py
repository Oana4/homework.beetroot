from oop_inheritance import Polygon, Square

square_1 = Square("blue", 4, 3)
square_1.compute_area()
print(square_1.display_color_of_figure())
square_1.change_color("yellow")
print(square_1.display_color_of_figure())
print(square_1.num_of_sides)
