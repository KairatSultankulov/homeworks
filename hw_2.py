class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return (self.__side_length ** 2)

    def info(self):
        area = self.calculate_area()
        print(f'Square side length: {self.__side_length} {Figure.unit}, area: {area} {Figure.unit}')

class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return (self.__width * self.__height)

    def info(self):
        area = self.calculate_area()
        print(f'Rectangle side width: {self.__width} {Figure.unit}, height: {self.__height} {Figure.unit}, area: {area} {Figure.unit}')

figures_list = [
    Square(5),
    Square(10),
    Rectangle(5, 8),
    Rectangle(4,8),
    Rectangle(5, 9)
]

for figure in figures_list:
    print(figure.info())

