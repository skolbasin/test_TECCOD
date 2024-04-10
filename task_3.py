import math


class Point:
    def __init__(self, x=0, y=0):
        # Инициализация координат точки
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        # Вычисление расстояния до другой точки
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def get_coordinates(self):
        # Получение координат точки
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        # Изменение координат точки
        self.x = x
        self.y = y

