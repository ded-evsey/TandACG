from min_square import Point
from n_lines import Line
import math
"""
Пусть на плоскости задан многоугольник
(необязательно выпуклый и необязательно ограниченный)  и точка.
Найти расстояние от этой точки до многоугольника.
"""


def distance(point, line):
    try:
        return abs(
            (
                    line.p2.y - line.p1.y
            ) * point.x - (
                    line.p2.x - line.p1.x
            ) * point.y + line.p2.x * line.p1.y - line.p2.y * line.p1.x
        )/math.sqrt(
            (line.p2.y - line.p1.y) ** 2 + (line.p2.x - line.p1.x) ** 2
        )
    except ZeroDivisionError:
        return 0


if __name__ == '__main__':
    points = []
    for _ in range(int(input('Count points\n'))):
        # points.append(Point.create_point())  # для мануального ввода точек многогранника
        points.append(Point())

    centroid_points = Point(
        sum([point.x for point in points]),
        sum([point.y for point in points])
    )
    points = sorted(points, key=lambda obj: math.atan2(obj.y, obj.x))
    print([
        point.__str__() for point in points
    ])
    print('Точка на удалении от многогранника желательно больше +-10 ')
    point = Point.create_point()
    d = distance(point, Line(points[0], points[1]))
    for i, point_fig in enumerate(points[1:-1]):
        dq = distance(point, Line(point_fig, points[i+1]))
        if dq < d and dq != 0:
            d = dq
    dq = distance(point, Line(points[0], points[-1]))
    if dq < d and dq != 0:
        d = dq
    print(f'расстояние до многоугольника{d}')
