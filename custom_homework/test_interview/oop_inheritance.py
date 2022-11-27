class Polygon:
    def __init__(self, color, number_of_sides):
        self.color = color
        self.num_of_sides = number_of_sides

    def display_color_of_figure(self):
        return self.color

    def change_color(self, new_color):
        self.color = new_color

    def compute_area(self):
        return f"This polygon has {self.num_of_sides}, but we don't know how to compute its area!"


class Square(Polygon):
    def __init__(self, color, number_of_sides=4, length_of_side=0):
        super().__init__(color, number_of_sides)
        self.length_of_side = length_of_side

    def compute_area(self):
        print(f"Your square area is {4 * self.length_of_side} cm, because your side has {self.length_of_side} cm")


