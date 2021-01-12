from min_square import Point, Triangle
import matplotlib.pyplot as plt
"""
23. Для набора из N точек определить количество попадающих внутрь заданного треугольника.
"""


class SmartTriangle(Triangle):
    def in_triangle(self, point):
        flag = 0
        for i, p in enumerate(self.points):
            if (
                (
                    p.y <= point.y < self.points[i-1].y
                ) or (
                    self.points[i-1].y <= point.y < p.y
                )
            ) and (
                point.x < (
                    self.points[i-1].x - p.x
                ) * (
                    point.y - p.y
                ) / (
                    self.points[i-1].y - p.y
                ) + p.x
            ):
                flag = 1 - flag
        if flag > 0:
            return True
        return False

    @classmethod
    def create_triangle(cls):
        return cls(*[Point.create_point() for _ in range(3)])


if __name__ == '__main__':
    triangle = SmartTriangle.create_triangle()
    n = int(input('Enter points count\n'))
    points = [Point() for _ in range(n)]
    points_in_triangle = [point for point in points if triangle.in_triangle(point)]
    print(f'all points = {[p.__str__() for p in points]}')
    print(
        f'points in triangle of coords('
        f'{triangle.__str__("blue")}) = {[p.__str__("green") for p in points_in_triangle]}, '
        f'and this sum = {len(points_in_triangle)}'
    )

    plt.show()
