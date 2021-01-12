import random
import matplotlib.pyplot as plt
import math
"""
В заданном наборе из N точек на плоскости найти тройку, образующую треугольник минимальной ненулевой площади
"""

plt.figure()


class Point:
    def __init__(self, x=None, y=None):
        self.x = random.randint(-10, 10) if not x else x
        self.y = random.randint(-10, 10) if not y else y

    def __str__(self, color='red'):
        plt.scatter(self.x, self.y, color=color)
        return f'({self.x},{self.y})'

    @classmethod
    def create_point(cls):
        x, y = input(
            'Введите х, y для точки\n'
        ).split(',')
        return cls(int(x), int(y))


class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.points = [point_1, point_2, point_3]

    def calc_area(self):
        """
        Поиск площди методом полупериметров
        :return: площадь
        """
        a = math.sqrt(
            (self.points[0].x - self.points[1].x) ** 2 + (self.points[0].y - self.points[1].y) ** 2
        )
        b = math.sqrt(
            (self.points[1].x - self.points[2].x) ** 2 + (self.points[1].y - self.points[2].y) ** 2
        )
        c = math.sqrt(
            (self.points[0].x - self.points[2].x) ** 2 + (self.points[0].y - self.points[2].y) ** 2
        )
        p = (a + b + c) / 2

        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def __str__(self, color='green'):
        plt.gca().add_patch(
            plt.Polygon(
                [(p.x, p.y) for p in self.points],
                color=color,
                alpha=0.2
            )
        )
        return f'{[p.__str__("none") for p in self.points]}'


if __name__ == '__main__':
    n = int(input('enter points count \n'))
    plate = []
    for _ in range(n):
        plate.append(Point())
    res_triangle = Triangle(
        plate[0],
        plate[1],
        plate[2]
    )
    min_area = res_triangle.calc_area()

    for i, p1 in enumerate(plate):
        for j, p2 in enumerate(plate):
            for k, p3 in enumerate(plate):
                if i == j == k:
                    continue
                triangle = Triangle(
                    p1, p2, p3
                )
                area = triangle.calc_area()
                if area != 0 and area < min_area:
                    min_area = area
                    res_triangle = triangle
    print(f'all points: {[p.__str__() for p in plate]}')
    print(f'minimum area triangle = {res_triangle}, and his area = {min_area}')
    plt.show()